import hmac
import json
import time
import typing
from collections import OrderedDict
from hashlib import sha256

import httpx


class SignatureVerificationError(Exception):
    """
    Exception raised when webhook signature verification fails.

    This error is raised when:
    - The signature header is missing or malformed
    - The computed signature doesn't match the provided signature
    - The timestamp is outside the tolerance window
    """

    def __init__(
        self,
        message: str,
        sig_header: typing.Optional[str] = None,
        payload: typing.Optional[str] = None,
    ):
        super().__init__(message)
        self.sig_header = sig_header
        self.payload = payload


class WebhookEvent:
    """
    Represents a Magic Hour webhook event.

    This class contains the parsed webhook event data including the event type
    and payload information.
    """

    def __init__(self, event_type: str, payload: typing.Dict[str, typing.Any]):
        self.type = event_type
        self.payload = payload

    def __repr__(self) -> str:
        return f"WebhookEvent(type='{self.type}', payload_id='{self.payload.get('id', 'unknown')}')"


class WebhookSignature:
    """
    Utility class for verifying Magic Hour webhook signatures.

    Magic Hour signs webhooks using HMAC-SHA256 with your webhook secret.
    The signature is provided in the 'magic-hour-event-signature' header,
    and the timestamp is provided in the 'magic-hour-event-timestamp' header.
    """

    @staticmethod
    def _compute_signature(payload: str, secret: str, timestamp: str) -> str:
        """
        Compute the HMAC-SHA256 signature for the given payload and secret.

        Args:
            payload: The raw webhook payload as a string
            secret: The webhook secret from Magic Hour Developer Hub
            timestamp: The timestamp from the magic-hour-event-timestamp header

        Returns:
            The computed signature as a hexadecimal string
        """
        signed_payload = f"{timestamp}.{payload}"
        mac = hmac.new(
            secret.encode("utf-8"),
            msg=signed_payload.encode("utf-8"),
            digestmod=sha256,
        )
        return mac.hexdigest()

    @staticmethod
    def _secure_compare(a: str, b: str) -> bool:
        """
        Securely compare two strings to prevent timing attacks.

        Args:
            a: First string to compare
            b: Second string to compare

        Returns:
            True if strings are equal, False otherwise
        """
        if len(a) != len(b):
            return False

        result = 0
        for x, y in zip(a, b):
            result |= ord(x) ^ ord(y)
        return result == 0

    @classmethod
    def verify_header(
        cls,
        payload: str,
        sig_header: str,
        timestamp_header: str,
        secret: str,
        tolerance: typing.Optional[int] = 300,
    ) -> bool:
        """
        Verify the webhook signature and timestamp.

        Args:
            payload: The raw webhook payload as received
            sig_header: The value of the 'magic-hour-event-signature' header
            timestamp_header: The value of the 'magic-hour-event-timestamp' header
            secret: Your webhook secret from Magic Hour Developer Hub
            tolerance: Maximum age of the webhook in seconds (default: 300/5 minutes)

        Returns:
            True if verification succeeds

        Raises:
            SignatureVerificationError: If verification fails
        """
        if not sig_header:
            raise SignatureVerificationError(
                "Missing signature header 'magic-hour-event-signature'",
                sig_header,
                payload,
            )

        if not timestamp_header:
            raise SignatureVerificationError(
                "Missing timestamp header 'magic-hour-event-timestamp'",
                sig_header,
                payload,
            )

        try:
            timestamp = int(timestamp_header)
        except (ValueError, TypeError):
            raise SignatureVerificationError(
                f"Invalid timestamp header: {timestamp_header}", sig_header, payload
            )

        # Verify timestamp tolerance
        if tolerance and timestamp < time.time() - tolerance:
            raise SignatureVerificationError(
                f"Timestamp outside the tolerance zone. Timestamp: {timestamp}, Current time: {int(time.time())}, Tolerance: {tolerance}s",
                sig_header,
                payload,
            )

        # Compute expected signature
        expected_sig = cls._compute_signature(payload, secret, timestamp_header)

        # Compare signatures
        if not cls._secure_compare(expected_sig, sig_header):
            raise SignatureVerificationError(
                "Signature verification failed. The provided signature does not match the expected signature for the payload",
                sig_header,
                payload,
            )

        return True


