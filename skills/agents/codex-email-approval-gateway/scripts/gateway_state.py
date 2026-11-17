#!/usr/bin/env python3
"""Secure local state for Codex email approvals and 5% quota alerts."""
from __future__ import annotations

import argparse
import fcntl
import json
import os
import re
import secrets
import stat
import tempfile
from datetime import datetime, timedelta, timezone
from email.utils import parseaddr
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1
REQUEST_ID_RE = re.compile(r"^[a-f0-9]{16,64}$")
BUCKETS = {"five_hour", "weekly"}


class StateError(ValueError):
    pass


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def parse_time(value: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc:
        raise StateError("timestamp must be ISO-8601") from exc
    if parsed.tzinfo is None:
        raise StateError("timestamp must include a timezone")
    return parsed.astimezone(timezone.utc)


def timestamp(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def empty_state() -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "quota_alerts": {},
        "approval_requests": {},
    }


def _secure_parent(path: Path) -> None:
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    mode = stat.S_IMODE(path.parent.stat().st_mode)
    if mode & 0o077:
        raise StateError("state directory permissions must be 700")


def _lock(path: Path):
    _secure_parent(path)
    lock_path = path.with_name(path.name + ".lock")
    fd = os.open(lock_path, os.O_CREAT | os.O_RDWR, 0o600)
    os.fchmod(fd, 0o600)
    fcntl.flock(fd, fcntl.LOCK_EX)
    return fd


def _unlock(fd: int) -> None:
    fcntl.flock(fd, fcntl.LOCK_UN)
    os.close(fd)


def load_state(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    _secure_parent(p)
    if not p.exists():
        return empty_state()
    mode = stat.S_IMODE(p.stat().st_mode)
    if mode & 0o077:
        raise StateError("state file permissions must be 600")
    try:
        state = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise StateError("state file is unreadable or invalid JSON") from exc
    if not isinstance(state, dict) or state.get("schema_version") != SCHEMA_VERSION:
        raise StateError("unsupported state schema")
    if not isinstance(state.get("quota_alerts"), dict):
        raise StateError("quota_alerts must be an object")
    if not isinstance(state.get("approval_requests"), dict):
        raise StateError("approval_requests must be an object")
    return state


def save_state(path: str | Path, state: dict[str, Any]) -> None:
    p = Path(path)
    _secure_parent(p)
    fd = _lock(p)
    temp_name = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=p.parent, prefix=".gateway-", delete=False
        ) as temp:
            temp_name = temp.name
            os.fchmod(temp.fileno(), 0o600)
            json.dump(state, temp, sort_keys=True, separators=(",", ":"))
            temp.write("\n")
            temp.flush()
            os.fsync(temp.fileno())
        os.replace(temp_name, p)
        os.chmod(p, 0o600)
    finally:
        if temp_name and os.path.exists(temp_name):
            os.unlink(temp_name)
        _unlock(fd)


def create_request(
    state: dict[str, Any],
    *,
    codex_thread_id: str,
    codex_host_id: str,
    task_label: str,
    action_summary: str,
    created_at: str | None = None,
    expires_hours: float = 24,
) -> dict[str, str]:
    if not codex_thread_id.strip() or not codex_host_id.strip():
        raise StateError("Codex thread and host IDs are required")
    if not task_label.strip() or len(task_label) > 120:
        raise StateError("task label must be 1 to 120 characters")
    if not action_summary.strip() or len(action_summary) > 1000:
        raise StateError("action summary must be 1 to 1000 characters")
    if not 0 < expires_hours <= 24:
        raise StateError("approval expiry must be between 0 and 24 hours")
    created = parse_time(created_at) if created_at else now_utc()
    request_id = secrets.token_hex(12)
    record = {
        "request_id": request_id,
        "codex_thread_id": codex_thread_id.strip(),
        "codex_host_id": codex_host_id.strip(),
        "task_label": task_label.strip(),
        "action_summary": action_summary.strip(),
        "created_at": timestamp(created),
        "expires_at": timestamp(created + timedelta(hours=expires_hours)),
        "gmail_thread_id": None,
        "gmail_message_id": None,
        "status": "pending",
        "decision": None,
        "decision_message_id": None,
        "processed_at": None,
    }
    state.setdefault("approval_requests", {})[request_id] = record
    return {
        "request_id": request_id,
        "created_at": record["created_at"],
        "expires_at": record["expires_at"],
        "subject": f"Codex Approval [{request_id}] {record['task_label']}",
    }


def bind_email(
    state: dict[str, Any], request_id: str, gmail_thread_id: str, gmail_message_id: str
) -> None:
    record = state.get("approval_requests", {}).get(request_id)
    if not record or record.get("status") != "pending":
        raise StateError("approval request is not pending")
    if not gmail_thread_id.strip() or not gmail_message_id.strip():
        raise StateError("Gmail thread and message IDs are required")
    record["gmail_thread_id"] = gmail_thread_id.strip()
    record["gmail_message_id"] = gmail_message_id.strip()


def pending_requests(state: dict[str, Any], now: str | None = None) -> list[dict[str, str]]:
    current = parse_time(now) if now else now_utc()
    pending = []
    for record in state.get("approval_requests", {}).values():
        if record.get("status") != "pending":
            continue
        expires = parse_time(record["expires_at"])
        if current >= expires:
            record["status"] = "expired"
            record["processed_at"] = timestamp(current)
            continue
        if not record.get("gmail_thread_id") or not record.get("gmail_message_id"):
            continue
        pending.append({
            key: str(record[key])
            for key in ("request_id", "codex_thread_id", "codex_host_id", "task_label",
                        "action_summary", "created_at", "expires_at", "gmail_thread_id",
                        "gmail_message_id")
        })
    return pending


def decision_from_reply(
    state: dict[str, Any],
    *,
    request_id: str,
    gmail_thread_id: str,
    gmail_message_id: str,
    sender: str,
    verified_self_address: str,
    subject: str,
    first_unquoted_line: str,
    received_at: str,
    now: str | None = None,
) -> str:
    record = state.get("approval_requests", {}).get(request_id)
    if not record or record.get("status") != "pending":
        raise StateError("approval request is not pending")
    if not record.get("gmail_thread_id") or gmail_thread_id != record["gmail_thread_id"]:
        raise StateError("reply is not in the registered Gmail thread")
    if not gmail_message_id or gmail_message_id == record.get("gmail_message_id"):
        raise StateError("reply message ID does not identify a new reply")
    if request_id not in subject:
        raise StateError("reply subject does not contain the request ID")
    sender_address = parseaddr(sender)[1].strip().casefold()
    verified_address = parseaddr(verified_self_address)[1].strip().casefold()
    if not verified_address or sender_address != verified_address:
        raise StateError("reply sender is not the authenticated self-address")
    received = parse_time(received_at)
    created = parse_time(record["created_at"])
    expires = parse_time(record["expires_at"])
    current = parse_time(now) if now else now_utc()
    if received <= created or current >= expires:
        raise StateError("reply is stale or expired")
    line = first_unquoted_line.strip().casefold()
    if line == "i approve":
        return "approved"
    if line == "i decline":
        return "declined"
    raise StateError("reply must begin with exactly I approve or I decline")


def mark_relayed(
    state: dict[str, Any],
    *,
    request_id: str,
    decision: str,
    email_message_id: str,
    codex_message_id: str,
    processed_at: str | None = None,
) -> None:
    record = state.get("approval_requests", {}).get(request_id)
    if decision not in {"approved", "declined"}:
        raise StateError("decision must be approved or declined")
    if not email_message_id.strip() or not codex_message_id.strip():
        raise StateError("email and Codex message IDs are required")
    if not record:
        raise StateError("approval request is unknown")
    if record.get("status") != "pending":
        if record.get("decision") == decision and record.get("email_reply_id") == email_message_id:
            return
        raise StateError("approval request was already processed")
    record.update({
        "status": "relayed",
        "decision": decision,
        "email_reply_id": email_message_id,
        "decision_message_id": codex_message_id,
        "processed_at": timestamp(parse_time(processed_at) if processed_at else now_utc()),
    })


def plan_quota_alerts(
    state: dict[str, Any],
    *,
    five_hour_used: float | None,
    five_hour_reset: str | None,
    weekly_used: float | None,
    weekly_reset: str | None,
) -> list[dict[str, Any]]:
    candidates = {
        "five_hour": (five_hour_used, five_hour_reset),
        "weekly": (weekly_used, weekly_reset),
    }
    alerts = []
    for bucket, (used, reset) in candidates.items():
        if used is None or reset is None:
            continue
        if not isinstance(used, (int, float)) or not 0 <= float(used) <= 100:
            continue
        if 100 - float(used) > 5:
            continue
        previous = state.setdefault("quota_alerts", {}).get(bucket, {})
        reset_key = str(reset)
        if previous.get("reset_at") == reset_key:
            continue
        alerts.append({
            "bucket": bucket,
            "remaining_percent": round(100 - float(used), 2),
            "reset_at": reset_key,
        })
    return alerts


def mark_quota_alert_sent(
    state: dict[str, Any], *, bucket: str, reset_at: str, message_id: str
) -> None:
    if bucket not in BUCKETS:
        raise StateError("bucket must be five_hour or weekly")
    if not reset_at.strip() or not message_id.strip():
        raise StateError("reset time and sent message ID are required")
    state.setdefault("quota_alerts", {})[bucket] = {
        "reset_at": reset_at.strip(),
        "message_id": message_id.strip(),
        "sent_at": timestamp(now_utc()),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init")
    sub.add_parser("pending")

    new = sub.add_parser("new-approval")
    new.add_argument("--codex-thread-id", required=True)
    new.add_argument("--codex-host-id", required=True)
    new.add_argument("--task-label", required=True)
    new.add_argument("--action-summary", required=True)
    new.add_argument("--expires-hours", type=float, default=24)

    bind = sub.add_parser("bind-email")
    bind.add_argument("--request-id", required=True)
    bind.add_argument("--gmail-thread-id", required=True)
    bind.add_argument("--gmail-message-id", required=True)

    validate = sub.add_parser("validate-reply")
    validate.add_argument("--request-id", required=True)
    validate.add_argument("--gmail-thread-id", required=True)
    validate.add_argument("--gmail-message-id", required=True)
    validate.add_argument("--sender", required=True)
    validate.add_argument("--verified-self-address", required=True)
    validate.add_argument("--subject", required=True)
    validate.add_argument("--first-unquoted-line", required=True)
    validate.add_argument("--received-at", required=True)

    relayed = sub.add_parser("mark-relayed")
    relayed.add_argument("--request-id", required=True)
    relayed.add_argument("--decision", choices=["approved", "declined"], required=True)
    relayed.add_argument("--email-message-id", required=True)
    relayed.add_argument("--codex-message-id", required=True)

    alerts = sub.add_parser("plan-quota-alerts")
    alerts.add_argument("--five-hour-used", type=float)
    alerts.add_argument("--five-hour-reset")
    alerts.add_argument("--weekly-used", type=float)
    alerts.add_argument("--weekly-reset")

    sent = sub.add_parser("mark-quota-alert-sent")
    sent.add_argument("--bucket", choices=sorted(BUCKETS), required=True)
    sent.add_argument("--reset-at", required=True)
    sent.add_argument("--message-id", required=True)

    args = parser.parse_args()
    path = Path(args.state)
    try:
        state = load_state(path)
        if args.command == "init":
            save_state(path, state)
            result: Any = {"status": "initialized"}
        elif args.command == "new-approval":
            result = create_request(
                state,
                codex_thread_id=args.codex_thread_id,
                codex_host_id=args.codex_host_id,
                task_label=args.task_label,
                action_summary=args.action_summary,
                expires_hours=args.expires_hours,
            )
            save_state(path, state)
        elif args.command == "bind-email":
            bind_email(state, args.request_id, args.gmail_thread_id, args.gmail_message_id)
            save_state(path, state)
            result = {"status": "bound"}
        elif args.command == "pending":
            result = {"requests": pending_requests(state)}
            save_state(path, state)
        elif args.command == "validate-reply":
            result = {"decision": decision_from_reply(
                state,
                request_id=args.request_id,
                gmail_thread_id=args.gmail_thread_id,
                gmail_message_id=args.gmail_message_id,
                sender=args.sender,
                verified_self_address=args.verified_self_address,
                subject=args.subject,
                first_unquoted_line=args.first_unquoted_line,
                received_at=args.received_at,
            )}
        elif args.command == "mark-relayed":
            mark_relayed(
                state,
                request_id=args.request_id,
                decision=args.decision,
                email_message_id=args.email_message_id,
                codex_message_id=args.codex_message_id,
            )
            save_state(path, state)
            result = {"status": "relayed"}
        elif args.command == "plan-quota-alerts":
            result = {"alerts": plan_quota_alerts(
                state,
                five_hour_used=args.five_hour_used,
                five_hour_reset=args.five_hour_reset,
                weekly_used=args.weekly_used,
                weekly_reset=args.weekly_reset,
            )}
        elif args.command == "mark-quota-alert-sent":
            mark_quota_alert_sent(
                state, bucket=args.bucket, reset_at=args.reset_at, message_id=args.message_id
            )
            save_state(path, state)
            result = {"status": "marked"}
        else:
            raise StateError("unknown command")
    except StateError as exc:
        print(json.dumps({"status": "invalid", "reason": str(exc)}))
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
