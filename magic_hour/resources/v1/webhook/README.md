# Magic Hour Webhook Verification

Secure webhook verification for Magic Hour API events. This module provides utilities to verify webhook signatures and parse webhook events from Magic Hour's webhook system.

## Overview

Magic Hour sends webhooks to notify your application about status changes for your video, image, and audio projects. This webhook verification system ensures that the events you receive are authentic and from Magic Hour's systems.

## Security

Magic Hour signs all webhook events using HMAC-SHA256 with your webhook secret. The webhook verification system:

- Verifies webhook signatures to ensure authenticity
- Checks timestamps to prevent replay attacks
- Provides secure comparison to prevent timing attacks
- Follows the same security patterns as Stripe's webhook system

## Event Types

Magic Hour sends the following webhook event types:

### Video Events
- `video.started` - Video processing has started
- `video.completed` - Video processing completed successfully  
- `video.errored` - Video processing failed

### Image Events
- `image.started` - Image processing has started
- `image.completed` - Image processing completed successfully
- `image.errored` - Image processing failed

### Audio Events
- `audio.started` - Audio processing has started
- `audio.completed` - Audio processing completed successfully
- `audio.errored` - Audio processing failed

## Quick Start

### 1. Basic Usage with Flask

```python
from flask import Flask, request, jsonify
from magic_hour.resources.v1.webhook import Webhook, SignatureVerificationError

app = Flask(__name__)
WEBHOOK_SECRET = "whsec_your_webhook_secret_from_magic_hour"

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('magic-hour-event-signature')
    timestamp_header = request.headers.get('magic-hour-event-timestamp')
    
    try:
        event = Webhook.construct_event(
            payload, sig_header, timestamp_header, WEBHOOK_SECRET
        )
        
        # Handle different event types
        if event.type == 'video.completed':
            handle_video_completed(event.payload)
        elif event.type == 'image.completed':
            handle_image_completed(event.payload)
        elif event.type.endswith('.errored'):
            handle_error(event.payload)
            
        return jsonify({"status": "success"})
        
    except SignatureVerificationError as e:
        print(f"Webhook signature verification failed: {e}")
        return jsonify({"error": "Invalid signature"}), 400
    except Exception as e:
        print(f"Error processing webhook: {e}")
        return jsonify({"error": "Processing failed"}), 500

def handle_video_completed(payload):
    project_id = payload['id']
    downloads = payload.get('downloads', [])
    print(f"Video {project_id} completed with {len(downloads)} files")

def handle_image_completed(payload):
    project_id = payload['id']
    downloads = payload.get('downloads', [])
    print(f"Image {project_id} completed with {len(downloads)} files")

def handle_error(payload):
    project_id = payload['id']
    error = payload.get('error', {})
    print(f"Project {project_id} failed: {error.get('message', 'Unknown error')}")
```

### 2. Using WebhookClient

```python
from magic_hour.resources.v1.webhook import WebhookClient
import httpx

# Initialize client with your webhook secret
webhook_client = WebhookClient(webhook_secret="whsec_your_secret")

def handle_webhook_request(request: httpx.Request):
    try:
        event = webhook_client.parse_event(request)
        
        print(f"Received {event.type} event")
        print(f"Project ID: {event.payload.get('id')}")
        print(f"Status: {event.payload.get('status')}")
        
        return {"status": "success"}
        
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}, 400
```

### 3. FastAPI Example

```python
from fastapi import FastAPI, Request, HTTPException
from magic_hour.resources.v1.webhook import Webhook, SignatureVerificationError

app = FastAPI()
WEBHOOK_SECRET = "whsec_your_webhook_secret"

@app.post("/webhook")
async def webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("magic-hour-event-signature")
    timestamp_header = request.headers.get("magic-hour-event-timestamp")
    
    try:
        event = Webhook.construct_event(
            payload, sig_header, timestamp_header, WEBHOOK_SECRET
        )
        
        # Process the event
        await process_webhook_event(event)
        
        return {"status": "success"}
        
    except SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def process_webhook_event(event):
    if event.type in ['video.completed', 'image.completed', 'audio.completed']:
        # Download completed files
        for download in event.payload.get('downloads', []):
            print(f"File available: {download['url']}")
    elif event.type.endswith('.errored'):
        # Handle errors
        error = event.payload.get('error', {})
        print(f"Processing failed: {error.get('message')}")
```

## Advanced Usage

### Custom Timestamp Tolerance

By default, webhooks are considered valid for 5 minutes (300 seconds). You can customize this:

```python
from magic_hour.resources.v1.webhook import Webhook

# Allow webhooks up to 10 minutes old
event = Webhook.construct_event(
    payload, sig_header, timestamp_header, secret, tolerance=600
)

# Disable timestamp checking (not recommended for production)
event = Webhook.construct_event(
    payload, sig_header, timestamp_header, secret, tolerance=None
)
```

### Manual Signature Verification

For more control, you can use the `WebhookSignature` class directly:

