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


class AiPhotoEditorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.V1AiPhotoEditorCreateBodyAssets,
        resolution: int,
        style: params.V1AiPhotoEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        steps: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiPhotoEditorCreateResponse:
        """
        AI Photo Editor

        > **NOTE**: this API is still in early development stages, and should be avoided. Please reach out to us if you're interested in this API.

        Edit photo using AI. Each photo costs 10 credits.

        POST /v1/ai-photo-editor

        Args:
            name: The name of image
            steps: Deprecated: Please use `.style.steps` instead. Number of iterations used to generate the output. Higher values improve quality and increase the strength of the prompt but increase processing time.
            assets: Provide the assets for photo editor
            resolution: The resolution of the final output image. The allowed value is based on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            style: V1AiPhotoEditorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_photo_editor.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            resolution=768,
            style={
                "image_description": "A photo of a person",
                "likeness_strength": 5.2,
                "negative_prompt": "painting, cartoon, sketch",
                "prompt": "A photo portrait of a person wearing a hat",
                "prompt_strength": 3.75,
                "steps": 4,
                "upscale_factor": 2,
                "upscale_fidelity": 0.5,
            },
            name="Photo Editor image",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "steps": steps,
                "assets": assets,
                "resolution": resolution,
                "style": style,
            },
            dump_with=params._SerializerV1AiPhotoEditorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-photo-editor",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiPhotoEditorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiPhotoEditorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.V1AiPhotoEditorCreateBodyAssets,
        resolution: int,
        style: params.V1AiPhotoEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        steps: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiPhotoEditorCreateResponse:
        """
        AI Photo Editor

        > **NOTE**: this API is still in early development stages, and should be avoided. Please reach out to us if you're interested in this API.

        Edit photo using AI. Each photo costs 10 credits.

        POST /v1/ai-photo-editor

        Args:
            name: The name of image
            steps: Deprecated: Please use `.style.steps` instead. Number of iterations used to generate the output. Higher values improve quality and increase the strength of the prompt but increase processing time.
            assets: Provide the assets for photo editor
            resolution: The resolution of the final output image. The allowed value is based on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            style: V1AiPhotoEditorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_photo_editor.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            resolution=768,
            style={
                "image_description": "A photo of a person",
                "likeness_strength": 5.2,
                "negative_prompt": "painting, cartoon, sketch",
                "prompt": "A photo portrait of a person wearing a hat",
                "prompt_strength": 3.75,
                "steps": 4,
                "upscale_factor": 2,
                "upscale_fidelity": 0.5,
            },
            name="Photo Editor image",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "steps": steps,
                "assets": assets,
                "resolution": resolution,
                "style": style,
            },
            dump_with=params._SerializerV1AiPhotoEditorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-photo-editor",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiPhotoEditorCreateResponse,
            request_options=request_options or default_request_options(),
        )
