---
name: codex-email-approval-gateway
description: Send scoped approval emails and relay verified replies into the matching Codex task when authenticated Gmail and Codex thread tools are available.
metadata:
  short-description: Relay scoped email approvals to Codex
---

# Codex Email Approval Gateway

Use this skill inside an active task when it needs a user decision by email, processes a reply to its registered request, or observes a quota threshold during a permitted in-chat usage check. It requires authenticated Gmail and, for relays, a Codex thread messaging tool. Never create a recurring poller or new chat for this skill.

## Authorization and scope

- Follow the active Questions that interrupt work rule. Search available context, choose a safe default, and continue independent work before sending a blocker notice.
- Email approval is for one specific user decision. Keep the original task, checkpoint, and scope. Never treat the reply as approval for a different action.
- Do not ask for credentials, passwords, one-time codes, security answers, or secrets by email. A reply cannot complete authentication, MFA, CAPTCHA, or legal consent.
- Native Codex or operating-system approval prompts remain under their own supported approval controls. This gateway can relay a user decision into a Codex task; it cannot claim that a native permission dialog was approved or bypass that dialog.
- Do not search or read unrelated inbox messages. Process only the exact Gmail thread recorded for a pending request.

## Send an approval request

1. Confirm that the missing answer is essential and no safe, useful route remains. Continue all independent safe work.
2. Generate a unique request ID and a short expiration, default 24 hours. Record the Codex thread ID, host ID, task label, exact action scope, and expiration using scripts/gateway_state.py.
3. Send one HTML email to the authenticated self-address using the approved connector. Use the subject format: Codex Approval [REQUEST_ID] TASK_LABEL. State the exact action, target, side effects, relevant cost, and the user's choices. Do not include credentials or raw private prompts.
4. Tell the user to reply in the same thread with exactly I approve or I decline. A free-text answer is allowed for a question request, but it must not authorize a different or expanded action.
5. Verify the sent item and record its Gmail message ID and thread ID. Ask the same concise question in the active Codex task. Do not send duplicate reminders.

## Process replies

The matching active task may check only approval threads registered in its local state file, when that task is active or resumes. Do not run background polling or create a chat to check a reply. It must:

- Read only the registered Gmail thread IDs, verify the Gmail profile's authenticated address, and ignore replies from any other sender.
- Require the reply to be in the exact original Gmail thread, newer than the request, before expiration, and tied to the exact request ID.
- Accept only an unquoted first line that is exactly I approve or I decline, ignoring case and surrounding whitespace. If the reply is ambiguous, forwarded, stale, or contains conflicting decisions, leave the request pending and do not relay it.
- Check the target Codex thread for the request ID before sending, to avoid duplicate relays.
- Send the verified decision only to the recorded Codex thread and host. Include the request ID, task label, exact scope, and decision. Do not copy unrelated email content.
- Mark the request processed only after the Codex message send succeeds. Preserve the message ID and decision for audit.
- Treat an approval as authorization for the exact action in the email. A decline stops only that action; continue other safe work.

## In-chat quota alerts

- Read usage only when the active-task cadence in codex-usage-fallback-router calls for it: before unusually high-cost model work, long/deep research, after a quota warning, or when a recent reading is near a threshold.
- Do not schedule periodic usage checks or email-reply polling. Do not create a new chat to check quota or a reply.
- If an active task observes either bucket at 5% remaining or less, send one HTML email per bucket reset window. Verify Sent before recording the alert.
- At weekly remaining usage of 10% or less, pause all goals and tasks as required by the global quota policy. There is no background monitor; the active task preserves its checkpoint and stops.
- At five-hour remaining usage of 5% or less, use the configured preapproved fallback only when weekly capacity is above the global floor and project data may be sent to that provider.

## State helper

Use `scripts/gateway_state.py` to create the private state file and validate request IDs, expiry, sender, thread, and one-time decisions. Set `STATE` to the approved private state path. The helper stores no email body or credentials. Protect the state directory with mode 700 and the state file with mode 600.

The helper accepts `--state STATE` before its subcommand. Use the returned request ID and subject when sending the email. Bind the Gmail thread and sent-message IDs only after Sent readback confirms the message.

```sh
python3 scripts/gateway_state.py --state "$STATE" init
python3 scripts/gateway_state.py --state "$STATE" pending
python3 scripts/gateway_state.py --state "$STATE" new-approval --codex-thread-id THREAD_ID --codex-host-id HOST_ID --task-label LABEL --action-summary "EXACT ACTION"
python3 scripts/gateway_state.py --state "$STATE" bind-email --request-id REQUEST_ID --gmail-thread-id GMAIL_THREAD_ID --gmail-message-id SENT_MESSAGE_ID
python3 scripts/gateway_state.py --state "$STATE" plan-quota-alerts --five-hour-used FIVE_HOUR_USED --five-hour-reset FIVE_HOUR_RESET --weekly-used WEEKLY_USED --weekly-reset WEEKLY_RESET
python3 scripts/gateway_state.py --state "$STATE" validate-reply --request-id REQUEST_ID --gmail-thread-id GMAIL_THREAD_ID --gmail-message-id REPLY_MESSAGE_ID --sender SENDER --verified-self-address SELF_ADDRESS --subject SUBJECT --first-unquoted-line "I approve" --received-at RFC3339_TIME
python3 scripts/gateway_state.py --state "$STATE" mark-relayed --request-id REQUEST_ID --decision approved --email-message-id REPLY_MESSAGE_ID --codex-message-id CODEX_MESSAGE_ID
python3 scripts/gateway_state.py --state "$STATE" mark-quota-alert-sent --bucket weekly --reset-at WEEKLY_RESET --message-id SENT_MESSAGE_ID
```

Use `decision declined` for a decline and `bucket five_hour` for the five-hour alert. Do not mark a reply or alert sent until the corresponding Codex or Gmail readback succeeds.

## Runtime capability limit

If Gmail or Codex thread messaging is unavailable, do not claim automatic relay. Send the blocker email and ask in the active task under the global rule. After a verified email approval of an exact UI action, Computer Use may navigate and change the setting up to the native authentication prompt, including selecting a visible Use Password option. Stop before entering a password or code. Never ask for, store, echo, or type credentials, even if they appear in chat or email. Ask the user to authenticate on the device; continue only after the supported UI confirms the action. Email approval does not dismiss a native Codex or operating-system permission prompt.
