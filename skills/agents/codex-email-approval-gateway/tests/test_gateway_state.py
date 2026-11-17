import tempfile
import unittest
from pathlib import Path

from scripts.gateway_state import (
    StateError,
    bind_email,
    create_request,
    decision_from_reply,
    empty_state,
    mark_quota_alert_sent,
    mark_relayed,
    plan_quota_alerts,
    save_state,
)


class GatewayStateTests(unittest.TestCase):
    def test_quota_alerts_fire_once_per_reset_window(self):
        state = empty_state()
        alerts = plan_quota_alerts(
            state, five_hour_used=95, five_hour_reset="five-reset-1",
            weekly_used=95, weekly_reset="week-reset-1",
        )
        self.assertEqual({a["bucket"] for a in alerts}, {"five_hour", "weekly"})
        mark_quota_alert_sent(
            state, bucket="weekly", reset_at="week-reset-1", message_id="sent-1"
        )
        self.assertEqual(
            [a["bucket"] for a in plan_quota_alerts(
                state, five_hour_used=95, five_hour_reset="five-reset-1",
                weekly_used=96, weekly_reset="week-reset-1",
            )],
            ["five_hour"],
        )
        self.assertEqual(
            [a["bucket"] for a in plan_quota_alerts(
                state, five_hour_used=95, five_hour_reset="five-reset-2",
                weekly_used=96, weekly_reset="week-reset-2",
            )],
            ["five_hour", "weekly"],
        )

    def test_no_quota_alert_above_five_percent_remaining(self):
        state = empty_state()
        self.assertEqual(
            plan_quota_alerts(
                state, five_hour_used=94.99, five_hour_reset="r1",
                weekly_used=80, weekly_reset="r2",
            ),
            [],
        )

    def test_valid_approval_reply_requires_same_thread_and_self_sender(self):
        state = empty_state()
        request = create_request(
            state, codex_thread_id="task-1", codex_host_id="local",
            task_label="Example", action_summary="Send the approved report",
            created_at="2026-11-14T12:00:00Z",
        )
        bind_email(state, request["request_id"], "gmail-thread-1", "sent-message-1")
        self.assertEqual(
            decision_from_reply(
                state, request_id=request["request_id"], gmail_thread_id="gmail-thread-1",
                gmail_message_id="reply-1", sender="Owner <owner@example.com>",
                verified_self_address="owner@example.com",
                subject=request["subject"], first_unquoted_line="I approve",
                received_at="2026-11-14T12:05:00Z", now="2026-11-14T12:06:00Z",
            ),
            "approved",
        )

    def test_decline_is_a_valid_scoped_decision(self):
        state = empty_state()
        request = create_request(
            state, codex_thread_id="task-2", codex_host_id="local",
            task_label="Example", action_summary="Trust local certificate",
            created_at="2026-11-14T12:00:00Z",
        )
        bind_email(state, request["request_id"], "gmail-thread-2", "sent-message-2")
        self.assertEqual(
            decision_from_reply(
                state, request_id=request["request_id"], gmail_thread_id="gmail-thread-2",
                gmail_message_id="reply-2", sender="owner@example.com",
                verified_self_address="owner@example.com",
                subject=request["subject"], first_unquoted_line="I decline",
                received_at="2026-11-14T12:05:00Z", now="2026-11-14T12:06:00Z",
            ),
            "declined",
        )

    def test_wrong_sender_thread_reply_text_and_expiry_are_rejected(self):
        state = empty_state()
        request = create_request(
            state, codex_thread_id="task-3", codex_host_id="local",
            task_label="Example", action_summary="Change access",
            created_at="2026-11-14T12:00:00Z", expires_hours=1,
        )
        bind_email(state, request["request_id"], "gmail-thread-3", "sent-message-3")
        base = dict(
            state=state, request_id=request["request_id"], gmail_thread_id="gmail-thread-3",
            gmail_message_id="reply-3", sender="owner@example.com",
            verified_self_address="owner@example.com", subject=request["subject"],
            first_unquoted_line="I approve", received_at="2026-11-14T12:05:00Z",
            now="2026-11-14T12:06:00Z",
        )
        for change in [
            {"sender":"stranger@example.com"},
            {"gmail_thread_id":"wrong-thread"},
            {"first_unquoted_line":"I approve and also delete the logs"},
            {"now":"2026-11-14T14:00:00Z"},
        ]:
            args={**base,**change}
            with self.assertRaises(StateError):
                decision_from_reply(**args)

    def test_relay_result_is_idempotent_for_same_decision(self):
        state=empty_state()
        request=create_request(
            state,codex_thread_id="task-4",codex_host_id="local",
            task_label="Example",action_summary="Run local check"
        )
        bind_email(state,request["request_id"],"gmail-thread-4","sent-message-4")
        mark_relayed(state,request_id=request["request_id"],decision="approved",
                     email_message_id="reply-4",codex_message_id="codex-message-4")
        mark_relayed(state,request_id=request["request_id"],decision="approved",
                     email_message_id="reply-4",codex_message_id="codex-message-4")
        with self.assertRaises(StateError):
            mark_relayed(state,request_id=request["request_id"],decision="declined",
                         email_message_id="reply-4",codex_message_id="codex-message-5")

    def test_state_file_is_created_with_private_permissions(self):
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)/"private"/"gateway.json"
            state=empty_state()
            save_state(path,state)
            self.assertEqual(path.stat().st_mode & 0o777,0o600)
            self.assertEqual(path.parent.stat().st_mode & 0o777,0o700)


if __name__ == "__main__":
    unittest.main()
