import hmac
import json
import time
import pytest
from unittest.mock import Mock
from hashlib import sha256

import httpx

from .client import (
    SignatureVerificationError,
    Webhook,
    WebhookClient,
    WebhookEvent,
    WebhookSignature,
)


class TestSignatureVerificationError:
    """Test SignatureVerificationError exception class."""

    def test_init_with_message_only(self):
        error = SignatureVerificationError("Test error")
        assert str(error) == "Test error"
        assert error.sig_header is None
        assert error.payload is None

    def test_init_with_all_params(self):
        error = SignatureVerificationError(
            "Test error", sig_header="sig123", payload="payload123"
        )
        assert str(error) == "Test error"
        assert error.sig_header == "sig123"
        assert error.payload == "payload123"


class TestWebhookEvent:
    """Test WebhookEvent class."""

    def test_init(self):
        payload = {"id": "test_id", "status": "complete"}
        event = WebhookEvent("video.completed", payload)
        assert event.type == "video.completed"
        assert event.payload == payload

    def test_repr(self):
        payload = {"id": "test_id", "status": "complete"}
        event = WebhookEvent("video.completed", payload)
        assert (
            repr(event) == "WebhookEvent(type='video.completed', payload_id='test_id')"
        )

    def test_repr_without_id(self):
        payload = {"status": "complete"}
        event = WebhookEvent("video.completed", payload)
        assert (
            repr(event) == "WebhookEvent(type='video.completed', payload_id='unknown')"
        )


class TestWebhookSignature:
    """Test WebhookSignature utility class."""

    def test_compute_signature(self):
        payload = "test payload"
        secret = "test_secret"
        timestamp = "1234567890"

        signature = WebhookSignature._compute_signature(payload, secret, timestamp)

        # Verify it's a valid hex string
        assert len(signature) == 64  # SHA256 hex digest length
        assert all(c in "0123456789abcdef" for c in signature)

        # Verify reproducibility
        signature2 = WebhookSignature._compute_signature(payload, secret, timestamp)
        assert signature == signature2

    def test_compute_signature_different_inputs(self):
        """Test that different inputs produce different signatures."""
        base_signature = WebhookSignature._compute_signature("payload", "secret", "123")

        # Different payload
        sig1 = WebhookSignature._compute_signature("different", "secret", "123")
        assert sig1 != base_signature

        # Different secret
        sig2 = WebhookSignature._compute_signature("payload", "different", "123")
        assert sig2 != base_signature

        # Different timestamp
        sig3 = WebhookSignature._compute_signature("payload", "secret", "456")
        assert sig3 != base_signature

    def test_secure_compare_equal_strings(self):
        assert WebhookSignature._secure_compare("test", "test") is True
        assert WebhookSignature._secure_compare("", "") is True
        assert WebhookSignature._secure_compare("abc123", "abc123") is True

    def test_secure_compare_different_strings(self):
        assert WebhookSignature._secure_compare("test", "different") is False
        assert WebhookSignature._secure_compare("test", "TEST") is False
        assert WebhookSignature._secure_compare("test", "") is False
        assert WebhookSignature._secure_compare("", "test") is False

    def test_secure_compare_different_lengths(self):
        assert WebhookSignature._secure_compare("short", "much_longer") is False
        assert WebhookSignature._secure_compare("longer", "abc") is False

    def test_verify_header_success(self):
        payload = '{"type":"video.completed","payload":{"id":"test"}}'
        secret = "test_secret"
        timestamp = str(int(time.time()))

        # Create valid signature
        signature = WebhookSignature._compute_signature(payload, secret, timestamp)

        # Should not raise any exception
        result = WebhookSignature.verify_header(
            payload, signature, timestamp, secret, tolerance=300
        )
        assert result is True

    def test_verify_header_missing_signature(self):
        with pytest.raises(SignatureVerificationError) as exc_info:
            WebhookSignature.verify_header("payload", "", "123", "secret")
        assert "Missing signature header" in str(exc_info.value)

    def test_verify_header_missing_timestamp(self):
        with pytest.raises(SignatureVerificationError) as exc_info:
            WebhookSignature.verify_header("payload", "sig", "", "secret")
        assert "Missing timestamp header" in str(exc_info.value)

    def test_verify_header_invalid_timestamp(self):
        with pytest.raises(SignatureVerificationError) as exc_info:
            WebhookSignature.verify_header("payload", "sig", "invalid", "secret")
        assert "Invalid timestamp header" in str(exc_info.value)

    def test_verify_header_old_timestamp(self):
        payload = "test payload"
        secret = "test_secret"
        old_timestamp = str(int(time.time()) - 400)  # 400 seconds ago
        signature = WebhookSignature._compute_signature(payload, secret, old_timestamp)

        with pytest.raises(SignatureVerificationError) as exc_info:
            WebhookSignature.verify_header(
                payload, signature, old_timestamp, secret, tolerance=300
            )
        assert "Timestamp outside the tolerance zone" in str(exc_info.value)

    def test_verify_header_no_tolerance(self):
        payload = "test payload"
        secret = "test_secret"
        old_timestamp = str(int(time.time()) - 400)  # 400 seconds ago
        signature = WebhookSignature._compute_signature(payload, secret, old_timestamp)

        # Should succeed when tolerance is None
        result = WebhookSignature.verify_header(
            payload, signature, old_timestamp, secret, tolerance=None
        )
        assert result is True

    def test_verify_header_invalid_signature(self):
        payload = "test payload"
        secret = "test_secret"
        timestamp = str(int(time.time()))

        with pytest.raises(SignatureVerificationError) as exc_info:
            WebhookSignature.verify_header(
                payload, "invalid_signature", timestamp, secret
            )
        assert "Signature verification failed" in str(exc_info.value)


