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


class AiHeadshotGeneratorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.PostV1AiHeadshotGeneratorBodyAssets,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1AiHeadshotGeneratorResponse:
        """
        AI Headshots

        Create an AI headshot. Each headshot costs 50 frames.

        POST /v1/ai-headshot-generator

        Args:
            name: The name of image
            assets: Provide the assets for headshot photo
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_headshot_generator.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            name="Ai Headshot image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets},
            dump_with=params._SerializerPostV1AiHeadshotGeneratorBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-headshot-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1AiHeadshotGeneratorResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiHeadshotGeneratorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.PostV1AiHeadshotGeneratorBodyAssets,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1AiHeadshotGeneratorResponse:
        """
        AI Headshots

        Create an AI headshot. Each headshot costs 50 frames.

        POST /v1/ai-headshot-generator

        Args:
            name: The name of image
            assets: Provide the assets for headshot photo
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_headshot_generator.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            name="Ai Headshot image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets},
            dump_with=params._SerializerPostV1AiHeadshotGeneratorBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-headshot-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1AiHeadshotGeneratorResponse,
            request_options=request_options or default_request_options(),
        )
