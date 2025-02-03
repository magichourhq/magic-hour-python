from httpx._models import Headers


class BinaryResponse:
    """
    Represents a binary HTTP response.

    A lightweight wrapper for binary content and its associated HTTP headers,
    typically used for handling file downloads or raw binary data from HTTP requests.
    """

    content: bytes
    headers: Headers

    def __init__(self, content: bytes, headers: Headers) -> None:
        """
        Initialize a binary response with content and headers.

        The content represents the raw binary data received in the response,
        while headers contain the associated HTTP response headers.
        """
        self.content = content
        self.headers = headers
