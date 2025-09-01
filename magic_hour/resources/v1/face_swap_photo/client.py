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


class FaceSwapPhotoClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1FaceSwapPhotoGenerateBodyAssets,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate face swap photo (alias for create with additional functionality).

        Swap faces in a photo using AI. Each face swap costs 5 credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for face swap photo
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the Face Swap Photo API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        client.v1.face_swap_photo.generate(
            assets={
                "face_swap_mode": "all-faces",
                "source_file_path": "api-assets/id/1234.png",
                "target_file_path": "api-assets/id/1234.png",
            },
            name="Face Swap image",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="./outputs/",
        )
        ```
        """

        file_client = FilesClient(base_client=self._base_client)

        # Upload source image file if present
        if "source_file_path" in assets and assets["source_file_path"]:
            source_file_path = assets["source_file_path"]
            assets["source_file_path"] = file_client.upload_file(file=source_file_path)

        # Upload target image file
        target_file_path = assets["target_file_path"]
        assets["target_file_path"] = file_client.upload_file(file=target_file_path)

        # Upload face mappings if present
        if "face_mappings" in assets and assets["face_mappings"]:
            for face_mapping in assets["face_mappings"]:
                if "new_face" in face_mapping and face_mapping["new_face"]:
                    new_face_file_path = face_mapping["new_face"]
                    face_mapping["new_face"] = file_client.upload_file(
                        file=new_face_file_path
                    )

        create_response = self.create(
            assets=assets, name=name, request_options=request_options
        )
        logger.info(f"Face Swap Photo response: {create_response}")

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
        assets: params.V1FaceSwapPhotoCreateBodyAssets,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1FaceSwapPhotoCreateResponse:
        """
        Face Swap Photo

        Create a face swap photo. Each photo costs 5 credits. The height/width of the output image depends on your subscription. Please refer to our [pricing](https://magichour.ai/pricing) page for more details

        POST /v1/face-swap-photo

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for face swap photo
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.face_swap_photo.create(
            assets={
                "face_mappings": [
                    {
                        "new_face": "api-assets/id/1234.png",
                        "original_face": "api-assets/id/0-0.png",
                    }
                ],
                "face_swap_mode": "all-faces",
                "source_file_path": "api-assets/id/1234.png",
                "target_file_path": "api-assets/id/1234.png",
            },
            name="Face Swap image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets},
            dump_with=params._SerializerV1FaceSwapPhotoCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/face-swap-photo",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1FaceSwapPhotoCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncFaceSwapPhotoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1FaceSwapPhotoGenerateBodyAssets,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate face swap photo (alias for create with additional functionality).

        Swap faces in a photo using AI. Each face swap costs 5 credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for face swap photo
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the Face Swap Photo API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        await client.v1.face_swap_photo.generate(
            assets={
                "face_swap_mode": "all-faces",
                "source_file_path": "api-assets/id/1234.png",
                "target_file_path": "api-assets/id/1234.png",
            },
            name="Face Swap image",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="./outputs/",
        )
        ```
        """

        file_client = AsyncFilesClient(base_client=self._base_client)

        # Upload source image file if present
        if "source_file_path" in assets and assets["source_file_path"]:
            source_file_path = assets["source_file_path"]
            assets["source_file_path"] = await file_client.upload_file(
                file=source_file_path
            )

        # Upload target image file
        target_file_path = assets["target_file_path"]
        assets["target_file_path"] = await file_client.upload_file(
            file=target_file_path
        )

        # Upload face mappings if present
        if "face_mappings" in assets and assets["face_mappings"]:
            for face_mapping in assets["face_mappings"]:
                if "new_face" in face_mapping and face_mapping["new_face"]:
                    new_face_file_path = face_mapping["new_face"]
                    face_mapping["new_face"] = await file_client.upload_file(
                        file=new_face_file_path
                    )

        create_response = await self.create(
            assets=assets, name=name, request_options=request_options
        )
        logger.info(f"Face Swap Photo response: {create_response}")

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
        assets: params.V1FaceSwapPhotoCreateBodyAssets,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1FaceSwapPhotoCreateResponse:
        """
        Face Swap Photo

        Create a face swap photo. Each photo costs 5 credits. The height/width of the output image depends on your subscription. Please refer to our [pricing](https://magichour.ai/pricing) page for more details

        POST /v1/face-swap-photo

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for face swap photo
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.face_swap_photo.create(
            assets={
                "face_mappings": [
                    {
                        "new_face": "api-assets/id/1234.png",
                        "original_face": "api-assets/id/0-0.png",
                    }
                ],
                "face_swap_mode": "all-faces",
                "source_file_path": "api-assets/id/1234.png",
                "target_file_path": "api-assets/id/1234.png",
            },
            name="Face Swap image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets},
            dump_with=params._SerializerV1FaceSwapPhotoCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/face-swap-photo",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1FaceSwapPhotoCreateResponse,
            request_options=request_options or default_request_options(),
        )
