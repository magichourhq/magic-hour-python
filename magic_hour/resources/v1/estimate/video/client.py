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


class VideoClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        end_seconds: float,
        tool: typing_extensions.Literal[
            "ai-ugc-ad",
            "ai-video-editor",
            "ai-video-translator",
            "ai-video-upscaler",
            "audio-to-video",
            "auto-subtitle-generator",
            "character-replace",
            "face-swap",
            "image-to-video",
            "text-to-video",
        ],
        audio: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        has_video_reference: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        start_seconds: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1EstimateVideoListResponse:
        """
        Estimate video credits

        Get the credits a video create request charges when it is submitted. Pass `tool`, then the fields below that the tool's create request uses, with the same values. Tools billed per frame charge an estimate at submission, assuming 30 fps for an uploaded video, and settle to the frames that render. Does not create a project or spend credits. It prices the fields passed here. It does not check your plan, your balance or the rest of the create request.

        GET /v1/estimate/video

        Args:
            audio: The `audio` of the create request. Used by `image-to-video`, `text-to-video`. Defaults to `false`.
            has_video_reference: Whether any of the create request's `references` is a video. Used by `text-to-video`. Defaults to `false`.
            model: The `model` of the create request. Used by `image-to-video`, `text-to-video`, `ai-ugc-ad`, `ai-video-editor`, `character-replace`.
            resolution: The `resolution` of the create request. Used by `image-to-video`, `text-to-video`, `ai-ugc-ad`, `ai-video-editor`, `character-replace`, `audio-to-video`, `ai-video-translator`, `ai-video-upscaler`. `ai-video-translator` defaults to `480p`.
            start_seconds: The `start_seconds` of the create request, for tools whose create request has it. Defaults to 0.
            end_seconds: The `end_seconds` of the create request. Used by every tool.
            tool: The create endpoint to price, named by its path. For example `image-to-video` for `POST /v1/image-to-video`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.estimate.video.list(
            end_seconds=5.0, tool="image-to-video", model="kling-3.0", resolution="720p"
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "end_seconds",
            to_encodable(item=end_seconds, dump_with=float),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "tool",
            to_encodable(
                item=tool,
                dump_with=typing_extensions.Literal[
                    "ai-ugc-ad",
                    "ai-video-editor",
                    "ai-video-translator",
                    "ai-video-upscaler",
                    "audio-to-video",
                    "auto-subtitle-generator",
                    "character-replace",
                    "face-swap",
                    "image-to-video",
                    "text-to-video",
                ],
            ),
            style="form",
            explode=True,
        )
        if not isinstance(audio, type_utils.NotGiven):
            encode_query_param(
                _query,
                "audio",
                to_encodable(item=audio, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(has_video_reference, type_utils.NotGiven):
            encode_query_param(
                _query,
                "has_video_reference",
                to_encodable(item=has_video_reference, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(model, type_utils.NotGiven):
            encode_query_param(
                _query,
                "model",
                to_encodable(item=model, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(resolution, type_utils.NotGiven):
            encode_query_param(
                _query,
                "resolution",
                to_encodable(item=resolution, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(start_seconds, type_utils.NotGiven):
            encode_query_param(
                _query,
                "start_seconds",
                to_encodable(item=start_seconds, dump_with=float),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/estimate/video",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.V1EstimateVideoListResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncVideoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        end_seconds: float,
        tool: typing_extensions.Literal[
            "ai-ugc-ad",
            "ai-video-editor",
            "ai-video-translator",
            "ai-video-upscaler",
            "audio-to-video",
            "auto-subtitle-generator",
            "character-replace",
            "face-swap",
            "image-to-video",
            "text-to-video",
        ],
        audio: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        has_video_reference: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        start_seconds: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1EstimateVideoListResponse:
        """
        Estimate video credits

        Get the credits a video create request charges when it is submitted. Pass `tool`, then the fields below that the tool's create request uses, with the same values. Tools billed per frame charge an estimate at submission, assuming 30 fps for an uploaded video, and settle to the frames that render. Does not create a project or spend credits. It prices the fields passed here. It does not check your plan, your balance or the rest of the create request.

        GET /v1/estimate/video

        Args:
            audio: The `audio` of the create request. Used by `image-to-video`, `text-to-video`. Defaults to `false`.
            has_video_reference: Whether any of the create request's `references` is a video. Used by `text-to-video`. Defaults to `false`.
            model: The `model` of the create request. Used by `image-to-video`, `text-to-video`, `ai-ugc-ad`, `ai-video-editor`, `character-replace`.
            resolution: The `resolution` of the create request. Used by `image-to-video`, `text-to-video`, `ai-ugc-ad`, `ai-video-editor`, `character-replace`, `audio-to-video`, `ai-video-translator`, `ai-video-upscaler`. `ai-video-translator` defaults to `480p`.
            start_seconds: The `start_seconds` of the create request, for tools whose create request has it. Defaults to 0.
            end_seconds: The `end_seconds` of the create request. Used by every tool.
            tool: The create endpoint to price, named by its path. For example `image-to-video` for `POST /v1/image-to-video`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.estimate.video.list(
            end_seconds=5.0, tool="image-to-video", model="kling-3.0", resolution="720p"
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "end_seconds",
            to_encodable(item=end_seconds, dump_with=float),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "tool",
            to_encodable(
                item=tool,
                dump_with=typing_extensions.Literal[
                    "ai-ugc-ad",
                    "ai-video-editor",
                    "ai-video-translator",
                    "ai-video-upscaler",
                    "audio-to-video",
                    "auto-subtitle-generator",
                    "character-replace",
                    "face-swap",
                    "image-to-video",
                    "text-to-video",
                ],
            ),
            style="form",
            explode=True,
        )
        if not isinstance(audio, type_utils.NotGiven):
            encode_query_param(
                _query,
                "audio",
                to_encodable(item=audio, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(has_video_reference, type_utils.NotGiven):
            encode_query_param(
                _query,
                "has_video_reference",
                to_encodable(item=has_video_reference, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(model, type_utils.NotGiven):
            encode_query_param(
                _query,
                "model",
                to_encodable(item=model, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(resolution, type_utils.NotGiven):
            encode_query_param(
                _query,
                "resolution",
                to_encodable(item=resolution, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(start_seconds, type_utils.NotGiven):
            encode_query_param(
                _query,
                "start_seconds",
                to_encodable(item=start_seconds, dump_with=float),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/estimate/video",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.V1EstimateVideoListResponse,
            request_options=request_options or default_request_options(),
        )
