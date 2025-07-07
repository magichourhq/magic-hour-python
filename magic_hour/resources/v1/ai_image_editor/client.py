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


class AiImageEditorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.V1AiImageEditorCreateBodyAssets,
        style: params.V1AiImageEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiImageEditorCreateResponse:
        """
        AI Image Editor

        Edit images with AI. Each edit costs 50 credits.

        POST /v1/ai-image-editor

        Args:
            name: The name of image
            assets: Provide the assets for image edit
            style: V1AiImageEditorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_image_editor.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            style={"prompt": "Give me sunglasses"},
            name="Ai Image Editor image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets, "style": style},
            dump_with=params._SerializerV1AiImageEditorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-image-editor",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiImageEditorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiImageEditorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.V1AiImageEditorCreateBodyAssets,
        style: params.V1AiImageEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiImageEditorCreateResponse:
        """
        AI Image Editor

        Edit images with AI. Each edit costs 50 credits.

        POST /v1/ai-image-editor

        Args:
            name: The name of image
            assets: Provide the assets for image edit
            style: V1AiImageEditorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_image_editor.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            style={"prompt": "Give me sunglasses"},
            name="Ai Image Editor image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets, "style": style},
            dump_with=params._SerializerV1AiImageEditorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-image-editor",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiImageEditorCreateResponse,
            request_options=request_options or default_request_options(),
        )
