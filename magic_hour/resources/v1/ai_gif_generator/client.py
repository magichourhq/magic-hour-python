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


class AiGifGeneratorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        style: params.V1AiGifGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiGifGeneratorCreateResponse:
        """
        AI GIFs

        Create an AI GIF. Each GIF costs 25 credits.

        POST /v1/ai-gif-generator

        Args:
            name: The name of gif
            style: V1AiGifGeneratorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_gif_generator.create(
            style={"prompt": "Cute dancing cat, pixel art"}, name="Ai Gif gif"
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "style": style},
            dump_with=params._SerializerV1AiGifGeneratorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-gif-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiGifGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiGifGeneratorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        style: params.V1AiGifGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiGifGeneratorCreateResponse:
        """
        AI GIFs

        Create an AI GIF. Each GIF costs 25 credits.

        POST /v1/ai-gif-generator

        Args:
            name: The name of gif
            style: V1AiGifGeneratorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_gif_generator.create(
            style={"prompt": "Cute dancing cat, pixel art"}, name="Ai Gif gif"
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "style": style},
            dump_with=params._SerializerV1AiGifGeneratorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-gif-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiGifGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )
