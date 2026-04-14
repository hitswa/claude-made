# Use Case: Building a Slack Slash Command Handler

**Category:** Business / Automation
**Difficulty:** Intermediate

---

## The Problem

Your team wants to type `/status ORD-1234` in Slack and get back a real-time order status without opening three internal tools. You need a small HTTP server that receives Slack's webhook, queries your internal API, and responds with a formatted message — all within Slack's 3-second response deadline.

## Why MADE fits this

Slack slash commands have a strict contract: verify the request signature, respond within 3 seconds, use a specific JSON response format. Missing any of these silently breaks the integration. The Architect bakes the contract into the acceptance criteria. The Builder implements it exactly. The Reviewer checks the signature verification and response format before the endpoint goes live.

---

## Step-by-Step

### 1. Prerequisites

You'll need:
- A Slack app with a slash command configured, pointing at your server's URL
- `SLACK_SIGNING_SECRET` from your Slack app settings
- The internal API endpoint that returns order status

### 2. Run the pipeline

```bash
python -m src.pipeline "Build a Slack slash command handler at src/slack_handler.py using Starlette. It receives POST /slack/status, verifies the Slack request signature using SLACK_SIGNING_SECRET from env, extracts the order ID from the slash command text, calls GET http://internal-api/orders/{id}/status, and returns a Slack-formatted JSON response. Use deferred response pattern if the internal API call might take > 2 seconds."
```

### 3. What the Architect produces (`handoff/task_brief.md`)

```markdown
## Objective
Create src/slack_handler.py: Starlette app handling POST /slack/status with signature verification and deferred response.

## Context Files
- src/main.py    ← mount the new router here, do not rewrite the file

## Acceptance Criteria
1. Endpoint: POST /slack/status
2. Signature verification:
   - Compute HMAC-SHA256 of "v0:{timestamp}:{raw_body}" using SLACK_SIGNING_SECRET.
   - Compare to X-Slack-Signature header (timing-safe comparison).
   - Reject with 403 if invalid or if X-Slack-Request-Timestamp is > 5 minutes old.
3. Parse order ID from request body field `text` (Slack sends form-encoded body).
4. If text is empty or malformed, return 200 with Slack ephemeral message: "Usage: /status <order-id>".
5. Call GET http://internal-api/orders/{order_id}/status (URL from env var INTERNAL_API_URL).
6. Return Slack response JSON:
   - 200 + { "response_type": "ephemeral", "text": "Order {id}: {status}" } on success.
   - 200 + { "response_type": "ephemeral", "text": "Order not found: {id}" } on 404.
   - 200 + { "response_type": "ephemeral", "text": "Service unavailable, try again." } on other errors.
7. All secrets read from environment via python-dotenv.
8. Mount handler on the existing Starlette app in src/main.py.

## Scope Boundaries
- Only modify: src/slack_handler.py (create) and src/main.py (mount only, no other changes).
- Do NOT add database models or session management.

## Edge Cases
- Slack sends duplicate events on retry — handler must be idempotent.
- Internal API timeout (>2s): return immediate Slack response "Fetching status, check back shortly." and log the timeout.
```

### 4. Key implementation patterns

**Signature verification (Builder will produce this):**
```python
import hashlib
import hmac
import time

def verify_slack_signature(body: bytes, timestamp: str, signature: str, secret: str) -> bool:
    if abs(time.time() - float(timestamp)) > 300:
        return False
    base = f"v0:{timestamp}:{body.decode()}"
    expected = "v0=" + hmac.new(secret.encode(), base.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)
```

**Slack response format:**
```json
{
  "response_type": "ephemeral",
  "text": "Order ORD-1234: Shipped — expected delivery April 18"
}
```

### 5. Test it locally

```bash
uvicorn src.main:app --reload --port 8000

# Simulate a Slack request (skip signature check in dev by mocking)
curl -X POST http://localhost:8000/slack/status \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "text=ORD-1234&user_id=U123"
```

For production testing, use [ngrok](https://ngrok.com) to expose your local server and configure the Slack app to point at the ngrok URL.

---

## Tips

- **Never skip signature verification, even in staging.** It's the only thing preventing anyone on the internet from calling your endpoint. The Architect bakes it into criterion #2 so the Builder cannot omit it.
- **Always return HTTP 200 to Slack, even for errors.** Slack treats non-200 as a failed delivery and retries. Error messages should go in the `text` field of the JSON body.
- **Use ephemeral responses for status commands.** `"response_type": "ephemeral"` means only the user who typed the command sees the response. Use `"in_channel"` only when the answer is useful to the whole channel.
