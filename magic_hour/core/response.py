import json
from typing import Any, Union, Dict, Type, TypeVar, List, Generic, Optional
from pydantic import BaseModel
import httpx

"""
Provides functionality for handling Server-Sent Events (SSE) streams and response data encoding.
Includes utilities for both synchronous and asynchronous stream processing.
"""

EncodableT = TypeVar(
    "EncodableT",
    bound=Union[
        object,
        str,
        int,
        float,
        None,
        BaseModel,
        List[Any],
        Dict[str, Any],
    ],
)


def from_encodable(*, data: Any, load_with: Type[EncodableT]) -> Any:
    """
    Converts raw data into a specified type using Pydantic validation.

    Uses a dynamic Pydantic model to validate and convert incoming data
    into the specified target type.
    """

    class Caster(BaseModel):
        data: load_with  # type: ignore

    return Caster(data=data).data


T = TypeVar("T")


class StreamResponse(Generic[T]):
    """
    Handles synchronous streaming of Server-Sent Events (SSE).

    Processes a streaming HTTP response by buffering chunks of data
    and parsing them according to SSE format, converting each event
    into the specified type.
    """

    def __init__(self, response: httpx.Response, stream_context, cast_to: Type[T]):
        """
        Initialize the stream processor with response and conversion settings.

        Args:
            response: The HTTP response containing the SSE stream
            stream_context: Context manager for the stream
            cast_to: Target type for converting parsed events
        """
        self.response = response
        self._context = stream_context
        self.cast_to = cast_to
        self.iterator = response.iter_bytes()
        self.buffer = bytearray()
        self.position = 0

    def __iter__(self):
        """Enables iteration over the stream events."""
        return self

    def __next__(self) -> T:
        """
        Retrieves and processes the next event from the stream.

        Buffers incoming data and processes it according to SSE format,
        converting each complete event into the specified type.

        Raises:
            StopIteration: When the stream is exhausted
        """
        try:
            while True:
                event = self._process_buffer()
                if event:
                    return event

                chunk = next(self.iterator)
                self.buffer += chunk

        except StopIteration:
            event = self._process_buffer(final=True)
            if event:
                return event
            self._context.__exit__(None, None, None)
            raise

    def _process_buffer(self, final=False) -> Optional[T]:
        """
        Processes the current buffer to extract complete SSE events.

        Searches for event boundaries and parses complete events,
        handling both JSON and non-JSON payloads.

        Args:
            final: Whether this is the final processing of the buffer
        """
        while self.position < len(self.buffer):
            for boundary in [b"\r\n\r\n", b"\n\n", b"\r\r"]:
                if (self.position + len(boundary)) <= len(self.buffer):
                    if (
                        self.buffer[self.position : self.position + len(boundary)]
                        == boundary
                    ):
                        message = self.buffer[: self.position].decode()
                        self.buffer = self.buffer[self.position + len(boundary) :]
                        self.position = 0

                        data = self._parse_sse(message)
                        if data:
                            try:
                                parsed_data = json.loads(data)
                                if (
                                    not isinstance(parsed_data, dict)
                                    or "data" not in parsed_data
                                ):
                                    parsed_data = {"data": parsed_data}
                                return from_encodable(
                                    data=parsed_data, load_with=self.cast_to
                                )
                            except json.JSONDecodeError:
                                return from_encodable(
                                    data={"data": data}, load_with=self.cast_to
                                )
                        return None

            self.position += 1

        if final and self.buffer:
            message = self.buffer.decode()
            data = self._parse_sse(message)
            if data:
                try:
                    parsed_data = json.loads(data)
                    if not isinstance(parsed_data, dict) or "data" not in parsed_data:
                        parsed_data = {"data": parsed_data}
                    return from_encodable(data=parsed_data, load_with=self.cast_to)
                except json.JSONDecodeError:
                    return from_encodable(data={"data": data}, load_with=self.cast_to)

        return None

    def _parse_sse(self, message: str) -> Optional[str]:
        """
        Parses an SSE message to extract the data field.

        Handles multi-line data fields and empty data fields according
        to the SSE specification.
        """
        data = []
        for line in message.split("\n"):
            if line.startswith("data:"):
                data.append(line[5:].strip())
            elif line.strip() == "data:":  # Handle empty data field
                data.append("")

        if data:
            return "\n".join(data)
        return None


class AsyncStreamResponse(Generic[T]):
    """
    Handles asynchronous streaming of Server-Sent Events (SSE).

    Asynchronous version of StreamResponse, providing the same functionality
    but compatible with async/await syntax.
    """

    def __init__(self, response: httpx.Response, stream_context, cast_to: Type[T]):
        """
        Initialize the async stream processor.

        Args:
            response: The HTTP response containing the SSE stream
            stream_context: Async context manager for the stream
            cast_to: Target type for converting parsed events
        """
        self.response = response
        self._context = stream_context
        self.cast_to = cast_to
        self.iterator = response.aiter_bytes()
        self.buffer = bytearray()
        self.position = 0

    def __aiter__(self):
        """Enables async iteration over the stream events."""
        return self

    async def __anext__(self) -> T:
        """
        Asynchronously retrieves and processes the next event from the stream.

        Similar to synchronous version but uses async/await syntax for
        iteration and context management.

        Raises:
            StopAsyncIteration: When the stream is exhausted
        """
        try:
            while True:
                event = self._process_buffer()
                if event:
                    return event

                chunk = await self.iterator.__anext__()
                self.buffer += chunk

        except StopAsyncIteration:
            event = self._process_buffer(final=True)
            if event:
                return event
            await self._context.__aexit__(None, None, None)
            raise

    def _process_buffer(self, final=False) -> Optional[T]:
        """
        Processes the current buffer to extract complete SSE events.

        Identical to the synchronous version's buffer processing.
        """
        while self.position < len(self.buffer):
            for boundary in [b"\r\n\r\n", b"\n\n", b"\r\r"]:
                if (self.position + len(boundary)) <= len(self.buffer):
                    if (
                        self.buffer[self.position : self.position + len(boundary)]
                        == boundary
                    ):
                        message = self.buffer[: self.position].decode()
                        self.buffer = self.buffer[self.position + len(boundary) :]
                        self.position = 0

                        data = self._parse_sse(message)
                        if data:
                            try:
                                parsed_data = json.loads(data)
                                if (
                                    not isinstance(parsed_data, dict)
                                    or "data" not in parsed_data
                                ):
                                    parsed_data = {"data": parsed_data}
                                return from_encodable(
                                    data=parsed_data, load_with=self.cast_to
                                )
                            except json.JSONDecodeError:
                                return from_encodable(
                                    data={"data": data}, load_with=self.cast_to
                                )
                        return None

            self.position += 1

        if final and self.buffer:
            message = self.buffer.decode()
            data = self._parse_sse(message)
            if data:
                try:
                    parsed_data = json.loads(data)
                    if not isinstance(parsed_data, dict) or "data" not in parsed_data:
                        parsed_data = {"data": parsed_data}
                    return from_encodable(data=parsed_data, load_with=self.cast_to)
                except json.JSONDecodeError:
                    return from_encodable(data={"data": data}, load_with=self.cast_to)

        return None

    def _parse_sse(self, message: str) -> Optional[str]:
        """
        Parses an SSE message to extract the data field.

        Identical to the synchronous version's SSE parsing.
        """
        data = []
        for line in message.split("\n"):
            line = line.strip()
            if line.startswith("data:"):
                data.append(line[5:].strip())
            elif line == "data:":  # Handle empty data field
                data.append("")

        if data:
            return "\n".join(data)
        return None