```python
from magic_hour.resources.v1.webhook import WebhookSignature, SignatureVerificationError

try:
    WebhookSignature.verify_header(
        payload=request_body,
        sig_header=request.headers.get('magic-hour-event-signature'),
        timestamp_header=request.headers.get('magic-hour-event-timestamp'),
        secret=webhook_secret,
        tolerance=300
    )
    # Signature is valid, process the webhook
    import json
    data = json.loads(request_body)
    
except SignatureVerificationError as e:
    print(f"Invalid signature: {e}")
```

### Error Handling

The webhook system raises specific exceptions for different failure scenarios:

```python
from magic_hour.resources.v1.webhook import Webhook, SignatureVerificationError

try:
    event = Webhook.construct_event(payload, sig_header, timestamp_header, secret)
    
except SignatureVerificationError as e:
    # Handle signature verification failures
    print(f"Signature verification failed: {e}")
    print(f"Provided signature: {e.sig_header}")
    print(f"Payload: {e.payload}")
    
except ValueError as e:
    # Handle malformed payloads or missing data
    print(f"Invalid webhook data: {e}")
    
except Exception as e:
    # Handle other unexpected errors
    print(f"Unexpected error: {e}")
```

## Webhook Event Structure

All webhook events follow this structure:

```json
{
  "type": "video.completed",
  "payload": {
    "id": "project_id",
    "name": "Project Name",
    "status": "complete",
    "type": "FACE_SWAP",
    "created_at": "2023-11-07T05:31:56Z",
    "enabled": true,
    "credits_charged": 5,
    "downloads": [
      {
        "url": "https://videos.magichour.ai/id/output.mp4",
        "expires_at": "2024-10-19T05:16:19.027Z"
      }
    ],
    "error": null
  }
}
```

### Event Fields

- `type`: The event type (e.g., "video.completed", "image.started")
- `payload`: The event data containing project information
  - `id`: Unique project identifier
  - `name`: Project name as provided during creation
  - `status`: Current project status ("processing", "complete", "error")
  - `type`: Project type (e.g., "FACE_SWAP", "TEXT_TO_VIDEO")
  - `created_at`: Project creation timestamp
  - `enabled`: Whether the project is enabled
  - `credits_charged`: Number of credits used
  - `downloads`: Array of download URLs (for completed projects)
  - `error`: Error information (for failed projects)

## Testing Webhooks

### Testing with ngrok

For local development, use ngrok to expose your local server:

```bash
# Install ngrok
npm install -g ngrok

# Expose your local server
ngrok http 3000

# Use the provided URL in Magic Hour Developer Hub
# Example: https://abc123.ngrok.io/webhook
```

### Testing Signature Verification

```python
import hmac
import json
import time
from hashlib import sha256

def create_test_webhook():
    secret = "whsec_test_secret"
    payload = json.dumps({
        "type": "video.completed",
        "payload": {"id": "test_id", "status": "complete"}
    })
    timestamp = str(int(time.time()))
    
    # Create signature like Magic Hour does
    signed_payload = f"{timestamp}.{payload}"
    signature = hmac.new(
        secret.encode("utf-8"),
        signed_payload.encode("utf-8"),
        sha256
    ).hexdigest()
    
    return payload, signature, timestamp

# Test the webhook
payload, signature, timestamp = create_test_webhook()
event = Webhook.construct_event(payload, signature, timestamp, "whsec_test_secret")
print(f"Test event: {event.type}")
```

## Security Best Practices

1. **Always verify signatures**: Never process webhooks without signature verification
2. **Use HTTPS**: Ensure your webhook endpoint uses HTTPS in production
3. **Keep secrets secure**: Store webhook secrets in environment variables
4. **Implement idempotency**: Handle duplicate webhook deliveries gracefully
5. **Respond quickly**: Return a 2xx status code within 5 seconds
6. **Log failures**: Log signature verification failures for monitoring

## Troubleshooting

### Common Issues

**"Missing signature header"**
- Ensure your endpoint receives the `magic-hour-event-signature` header
- Check if your reverse proxy strips headers

**"Signature verification failed"**
- Verify you're using the correct webhook secret
- Ensure the payload is not modified (no whitespace changes, encoding issues)
- Check if your framework automatically parses JSON (use raw body)

**"Timestamp outside tolerance zone"**
- Check your server's system clock
- Increase tolerance if network delays are causing issues
- Ensure you're using the raw timestamp header value

**"Invalid JSON payload"**
- Use the raw request body, don't pre-parse JSON
- Check for encoding issues (should be UTF-8)

### Getting Help

- Visit [Magic Hour Documentation](https://docs.magichour.ai/integration/webhook)
- Join our [Discord community](https://discord.gg/JX5rgsZaJp)
- Email support@magichour.ai

## API Reference

### Classes

- **`Webhook`**: Main utility class with static methods
- **`WebhookClient`**: Client class that can store webhook secrets
- **`WebhookEvent`**: Represents a parsed webhook event
- **`WebhookSignature`**: Low-level signature verification utilities
- **`SignatureVerificationError`**: Exception for signature verification failures

### Methods

- **`Webhook.construct_event()`**: Verify and parse webhook event
- **`WebhookClient.parse_event()`**: Parse event from httpx.Request
- **`WebhookSignature.verify_header()`**: Low-level signature verification
