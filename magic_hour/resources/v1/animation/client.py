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


class AnimationClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1AnimationGenerateBodyAssets,
        end_seconds: float,
        fps: float,
        height: int,
        style: params.V1AnimationCreateBodyStyle,
        width: int,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate animation (alias for create with additional functionality).

        Create a Animation video. The estimated frame cost is calculated based on the `fps` and `end_seconds` input.

        Args:
            name: The name of video. This value is mainly used for your own identification of the video.
            assets: Provide the assets for animation.
            end_seconds: This value determines the duration of the output video.
            fps: The desire output video frame rate
            height: The height of the final output video. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            style: Defines the style of the output video
            width: The width of the final output video. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Animation API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.animation.generate(
            assets={
                "audio_file_path": "path/to/audio.mp3",
                "audio_source": "file",
                "image_file_path": "path/to/image.png",
            },
            end_seconds=15.0,
            fps=12.0,
            height=960,
            style={
                "art_style": "Painterly Illustration",
                "camera_effect": "Simple Zoom In",
                "prompt": "Cyberpunk city",
                "prompt_type": "custom",
                "transition_speed": 5,
            },
            width=512,
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = FilesClient(base_client=self._base_client)

        # Upload image file if provided
        if "image_file_path" in assets and assets["image_file_path"]:
            image_file_path = assets["image_file_path"]
            assets["image_file_path"] = file_client.upload_file(file=image_file_path)

        # Upload audio file if audio_source is "file" and audio_file_path is provided
        if (
            assets.get("audio_source") == "file"
            and "audio_file_path" in assets
            and assets["audio_file_path"]
        ):
            audio_file_path = assets["audio_file_path"]
            assets["audio_file_path"] = file_client.upload_file(file=audio_file_path)

        create_response = self.create(
            assets=assets,
            end_seconds=end_seconds,
            fps=fps,
            height=height,
            style=style,
            width=width,
            name=name,
            request_options=request_options,
        )
        logger.info(f"Animation response: {create_response}")

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
        assets: params.V1AnimationCreateBodyAssets,
        end_seconds: float,
        fps: float,
        height: int,
        style: params.V1AnimationCreateBodyStyle,
        width: int,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AnimationCreateResponse:
        """
        Animation

        Create a Animation video. The estimated frame cost is calculated based on the `fps` and `end_seconds` input.

        POST /v1/animation

        Args:
            name: The name of video. This value is mainly used for your own identification of the video.
            assets: Provide the assets for animation.
            end_seconds: This value determines the duration of the output video.
            fps: The desire output video frame rate
            height: The height of the final output video. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            style: Defines the style of the output video
            width: The width of the final output video. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.animation.create(
            assets={
                "audio_file_path": "api-assets/id/1234.mp3",
                "audio_source": "file",
                "image_file_path": "api-assets/id/1234.png",
            },
            end_seconds=15.0,
            fps=12.0,
            height=960,
            style={
                "art_style": "Painterly Illustration",
                "camera_effect": "Simple Zoom In",
                "prompt": "Cyberpunk city",
                "prompt_type": "custom",
                "transition_speed": 5,
            },
            width=512,
            name="Animation video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "assets": assets,
                "end_seconds": end_seconds,
                "fps": fps,
                "height": height,
                "style": style,
                "width": width,
            },
            dump_with=params._SerializerV1AnimationCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/animation",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AnimationCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAnimationClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1AnimationGenerateBodyAssets,
        end_seconds: float,
        fps: float,
        height: int,
        style: params.V1AnimationCreateBodyStyle,
        width: int,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate animation (alias for create with additional functionality).

        Create a Animation video. The estimated frame cost is calculated based on the `fps` and `end_seconds` input.

        Args:
            name: The name of video. This value is mainly used for your own identification of the video.
            assets: Provide the assets for animation.
            end_seconds: This value determines the duration of the output video.
            fps: The desire output video frame rate
            height: The height of the final output video. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            style: Defines the style of the output video
            width: The width of the final output video. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Animation API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.animation.generate(
            assets={
                "audio_file_path": "path/to/audio.mp3",
                "audio_source": "file",
                "image_file_path": "path/to/image.png",
            },
            end_seconds=15.0,
            fps=12.0,
            height=960,
            style={
                "art_style": "Painterly Illustration",
                "camera_effect": "Simple Zoom In",
                "prompt": "Cyberpunk city",
                "prompt_type": "custom",
                "transition_speed": 5,
            },
            width=512,
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = AsyncFilesClient(base_client=self._base_client)

        # Upload image file if provided
        if "image_file_path" in assets and assets["image_file_path"]:
            image_file_path = assets["image_file_path"]
            assets["image_file_path"] = await file_client.upload_file(
                file=image_file_path
            )

        # Upload audio file if audio_source is "file" and audio_file_path is provided
        if (
            assets.get("audio_source") == "file"
            and "audio_file_path" in assets
            and assets["audio_file_path"]
        ):
            audio_file_path = assets["audio_file_path"]
            assets["audio_file_path"] = await file_client.upload_file(
                file=audio_file_path
            )

        create_response = await self.create(
            assets=assets,
            end_seconds=end_seconds,
            fps=fps,
            height=height,
            style=style,
            width=width,
            name=name,
            request_options=request_options,
        )
        logger.info(f"Animation response: {create_response}")

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
        assets: params.V1AnimationCreateBodyAssets,
        end_seconds: float,
        fps: float,
        height: int,
        style: params.V1AnimationCreateBodyStyle,
        width: int,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AnimationCreateResponse:
        """
        Animation

        Create a Animation video. The estimated frame cost is calculated based on the `fps` and `end_seconds` input.

        POST /v1/animation

        Args:
            name: The name of video. This value is mainly used for your own identification of the video.
            assets: Provide the assets for animation.
            end_seconds: This value determines the duration of the output video.
            fps: The desire output video frame rate
            height: The height of the final output video. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            style: Defines the style of the output video
            width: The width of the final output video. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.animation.create(
            assets={
                "audio_file_path": "api-assets/id/1234.mp3",
                "audio_source": "file",
                "image_file_path": "api-assets/id/1234.png",
            },
            end_seconds=15.0,
            fps=12.0,
            height=960,
            style={
                "art_style": "Painterly Illustration",
                "camera_effect": "Simple Zoom In",
                "prompt": "Cyberpunk city",
                "prompt_type": "custom",
                "transition_speed": 5,
            },
            width=512,
            name="Animation video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "assets": assets,
                "end_seconds": end_seconds,
                "fps": fps,
                "height": height,
                "style": style,
                "width": width,
            },
            dump_with=params._SerializerV1AnimationCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/animation",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AnimationCreateResponse,
            request_options=request_options or default_request_options(),
        )
