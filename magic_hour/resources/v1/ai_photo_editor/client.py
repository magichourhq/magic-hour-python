import typing

from magic_hour.helpers.logger import get_sdk_logger
from magic_hour.resources.v1.files.client import AsyncFilesClient, FilesClient
from magic_hour.resources.v1.image_projects.client import (
    AsyncImageProjectsClient,
    ImageProjectsClient,
)
from magic_hour.types import models, params
from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)


logger = get_sdk_logger(__name__)


class AiPhotoEditorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1AiPhotoEditorGenerateBodyAssets,
        resolution: int,
        style: params.V1AiPhotoEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        steps: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate edited photo (alias for create with additional functionality).

        Edit photo using AI. Each edit costs 5 credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for photo editor
            style: Photo editing parameters
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the AI Photo Editor API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.ai_photo_editor.generate(
            assets={"image_file_path": "path/to/photo.jpg"},
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
            name="Edited Portrait",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = FilesClient(base_client=self._base_client)

        image_file_path = assets["image_file_path"]
        assets["image_file_path"] = file_client.upload_file(file=image_file_path)

        create_response = self.create(
            assets=assets,
            resolution=resolution,
            style=style,
            name=name,
            steps=steps,
            request_options=request_options,
        )
        logger.info(f"AI Photo Editor response: {create_response}")

        image_projects_client = ImageProjectsClient(base_client=self._base_client)
        response = image_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

        return response

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
            name: The name of image. This value is mainly used for your own identification of the image.
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

    async def generate(
        self,
        *,
        assets: params.V1AiPhotoEditorGenerateBodyAssets,
        resolution: int,
        style: params.V1AiPhotoEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        steps: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate edited photo (alias for create with additional functionality).

        Edit photo using AI. Each edit costs 5 credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for photo editor
            style: Photo editing parameters
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the AI Photo Editor API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.ai_photo_editor.generate(
            assets={"image_file_path": "path/to/photo.jpg"},
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
            name="Edited Portrait",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = AsyncFilesClient(base_client=self._base_client)

        image_file_path = assets["image_file_path"]
        assets["image_file_path"] = await file_client.upload_file(file=image_file_path)

        create_response = await self.create(
            assets=assets,
            resolution=resolution,
            style=style,
            name=name,
            steps=steps,
            request_options=request_options,
        )
        logger.info(f"AI Photo Editor response: {create_response}")

        image_projects_client = AsyncImageProjectsClient(base_client=self._base_client)
        response = await image_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

        return response

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
            name: The name of image. This value is mainly used for your own identification of the image.
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
