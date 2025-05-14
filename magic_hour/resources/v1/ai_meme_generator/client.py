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


class AiMemeGeneratorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        style: params.V1AiMemeGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiMemeGeneratorCreateResponse:
        """
        AI Meme Generator

        Create an AI generated meme. Each meme costs 10 credits.

        POST /v1/ai-meme-generator

        Args:
            name: The name of the meme.
            style: V1AiMemeGeneratorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_meme_generator.create(
            style={
                "search_web": False,
                "template": "Drake Hotline Bling",
                "topic": "When the code finally works",
            },
            name="My Funny Meme",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "style": style},
            dump_with=params._SerializerV1AiMemeGeneratorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-meme-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiMemeGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiMemeGeneratorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        style: params.V1AiMemeGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiMemeGeneratorCreateResponse:
        """
        AI Meme Generator

        Create an AI generated meme. Each meme costs 10 credits.

        POST /v1/ai-meme-generator

        Args:
            name: The name of the meme.
            style: V1AiMemeGeneratorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_meme_generator.create(
            style={
                "search_web": False,
                "template": "Drake Hotline Bling",
                "topic": "When the code finally works",
            },
            name="My Funny Meme",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "style": style},
            dump_with=params._SerializerV1AiMemeGeneratorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-meme-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiMemeGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )
