import typing

from magic_hour.helpers.logger import get_sdk_logger
from magic_hour.resources.v1.files.client import AsyncFilesClient, FilesClient
from magic_hour.resources.v1.video_projects.client import (
    AsyncVideoProjectsClient,
    VideoProjectsClient,
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


class AiTalkingPhotoClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1AiTalkingPhotoGenerateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1AiTalkingPhotoCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate talking photo (alias for create with additional functionality).

        Create a talking photo from an image and audio or text input. Each generation costs credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            style: Attributes used to dictate the style of the output
            assets: Provide the assets for creating a talking photo
            end_seconds: The end time of the input audio in seconds. The maximum duration allowed is 60 seconds.
            start_seconds: The start time of the input audio in seconds. The maximum duration allowed is 60 seconds.
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the AI Talking Photo API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.ai_talking_photo.generate(
            assets={
                "audio_file_path": "path/to/audio.mp3",
                "image_file_path": "path/to/image.png",
            },
            end_seconds=30.0,
            start_seconds=5.0,
            style={"enhancement": "high"},
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = FilesClient(base_client=self._base_client)

        audio_file_path = assets["audio_file_path"]
        image_file_path = assets["image_file_path"]
        assets["audio_file_path"] = file_client.upload_file(file=audio_file_path)
        assets["image_file_path"] = file_client.upload_file(file=image_file_path)

        create_response = self.create(
            assets=assets,
            end_seconds=end_seconds,
            start_seconds=start_seconds,
            name=name,
            style=style,
            request_options=request_options,
        )
        logger.info(f"AI Talking Photo response: {create_response}")

        video_projects_client = VideoProjectsClient(base_client=self._base_client)
        response = video_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

        return response

    def create(
        self,
        *,
        assets: params.V1AiTalkingPhotoCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1AiTalkingPhotoCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiTalkingPhotoCreateResponse:
        """
        AI Talking Photo

        Create a talking photo from an image and audio or text input.

        POST /v1/ai-talking-photo

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            style: Attributes used to dictate the style of the output
            assets: Provide the assets for creating a talking photo
            end_seconds: The end time of the input audio in seconds. The maximum duration allowed is 60 seconds.
            start_seconds: The start time of the input audio in seconds. The maximum duration allowed is 60 seconds.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_talking_photo.create(
            assets={
                "audio_file_path": "api-assets/id/1234.mp3",
                "image_file_path": "api-assets/id/1234.png",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            name="Talking Photo image",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "style": style,
                "assets": assets,
                "end_seconds": end_seconds,
                "start_seconds": start_seconds,
            },
            dump_with=params._SerializerV1AiTalkingPhotoCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-talking-photo",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiTalkingPhotoCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiTalkingPhotoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1AiTalkingPhotoGenerateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1AiTalkingPhotoCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate talking photo (alias for create with additional functionality).

        Create a talking photo from an image and audio or text input. Each generation costs credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            style: Attributes used to dictate the style of the output
            assets: Provide the assets for creating a talking photo
            end_seconds: The end time of the input audio in seconds. The maximum duration allowed is 60 seconds.
            start_seconds: The start time of the input audio in seconds. The maximum duration allowed is 60 seconds.
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the AI Talking Photo API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.ai_talking_photo.generate(
            assets={
                "audio_file_path": "path/to/audio.mp3",
                "image_file_path": "path/to/image.png",
            },
            end_seconds=30.0,
            start_seconds=5.0,
            style={"enhancement": "high"},
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = AsyncFilesClient(base_client=self._base_client)

        audio_file_path = assets["audio_file_path"]
        image_file_path = assets["image_file_path"]
        assets["audio_file_path"] = await file_client.upload_file(file=audio_file_path)
        assets["image_file_path"] = await file_client.upload_file(file=image_file_path)

        create_response = await self.create(
            assets=assets,
            end_seconds=end_seconds,
            start_seconds=start_seconds,
            name=name,
            style=style,
            request_options=request_options,
        )
        logger.info(f"AI Talking Photo response: {create_response}")

        video_projects_client = AsyncVideoProjectsClient(base_client=self._base_client)
        response = await video_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

        return response

    async def create(
        self,
        *,
        assets: params.V1AiTalkingPhotoCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1AiTalkingPhotoCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiTalkingPhotoCreateResponse:
        """
        AI Talking Photo

        Create a talking photo from an image and audio or text input.

        POST /v1/ai-talking-photo

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            style: Attributes used to dictate the style of the output
            assets: Provide the assets for creating a talking photo
            end_seconds: The end time of the input audio in seconds. The maximum duration allowed is 60 seconds.
            start_seconds: The start time of the input audio in seconds. The maximum duration allowed is 60 seconds.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_talking_photo.create(
            assets={
                "audio_file_path": "api-assets/id/1234.mp3",
                "image_file_path": "api-assets/id/1234.png",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            name="Talking Photo image",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "style": style,
                "assets": assets,
                "end_seconds": end_seconds,
                "start_seconds": start_seconds,
            },
            dump_with=params._SerializerV1AiTalkingPhotoCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-talking-photo",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiTalkingPhotoCreateResponse,
            request_options=request_options or default_request_options(),
        )