class Webhook:
    """
    Main webhook utility class for Magic Hour webhooks.

    This class provides methods to construct and verify webhook events
    received from Magic Hour's webhook system.
    """

    DEFAULT_TOLERANCE = 300  # 5 minutes

    @staticmethod
    def construct_event(
        payload: typing.Union[str, bytes],
        sig_header: str,
        timestamp_header: str,
        secret: str,
        tolerance: typing.Optional[int] = DEFAULT_TOLERANCE,
    ) -> WebhookEvent:
        """
        Construct a verified webhook event from the request data.

        This method verifies the webhook signature and constructs a WebhookEvent
        object from the payload data.

        Args:
            payload: The raw webhook payload (string or bytes)
            sig_header: The 'magic-hour-event-signature' header value
            timestamp_header: The 'magic-hour-event-timestamp' header value
            secret: Your webhook secret from Magic Hour Developer Hub
            tolerance: Maximum age of the webhook in seconds (default: 300)

        Returns:
            A WebhookEvent object containing the parsed event data

        Raises:
            SignatureVerificationError: If signature verification fails
            ValueError: If the payload is not valid JSON

        Examples:
            ```python
            from magic_hour.resources.v1.webhook import Webhook

            # In your webhook handler (e.g., Flask, FastAPI)
            def handle_webhook(request):
                payload = request.get_data(as_text=True)
                sig_header = request.headers.get('magic-hour-event-signature')
                timestamp_header = request.headers.get('magic-hour-event-timestamp')
                secret = 'whsec_your_webhook_secret'

                try:
                    event = Webhook.construct_event(
                        payload, sig_header, timestamp_header, secret
                    )

                    if event.type == 'video.completed':
                        print(f"Video {event.payload['id']} completed!")
                        # Handle video completion
                    elif event.type == 'image.completed':
                        print(f"Image {event.payload['id']} completed!")
                        # Handle image completion

                except SignatureVerificationError as e:
                    print(f"Webhook signature verification failed: {e}")
                    return "Invalid signature", 400

                return "OK", 200
            ```
        """
        # Convert bytes to string if necessary
        payload_str: str
        if isinstance(payload, bytes):
            payload_str = payload.decode("utf-8")
        else:
            payload_str = str(payload)

        # Verify the signature
        WebhookSignature.verify_header(
            payload_str, sig_header, timestamp_header, secret, tolerance
        )

        # Parse the JSON payload
        try:
            data = json.loads(payload_str, object_pairs_hook=OrderedDict)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON payload: {e}")

        # Extract event type and payload
        event_type = data.get("type")
        if not event_type:
            raise ValueError("Missing 'type' field in webhook payload")

        event_payload = data.get("payload", {})

        return WebhookEvent(event_type=event_type, payload=event_payload)


class WebhookClient:
    """
    Client for handling Magic Hour webhook events.

    This client provides methods to parse and verify webhook events
    from Magic Hour's webhook system.
    """

    def __init__(self, webhook_secret: typing.Optional[str] = None):
        """
        Initialize the webhook client.

        Args:
            webhook_secret: Your webhook secret from Magic Hour Developer Hub.
                          If not provided, it must be passed to individual methods.
        """
        self.webhook_secret = webhook_secret

    def parse_event(
        self,
        request: httpx.Request,
        webhook_secret: typing.Optional[str] = None,
        tolerance: typing.Optional[int] = Webhook.DEFAULT_TOLERANCE,
    ) -> WebhookEvent:
        """
        Parse and verify a webhook event from an httpx.Request object.

        Args:
            request: The httpx.Request object containing the webhook data
            webhook_secret: Webhook secret (uses instance secret if not provided)
            tolerance: Maximum age of the webhook in seconds (default: 300)

        Returns:
            A verified WebhookEvent object

        Raises:
            SignatureVerificationError: If signature verification fails
            ValueError: If required headers or secret are missing

        Examples:
            ```python
            from magic_hour.resources.v1.webhook import WebhookClient
            import httpx

            # Initialize client with secret
            webhook_client = WebhookClient(webhook_secret='whsec_your_secret')

            # In your webhook handler
            def handle_webhook(request: httpx.Request):
                try:
                    event = webhook_client.parse_event(request)
                    print(f"Received {event.type} event for {event.payload.get('id')}")
                    return {"status": "success"}
                except Exception as e:
                    print(f"Error processing webhook: {e}")
                    return {"error": str(e)}, 400
            ```
        """
        # Use provided secret or instance secret
        secret = webhook_secret or self.webhook_secret
        if not secret:
            raise ValueError(
                "webhook_secret is required. Provide it during initialization or as a parameter."
            )

        # Extract headers
        sig_header = request.headers.get("magic-hour-event-signature")
        timestamp_header = request.headers.get("magic-hour-event-timestamp")

        if not sig_header:
            raise ValueError("Missing 'magic-hour-event-signature' header")
        if not timestamp_header:
            raise ValueError("Missing 'magic-hour-event-timestamp' header")

        # Get the payload
        payload = None

gcam wi

        # If content didn't work, try read method
        if payload is None and hasattr(request, "read"):
            try:
                content = request.read()
                payload = (
                    content.decode("utf-8")
                    if isinstance(content, bytes)
                    else str(content)
                )
            except (AttributeError, TypeError):
                pass

        if payload is None:
            raise ValueError(
                "Unable to extract payload from request object. Request must have 'content' attribute or 'read()' method."
            )

        # Construct and return the event
        return Webhook.construct_event(
            payload=payload,
            sig_header=sig_header,
            timestamp_header=timestamp_header,
            secret=secret,
            tolerance=tolerance,
        )

    def construct_event(
        self,
        payload: typing.Union[str, bytes],
        sig_header: str,
        timestamp_header: str,
        webhook_secret: typing.Optional[str] = None,
        tolerance: typing.Optional[int] = Webhook.DEFAULT_TOLERANCE,
    ) -> WebhookEvent:
        """
        Construct a verified webhook event from raw data.

        This is a convenience method that delegates to Webhook.construct_event
        but can use the instance's webhook_secret if not provided.

        Args:
            payload: The raw webhook payload
            sig_header: The 'magic-hour-event-signature' header value
            timestamp_header: The 'magic-hour-event-timestamp' header value
            webhook_secret: Webhook secret (uses instance secret if not provided)
            tolerance: Maximum age of the webhook in seconds (default: 300)

        Returns:
            A verified WebhookEvent object

        Raises:
            SignatureVerificationError: If signature verification fails
            ValueError: If required secret is missing
        """
        # Use provided secret or instance secret
        secret = webhook_secret or self.webhook_secret
        if not secret:
            raise ValueError(
                "webhook_secret is required. Provide it during initialization or as a parameter."
            )

        return Webhook.construct_event(
            payload=payload,
            sig_header=sig_header,
            timestamp_header=timestamp_header,
            secret=secret,
            tolerance=tolerance,
        )
