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


class AiImageEditorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1AiImageEditorGenerateBodyAssets,
        style: params.V1AiImageEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate edited image (alias for create with additional functionality).

        Edit image using AI. Each edit costs 5 credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for image editor
            style: Image editing parameters
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the AI Image Editor API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.ai_image_editor.generate(
            assets={"image_file_paths": ["path/to/image.png", "path/to/image2.png"]},
            style={"prompt": "Add a sunset background"},
            name="Edited Image",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = FilesClient(base_client=self._base_client)

        if "image_file_path" in assets:
            image_file_path = assets["image_file_path"]
            assets["image_file_path"] = file_client.upload_file(file=image_file_path)

        if "image_file_paths" in assets:
            for image_file_path in assets["image_file_paths"]:
                assets["image_file_paths"] = [
                    file_client.upload_file(file=image_file_path)
                    for image_file_path in assets["image_file_paths"]
                ]

        create_response = self.create(
            assets=assets, style=style, name=name, request_options=request_options
        )
        logger.info(f"AI Image Editor response: {create_response}")

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
            name: The name of image. This value is mainly used for your own identification of the image.
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
            assets={
                "image_file_path": "api-assets/id/1234.png",
                "image_file_paths": [
                    "api-assets/id/1234.png",
                    "api-assets/id/1235.png",
                ],
            },
            style={"model": "Nano Banana", "prompt": "Give me sunglasses"},
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

    async def generate(
        self,
        *,
        assets: params.V1AiImageEditorGenerateBodyAssets,
        style: params.V1AiImageEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate edited image (alias for create with additional functionality).

        Edit image using AI. Each edit costs 5 credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for image editor
            style: Image editing parameters
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the AI Image Editor API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.ai_image_editor.generate(
            assets={"image_file_paths": ["path/to/image.png", "path/to/image2.png"]},
            style={"prompt": "Add a sunset background"},
            name="Edited Image",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = AsyncFilesClient(base_client=self._base_client)

        if "image_file_path" in assets:
            image_file_path = assets["image_file_path"]
            assets["image_file_path"] = await file_client.upload_file(
                file=image_file_path
            )

        if "image_file_paths" in assets:
            for image_file_path in assets["image_file_paths"]:
                assets["image_file_paths"] = [
                    await file_client.upload_file(file=image_file_path)
                    for image_file_path in assets["image_file_paths"]
                ]

        create_response = await self.create(
            assets=assets, style=style, name=name, request_options=request_options
        )
        logger.info(f"AI Image Editor response: {create_response}")

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
            name: The name of image. This value is mainly used for your own identification of the image.
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
            assets={
                "image_file_path": "api-assets/id/1234.png",
                "image_file_paths": [
                    "api-assets/id/1234.png",
                    "api-assets/id/1235.png",
                ],
            },
            style={"model": "Nano Banana", "prompt": "Give me sunglasses"},
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
