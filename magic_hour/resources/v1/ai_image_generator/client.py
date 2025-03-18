import typing
import typing_extensions

from magic_hour.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from magic_hour.types import models, params


class AiImageGeneratorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        image_count: int,
        orientation: typing_extensions.Literal["landscape", "portrait", "square"],
        style: params.PostV1AiImageGeneratorBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1AiImageGeneratorResponse:
        """
        AI Images

        Create an AI image. Each image costs 5 frames.

        POST /v1/ai-image-generator

        Args:
            name: The name of image
            image_count: number to images to generate
            orientation: typing_extensions.Literal["landscape", "portrait", "square"]
            style: PostV1AiImageGeneratorBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_image_generator.create(
            image_count=1,
            orientation="landscape",
            style={"prompt": "Cool image"},
            name="Ai Image image",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "image_count": image_count,
                "orientation": orientation,
                "style": style,
            },
            dump_with=params._SerializerPostV1AiImageGeneratorBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-image-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1AiImageGeneratorResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiImageGeneratorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        image_count: int,
        orientation: typing_extensions.Literal["landscape", "portrait", "square"],
        style: params.PostV1AiImageGeneratorBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1AiImageGeneratorResponse:
        """
        AI Images

        Create an AI image. Each image costs 5 frames.

        POST /v1/ai-image-generator

        Args:
            name: The name of image
            image_count: number to images to generate
            orientation: typing_extensions.Literal["landscape", "portrait", "square"]
            style: PostV1AiImageGeneratorBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_image_generator.create(
            image_count=1,
            orientation="landscape",
            style={"prompt": "Cool image"},
            name="Ai Image image",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "image_count": image_count,
                "orientation": orientation,
                "style": style,
            },
            dump_with=params._SerializerPostV1AiImageGeneratorBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-image-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1AiImageGeneratorResponse,
            request_options=request_options or default_request_options(),
        )
