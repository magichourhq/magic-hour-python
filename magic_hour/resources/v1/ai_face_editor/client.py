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


class AiFaceEditorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1AiFaceEditorGenerateBodyAssets,
        style: params.V1AiFaceEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate face edited image (alias for create with additional functionality).

        Edit facial features of an image using AI. Each edit costs 1 frame. The height/width of the output image depends on your subscription. Please refer to our [pricing](/pricing) page for more details

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for face editor
            style: Face editing parameters
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the AI Face Editor API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.ai_face_editor.generate(
            assets={"image_file_path": "path/to/face.png"},
            style={
                "enhance_face": True,
                "eye_gaze_horizontal": 0.2,
                "eye_gaze_vertical": -0.1,
                "eye_open_ratio": 0.8,
                "eyebrow_direction": 0.3,
                "head_pitch": 0.1,
                "head_roll": 0.0,
                "head_yaw": -0.2,
                "lip_open_ratio": 0.0,
                "mouth_grim": 0.0,
                "mouth_position_horizontal": 0.0,
                "mouth_position_vertical": 0.0,
                "mouth_pout": 0.0,
                "mouth_purse": 0.0,
                "mouth_smile": 0.5,
            },
            name="Face Editor image",
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
            assets=assets, style=style, name=name, request_options=request_options
        )
        logger.info(f"AI Face Editor response: {create_response}")

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
        assets: params.V1AiFaceEditorCreateBodyAssets,
        style: params.V1AiFaceEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiFaceEditorCreateResponse:
        """
        AI Face Editor

        Edit facial features of an image using AI. Each edit costs 1 frame. The height/width of the output image depends on your subscription. Please refer to our [pricing](/pricing) page for more details

        POST /v1/ai-face-editor

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for face editor
            style: Face editing parameters
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_face_editor.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            style={
                "enhance_face": False,
                "eye_gaze_horizontal": 0.0,
                "eye_gaze_vertical": 0.0,
                "eye_open_ratio": 0.0,
                "eyebrow_direction": 0.0,
                "head_pitch": 0.0,
                "head_roll": 0.0,
                "head_yaw": 0.0,
                "lip_open_ratio": 0.0,
                "mouth_grim": 0.0,
                "mouth_position_horizontal": 0.0,
                "mouth_position_vertical": 0.0,
                "mouth_pout": 0.0,
                "mouth_purse": 0.0,
                "mouth_smile": 0.0,
            },
            name="Face Editor image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets, "style": style},
            dump_with=params._SerializerV1AiFaceEditorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-face-editor",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiFaceEditorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiFaceEditorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1AiFaceEditorGenerateBodyAssets,
        style: params.V1AiFaceEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate face edited image (alias for create with additional functionality).

        Edit facial features of an image using AI. Each edit costs 1 frame. The height/width of the output image depends on your subscription. Please refer to our [pricing](/pricing) page for more details

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for face editor
            style: Face editing parameters
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the AI Face Editor API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.ai_face_editor.generate(
            assets={"image_file_path": "path/to/face.png"},
            style={
                "enhance_face": True,
                "eye_gaze_horizontal": 0.2,
                "eye_gaze_vertical": -0.1,
                "eye_open_ratio": 0.8,
                "eyebrow_direction": 0.3,
                "head_pitch": 0.1,
                "head_roll": 0.0,
                "head_yaw": -0.2,
                "lip_open_ratio": 0.0,
                "mouth_grim": 0.0,
                "mouth_position_horizontal": 0.0,
                "mouth_position_vertical": 0.0,
                "mouth_pout": 0.0,
                "mouth_purse": 0.0,
                "mouth_smile": 0.5,
            },
            name="Face Editor image",
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
            assets=assets, style=style, name=name, request_options=request_options
        )
        logger.info(f"AI Face Editor response: {create_response}")

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
        assets: params.V1AiFaceEditorCreateBodyAssets,
        style: params.V1AiFaceEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiFaceEditorCreateResponse:
        """
        AI Face Editor

        Edit facial features of an image using AI. Each edit costs 1 frame. The height/width of the output image depends on your subscription. Please refer to our [pricing](/pricing) page for more details

        POST /v1/ai-face-editor

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for face editor
            style: Face editing parameters
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_face_editor.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            style={
                "enhance_face": False,
                "eye_gaze_horizontal": 0.0,
                "eye_gaze_vertical": 0.0,
                "eye_open_ratio": 0.0,
                "eyebrow_direction": 0.0,
                "head_pitch": 0.0,
                "head_roll": 0.0,
                "head_yaw": 0.0,
                "lip_open_ratio": 0.0,
                "mouth_grim": 0.0,
                "mouth_position_horizontal": 0.0,
                "mouth_position_vertical": 0.0,
                "mouth_pout": 0.0,
                "mouth_purse": 0.0,
                "mouth_smile": 0.0,
            },
            name="Face Editor image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets, "style": style},
            dump_with=params._SerializerV1AiFaceEditorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-face-editor",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiFaceEditorCreateResponse,
            request_options=request_options or default_request_options(),
        )
