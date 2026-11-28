import typing
import typing_extensions

from magic_hour.types import models
from make_api_request import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)


class AudioClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        tool: typing_extensions.Literal[
            "ai-music-generator", "ai-voice-cloner", "ai-voice-generator"
        ],
        character_count: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        duration: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1EstimateAudioListResponse:
        """
        Estimate audio credits

        Get the credits an audio create request charges. Pass `tool`, then the field below that the tool's create request uses. Does not create a project or spend credits. It prices the fields passed here. It does not check your plan, your balance or the rest of the create request.

        GET /v1/estimate/audio

        Args:
            character_count: The number of characters in the `style.prompt` of the create request. Used by `ai-voice-generator`, `ai-voice-cloner`.
            duration: The `duration` of the create request. Used by `ai-music-generator`.
            tool: The create endpoint to price, named by its path. For example `ai-voice-generator` for `POST /v1/ai-voice-generator`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.estimate.audio.list(tool="ai-voice-generator", character_count=120)
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "tool",
            to_encodable(
                item=tool,
                dump_with=typing_extensions.Literal[
                    "ai-music-generator", "ai-voice-cloner", "ai-voice-generator"
                ],
            ),
            style="form",
            explode=True,
        )
        if not isinstance(character_count, type_utils.NotGiven):
            encode_query_param(
                _query,
                "character_count",
                to_encodable(item=character_count, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(duration, type_utils.NotGiven):
            encode_query_param(
                _query,
                "duration",
                to_encodable(item=duration, dump_with=int),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/estimate/audio",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.V1EstimateAudioListResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAudioClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        tool: typing_extensions.Literal[
            "ai-music-generator", "ai-voice-cloner", "ai-voice-generator"
        ],
        character_count: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        duration: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1EstimateAudioListResponse:
        """
        Estimate audio credits

        Get the credits an audio create request charges. Pass `tool`, then the field below that the tool's create request uses. Does not create a project or spend credits. It prices the fields passed here. It does not check your plan, your balance or the rest of the create request.

        GET /v1/estimate/audio

        Args:
            character_count: The number of characters in the `style.prompt` of the create request. Used by `ai-voice-generator`, `ai-voice-cloner`.
            duration: The `duration` of the create request. Used by `ai-music-generator`.
            tool: The create endpoint to price, named by its path. For example `ai-voice-generator` for `POST /v1/ai-voice-generator`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.estimate.audio.list(
            tool="ai-voice-generator", character_count=120
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "tool",
            to_encodable(
                item=tool,
                dump_with=typing_extensions.Literal[
                    "ai-music-generator", "ai-voice-cloner", "ai-voice-generator"
                ],
            ),
            style="form",
            explode=True,
        )
        if not isinstance(character_count, type_utils.NotGiven):
            encode_query_param(
                _query,
                "character_count",
                to_encodable(item=character_count, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(duration, type_utils.NotGiven):
            encode_query_param(
                _query,
                "duration",
                to_encodable(item=duration, dump_with=int),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/estimate/audio",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.V1EstimateAudioListResponse,
            request_options=request_options or default_request_options(),
        )
