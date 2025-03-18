import typing

from magic_hour.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from magic_hour.types import models, params


class AiImageUpscalerClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.PostV1AiImageUpscalerBodyAssets,
        scale_factor: float,
        style: params.PostV1AiImageUpscalerBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1AiImageUpscalerResponse:
        """
        AI Image Upscaler

        Upscale your image using AI. Each 2x upscale costs 50 frames, and 4x upscale costs 200 frames.

        POST /v1/ai-image-upscaler

        Args:
            name: The name of image
            assets: Provide the assets for upscaling
            scale_factor: How much to scale the image. Must be either 2 or 4
            style: PostV1AiImageUpscalerBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_image_upscaler.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            scale_factor=2.0,
            style={"enhancement": "Balanced"},
            name="Image Upscaler image",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "assets": assets,
                "scale_factor": scale_factor,
                "style": style,
            },
            dump_with=params._SerializerPostV1AiImageUpscalerBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-image-upscaler",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1AiImageUpscalerResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiImageUpscalerClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.PostV1AiImageUpscalerBodyAssets,
        scale_factor: float,
        style: params.PostV1AiImageUpscalerBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1AiImageUpscalerResponse:
        """
        AI Image Upscaler

        Upscale your image using AI. Each 2x upscale costs 50 frames, and 4x upscale costs 200 frames.

        POST /v1/ai-image-upscaler

        Args:
            name: The name of image
            assets: Provide the assets for upscaling
            scale_factor: How much to scale the image. Must be either 2 or 4
            style: PostV1AiImageUpscalerBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_image_upscaler.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            scale_factor=2.0,
            style={"enhancement": "Balanced"},
            name="Image Upscaler image",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "assets": assets,
                "scale_factor": scale_factor,
                "style": style,
            },
            dump_with=params._SerializerPostV1AiImageUpscalerBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-image-upscaler",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1AiImageUpscalerResponse,
            request_options=request_options or default_request_options(),
        )