class TestWebhook:
    """Test main Webhook utility class."""

    def _create_valid_webhook_data(self, secret="test_secret"):
        """Helper to create valid webhook data."""
        payload_dict = {
            "type": "video.completed",
            "payload": {
                "id": "test_id",
                "status": "complete",
                "downloads": [{"url": "https://example.com/video.mp4"}],
            },
        }
        payload = json.dumps(payload_dict, separators=(",", ":"))
        timestamp = str(int(time.time()))
        signature = WebhookSignature._compute_signature(payload, secret, timestamp)

        return payload, signature, timestamp

    def test_construct_event_success_string_payload(self):
        payload, signature, timestamp = self._create_valid_webhook_data()

        event = Webhook.construct_event(payload, signature, timestamp, "test_secret")

        assert isinstance(event, WebhookEvent)
        assert event.type == "video.completed"
        assert event.payload["id"] == "test_id"
        assert event.payload["status"] == "complete"

    def test_construct_event_success_bytes_payload(self):
        payload, signature, timestamp = self._create_valid_webhook_data()
        payload_bytes = payload.encode("utf-8")

        event = Webhook.construct_event(
            payload_bytes, signature, timestamp, "test_secret"
        )

        assert isinstance(event, WebhookEvent)
        assert event.type == "video.completed"

    def test_construct_event_invalid_signature(self):
        payload, _, timestamp = self._create_valid_webhook_data()

        with pytest.raises(SignatureVerificationError):
            Webhook.construct_event(payload, "invalid_sig", timestamp, "test_secret")

    def test_construct_event_invalid_json(self):
        invalid_payload = "not json"
        timestamp = str(int(time.time()))
        signature = WebhookSignature._compute_signature(
            invalid_payload, "secret", timestamp
        )

        with pytest.raises(ValueError) as exc_info:
            Webhook.construct_event(invalid_payload, signature, timestamp, "secret")
        assert "Invalid JSON payload" in str(exc_info.value)

    def test_construct_event_missing_type(self):
        payload_dict = {"payload": {"id": "test"}}  # Missing "type"
        payload = json.dumps(payload_dict)
        timestamp = str(int(time.time()))
        signature = WebhookSignature._compute_signature(payload, "secret", timestamp)

        with pytest.raises(ValueError) as exc_info:
            Webhook.construct_event(payload, signature, timestamp, "secret")
        assert "Missing 'type' field" in str(exc_info.value)

    def test_construct_event_empty_payload_field(self):
        payload_dict = {"type": "video.completed"}  # Missing "payload"
        payload = json.dumps(payload_dict)
        timestamp = str(int(time.time()))
        signature = WebhookSignature._compute_signature(payload, "secret", timestamp)

        event = Webhook.construct_event(payload, signature, timestamp, "secret")
        assert event.type == "video.completed"
        assert event.payload == {}

    def test_construct_event_custom_tolerance(self):
        payload, signature, timestamp = self._create_valid_webhook_data()

        # Should work with custom tolerance
        event = Webhook.construct_event(
            payload, signature, timestamp, "test_secret", tolerance=600
        )
        assert event.type == "video.completed"

    def test_default_tolerance(self):
        assert Webhook.DEFAULT_TOLERANCE == 300


