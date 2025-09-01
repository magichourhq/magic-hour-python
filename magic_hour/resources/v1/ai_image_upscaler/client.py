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


class AiImageUpscalerClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1AiImageUpscalerGenerateBodyAssets,
        scale_factor: float,
        style: params.V1AiImageUpscalerCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate upscaled image (alias for create with additional functionality).

        Upscale image using AI. Each upscale costs 5 credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for image upscaler
            scale_factor: How much to scale the image. Must be either 2 or 4.
            style: Image upscaling parameters
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the AI Image Upscaler API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.ai_image_upscaler.generate(
            assets={"image_file_path": "path/to/image.png"},
            scale_factor=2.0,
            style={"enhancement": "Balanced"},
            name="Upscaled Image",
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
            scale_factor=scale_factor,
            style=style,
            name=name,
            request_options=request_options,
        )
        logger.info(f"AI Image Upscaler response: {create_response}")

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
        assets: params.V1AiImageUpscalerCreateBodyAssets,
        scale_factor: float,
        style: params.V1AiImageUpscalerCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiImageUpscalerCreateResponse:
        """
        AI Image Upscaler

        Upscale your image using AI. Each 2x upscale costs 50 credits, and 4x upscale costs 200 credits.

        POST /v1/ai-image-upscaler

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for upscaling
            scale_factor: How much to scale the image. Must be either 2 or 4.

        Note: 4x upscale is only available on Creator, Pro, or Business tier.
            style: V1AiImageUpscalerCreateBodyStyle
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
            dump_with=params._SerializerV1AiImageUpscalerCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-image-upscaler",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiImageUpscalerCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiImageUpscalerClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1AiImageUpscalerGenerateBodyAssets,
        scale_factor: float,
        style: params.V1AiImageUpscalerCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate upscaled image (alias for create with additional functionality).

        Upscale image using AI. Each upscale costs 5 credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for image upscaler
            scale_factor: How much to scale the image. Must be either 2 or 4.
            style: Image upscaling parameters
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the AI Image Upscaler API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.ai_image_upscaler.generate(
            assets={"image_file_path": "path/to/image.png"},
            scale_factor=2.0,
            style={"enhancement": "Balanced"},
            name="Upscaled Image",
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
            scale_factor=scale_factor,
            style=style,
            name=name,
            request_options=request_options,
        )
        logger.info(f"AI Image Upscaler response: {create_response}")

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
        assets: params.V1AiImageUpscalerCreateBodyAssets,
        scale_factor: float,
        style: params.V1AiImageUpscalerCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiImageUpscalerCreateResponse:
        """
        AI Image Upscaler

        Upscale your image using AI. Each 2x upscale costs 50 credits, and 4x upscale costs 200 credits.

        POST /v1/ai-image-upscaler

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for upscaling
            scale_factor: How much to scale the image. Must be either 2 or 4.

        Note: 4x upscale is only available on Creator, Pro, or Business tier.
            style: V1AiImageUpscalerCreateBodyStyle
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
            dump_with=params._SerializerV1AiImageUpscalerCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-image-upscaler",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiImageUpscalerCreateResponse,
            request_options=request_options or default_request_options(),
        )
