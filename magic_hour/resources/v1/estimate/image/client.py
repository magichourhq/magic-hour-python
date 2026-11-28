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


class ImageClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        tool: typing_extensions.Literal[
            "ai-clothes-changer",
            "ai-face-editor",
            "ai-gif-generator",
            "ai-headshot-generator",
            "ai-image-editor",
            "ai-image-generator",
            "ai-image-upscaler",
            "ai-meme-generator",
            "ai-qr-code-generator",
            "body-swap",
            "face-swap-photo",
            "head-swap",
            "image-background-remover",
            "photo-colorizer",
        ],
        image_count: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mode: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        scale_factor: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1EstimateImageListResponse:
        """
        Estimate image credits

        Get the credits an image create request charges. Pass `tool`, then the fields below that the tool's create request uses, with the same values. Does not create a project or spend credits. It prices the fields passed here. It does not check your plan, your balance or the rest of the create request.

        GET /v1/estimate/image

        Args:
            image_count: The `image_count` of the create request. Used by `ai-image-generator`, `ai-image-editor`. Defaults to 1.
            mode: The `style.mode` of the create request. Used by `ai-image-upscaler`. One of `preserve`, `balanced`, `creative`. Defaults to `balanced`.
            model: The `model` of the create request. Used by `ai-image-generator`, `ai-image-editor`.
            resolution: The `resolution` of the create request. Used by `ai-image-generator`, `ai-image-editor`, `body-swap`. One of `640px`, `1k`, `2k`, `4k`.
            scale_factor: The `scale_factor` of the create request. Used by `ai-image-upscaler`. One of `2`, `4`.
            tool: The create endpoint to price, named by its path. For example `ai-image-editor` for `POST /v1/ai-image-editor`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.estimate.image.list(
            tool="ai-image-editor",
            image_count=4,
            model="nano-banana-2.1",
            resolution="2k",
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
                    "ai-clothes-changer",
                    "ai-face-editor",
                    "ai-gif-generator",
                    "ai-headshot-generator",
                    "ai-image-editor",
                    "ai-image-generator",
                    "ai-image-upscaler",
                    "ai-meme-generator",
                    "ai-qr-code-generator",
                    "body-swap",
                    "face-swap-photo",
                    "head-swap",
                    "image-background-remover",
                    "photo-colorizer",
                ],
            ),
            style="form",
            explode=True,
        )
        if not isinstance(image_count, type_utils.NotGiven):
            encode_query_param(
                _query,
                "image_count",
                to_encodable(item=image_count, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(mode, type_utils.NotGiven):
            encode_query_param(
                _query,
                "mode",
                to_encodable(item=mode, dump_with=str),
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
        if not isinstance(scale_factor, type_utils.NotGiven):
            encode_query_param(
                _query,
                "scale_factor",
                to_encodable(item=scale_factor, dump_with=float),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/estimate/image",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.V1EstimateImageListResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncImageClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        tool: typing_extensions.Literal[
            "ai-clothes-changer",
            "ai-face-editor",
            "ai-gif-generator",
            "ai-headshot-generator",
            "ai-image-editor",
            "ai-image-generator",
            "ai-image-upscaler",
            "ai-meme-generator",
            "ai-qr-code-generator",
            "body-swap",
            "face-swap-photo",
            "head-swap",
            "image-background-remover",
            "photo-colorizer",
        ],
        image_count: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mode: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        scale_factor: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1EstimateImageListResponse:
        """
        Estimate image credits

        Get the credits an image create request charges. Pass `tool`, then the fields below that the tool's create request uses, with the same values. Does not create a project or spend credits. It prices the fields passed here. It does not check your plan, your balance or the rest of the create request.

        GET /v1/estimate/image

        Args:
            image_count: The `image_count` of the create request. Used by `ai-image-generator`, `ai-image-editor`. Defaults to 1.
            mode: The `style.mode` of the create request. Used by `ai-image-upscaler`. One of `preserve`, `balanced`, `creative`. Defaults to `balanced`.
            model: The `model` of the create request. Used by `ai-image-generator`, `ai-image-editor`.
            resolution: The `resolution` of the create request. Used by `ai-image-generator`, `ai-image-editor`, `body-swap`. One of `640px`, `1k`, `2k`, `4k`.
            scale_factor: The `scale_factor` of the create request. Used by `ai-image-upscaler`. One of `2`, `4`.
            tool: The create endpoint to price, named by its path. For example `ai-image-editor` for `POST /v1/ai-image-editor`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.estimate.image.list(
            tool="ai-image-editor",
            image_count=4,
            model="nano-banana-2.1",
            resolution="2k",
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
                    "ai-clothes-changer",
                    "ai-face-editor",
                    "ai-gif-generator",
                    "ai-headshot-generator",
                    "ai-image-editor",
                    "ai-image-generator",
                    "ai-image-upscaler",
                    "ai-meme-generator",
                    "ai-qr-code-generator",
                    "body-swap",
                    "face-swap-photo",
                    "head-swap",
                    "image-background-remover",
                    "photo-colorizer",
                ],
            ),
            style="form",
            explode=True,
        )
        if not isinstance(image_count, type_utils.NotGiven):
            encode_query_param(
                _query,
                "image_count",
                to_encodable(item=image_count, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(mode, type_utils.NotGiven):
            encode_query_param(
                _query,
                "mode",
                to_encodable(item=mode, dump_with=str),
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
        if not isinstance(scale_factor, type_utils.NotGiven):
            encode_query_param(
                _query,
                "scale_factor",
                to_encodable(item=scale_factor, dump_with=float),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/estimate/image",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.V1EstimateImageListResponse,
            request_options=request_options or default_request_options(),
        )