class TestWebhookClient:
    """Test WebhookClient class."""

    def test_init_without_secret(self):
        client = WebhookClient()
        assert client.webhook_secret is None

    def test_init_with_secret(self):
        client = WebhookClient(webhook_secret="test_secret")
        assert client.webhook_secret == "test_secret"

    def test_construct_event_with_instance_secret(self):
        client = WebhookClient(webhook_secret="test_secret")
        payload, signature, timestamp = self._create_valid_webhook_data()

        event = client.construct_event(payload, signature, timestamp)
        assert event.type == "image.completed"

    def test_construct_event_with_parameter_secret(self):
        client = WebhookClient()  # No instance secret
        payload, signature, timestamp = self._create_valid_webhook_data()

        event = client.construct_event(
            payload, signature, timestamp, webhook_secret="test_secret"
        )
        assert event.type == "image.completed"

    def test_construct_event_parameter_overrides_instance(self):
        client = WebhookClient(webhook_secret="instance_secret")
        payload, signature, timestamp = self._create_valid_webhook_data("param_secret")

        event = client.construct_event(
            payload, signature, timestamp, webhook_secret="param_secret"
        )
        assert event.type == "image.completed"

    def test_construct_event_no_secret_provided(self):
        client = WebhookClient()  # No instance secret
        payload, signature, timestamp = self._create_valid_webhook_data()

        with pytest.raises(ValueError) as exc_info:
            client.construct_event(payload, signature, timestamp)
        assert "webhook_secret is required" in str(exc_info.value)

    def _create_valid_webhook_data(self, secret="test_secret"):
        """Helper to create valid webhook data."""
        payload_dict = {
            "type": "image.completed",
            "payload": {"id": "img_123", "status": "complete"},
        }
        payload = json.dumps(payload_dict, separators=(",", ":"))
        timestamp = str(int(time.time()))
        signature = WebhookSignature._compute_signature(payload, secret, timestamp)

        return payload, signature, timestamp

    def test_parse_event_with_content_attribute(self):
        client = WebhookClient(webhook_secret="test_secret")
        payload, signature, timestamp = self._create_valid_webhook_data()

        # Mock request with content attribute
        request = Mock(spec=httpx.Request)
        request.headers = {
            "magic-hour-event-signature": signature,
            "magic-hour-event-timestamp": timestamp,
        }
        request.content = payload.encode("utf-8")

        event = client.parse_event(request)
        assert event.type == "image.completed"
        assert event.payload["id"] == "img_123"

    def test_parse_event_with_read_method(self):
        client = WebhookClient(webhook_secret="test_secret")
        payload, signature, timestamp = self._create_valid_webhook_data()

        # Mock request with read method
        request = Mock()
        request.headers = {
            "magic-hour-event-signature": signature,
            "magic-hour-event-timestamp": timestamp,
        }
        request.read = Mock(return_value=payload.encode("utf-8"))
        # Remove content attribute to force using read method
        del request.content

        event = client.parse_event(request)
        assert event.type == "image.completed"

    def test_parse_event_missing_signature_header(self):
        client = WebhookClient(webhook_secret="test_secret")

        request = Mock(spec=httpx.Request)
        request.headers = {"magic-hour-event-timestamp": "123"}
        request.content = "payload"

        with pytest.raises(ValueError) as exc_info:
            client.parse_event(request)
        assert "Missing 'magic-hour-event-signature' header" in str(exc_info.value)

    def test_parse_event_missing_timestamp_header(self):
        client = WebhookClient(webhook_secret="test_secret")

        request = Mock(spec=httpx.Request)
        request.headers = {"magic-hour-event-signature": "sig"}
        request.content = "payload"

        with pytest.raises(ValueError) as exc_info:
            client.parse_event(request)
        assert "Missing 'magic-hour-event-timestamp' header" in str(exc_info.value)

    def test_parse_event_no_payload_method(self):
        client = WebhookClient(webhook_secret="test_secret")

        request = Mock()
        request.headers = {
            "magic-hour-event-signature": "sig",
            "magic-hour-event-timestamp": str(int(time.time())),  # Use current time
        }
        # Remove both content and read to trigger the error we want to test
        if hasattr(request, "content"):
            del request.content
        if hasattr(request, "read"):
            del request.read

        with pytest.raises(ValueError) as exc_info:
            client.parse_event(request)
        assert "Unable to extract payload from request object" in str(exc_info.value)

    def test_parse_event_no_secret(self):
        client = WebhookClient()  # No secret

        request = Mock(spec=httpx.Request)
        request.headers = {
            "magic-hour-event-signature": "sig",
            "magic-hour-event-timestamp": "123",
        }
        request.content = "payload"

        with pytest.raises(ValueError) as exc_info:
            client.parse_event(request)
        assert "webhook_secret is required" in str(exc_info.value)

    def test_parse_event_with_parameter_secret(self):
        client = WebhookClient()  # No instance secret
        payload, signature, timestamp = self._create_valid_webhook_data()

        request = Mock(spec=httpx.Request)
        request.headers = {
            "magic-hour-event-signature": signature,
            "magic-hour-event-timestamp": timestamp,
        }
        request.content = payload.encode("utf-8")

        event = client.parse_event(request, webhook_secret="test_secret")
        assert event.type == "image.completed"

    def test_parse_event_custom_tolerance(self):
        client = WebhookClient(webhook_secret="test_secret")
        payload, signature, timestamp = self._create_valid_webhook_data()

        request = Mock(spec=httpx.Request)
        request.headers = {
            "magic-hour-event-signature": signature,
            "magic-hour-event-timestamp": timestamp,
        }
        request.content = payload.encode("utf-8")

        event = client.parse_event(request, tolerance=600)
        assert event.type == "image.completed"


class TestIntegration:
    """Integration tests for the webhook system."""

    def test_full_webhook_flow(self):
        """Test the complete webhook verification flow."""
        # Setup
        secret = "whsec_test_secret_123"
        webhook_client = WebhookClient(webhook_secret=secret)

        # Create webhook payload like Magic Hour would
        webhook_payload = {
            "type": "audio.completed",
            "payload": {
                "id": "audio_proj_123",
                "name": "Voice Generation",
                "status": "complete",
                "type": "VOICE_GENERATOR",
                "created_at": "2023-11-07T05:31:56Z",
                "enabled": True,
                "credits_charged": 2,
                "downloads": [
                    {
                        "url": "https://audio.magichour.ai/id/output.wav",
                        "expires_at": "2024-10-19T05:16:19.027Z",
                    }
                ],
                "error": None,
            },
        }

        payload_str = json.dumps(webhook_payload, separators=(",", ":"))
        timestamp = str(int(time.time()))

        # Create signature like Magic Hour would
        signed_payload = f"{timestamp}.{payload_str}"
        signature = hmac.new(
            secret.encode("utf-8"), signed_payload.encode("utf-8"), sha256
        ).hexdigest()

        # Test direct Webhook.construct_event
        event = Webhook.construct_event(payload_str, signature, timestamp, secret)
        assert event.type == "audio.completed"
        assert event.payload["id"] == "audio_proj_123"
        assert event.payload["credits_charged"] == 2
        assert len(event.payload["downloads"]) == 1

        # Test WebhookClient.construct_event
        event2 = webhook_client.construct_event(payload_str, signature, timestamp)
        assert event2.type == event.type
        assert event2.payload == event.payload

        # Test WebhookClient.parse_event with mock request
        request = Mock(spec=httpx.Request)
        request.headers = {
            "magic-hour-event-signature": signature,
            "magic-hour-event-timestamp": timestamp,
        }
        request.content = payload_str.encode("utf-8")

        event3 = webhook_client.parse_event(request)
        assert event3.type == event.type
        assert event3.payload == event.payload

    def test_different_event_types(self):
        """Test webhook verification works for different event types."""
        secret = "test_secret"

        event_types = [
            "video.started",
            "video.completed",
            "video.errored",
            "image.started",
            "image.completed",
            "image.errored",
            "audio.started",
            "audio.completed",
            "audio.errored",
        ]

        for event_type in event_types:
            payload_dict = {
                "type": event_type,
                "payload": {
                    "id": f"proj_{event_type.replace('.', '_')}",
                    "status": "complete" if "completed" in event_type else "processing",
                },
            }

            payload = json.dumps(payload_dict, separators=(",", ":"))
            timestamp = str(int(time.time()))
            signature = WebhookSignature._compute_signature(payload, secret, timestamp)

            event = Webhook.construct_event(payload, signature, timestamp, secret)
            assert event.type == event_type
            assert event.payload["id"] == f"proj_{event_type.replace('.', '_')}"

    def test_malicious_payload_attempts(self):
        """Test that malicious or malformed payloads are rejected."""
        secret = "test_secret"

        # Test cases for malicious payloads
        malicious_cases = [
            # Payload tampering
            (
                '{"type":"video.completed","payload":{"id":"hacked"}}',
                "original_signature",
            ),
            # Wrong secret
            (
                '{"type":"video.completed","payload":{"id":"test"}}',
                "wrong_secret_signature",
            ),
            # Timestamp manipulation (old timestamp)
            ('{"type":"video.completed","payload":{"id":"test"}}', "old_timestamp"),
        ]

        for payload, case_type in malicious_cases:
            timestamp = str(int(time.time()))

            if case_type == "original_signature":
                # Create signature for different payload
                original_payload = (
                    '{"type":"video.started","payload":{"id":"original"}}'
                )
                signature = WebhookSignature._compute_signature(
                    original_payload, secret, timestamp
                )
            elif case_type == "wrong_secret_signature":
                signature = WebhookSignature._compute_signature(
                    payload, "wrong_secret", timestamp
                )
            elif case_type == "old_timestamp":
                old_timestamp = str(int(time.time()) - 400)
                signature = WebhookSignature._compute_signature(
                    payload, secret, old_timestamp
                )
                timestamp = old_timestamp

            with pytest.raises(SignatureVerificationError):
                Webhook.construct_event(payload, signature, timestamp, secret)


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])
