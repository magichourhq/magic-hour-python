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


class LipSyncClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1LipSyncGenerateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        max_fps_limit: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1LipSyncCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        width: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate lip sync video (alias for create with additional functionality).

        Create a Lip Sync video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Args:
            height: `height` is deprecated and no longer influences the output video's resolution.
            max_fps_limit: Defines the maximum FPS (frames per second) for the output video. If the input video's FPS is lower than this limit, the output video will retain the input FPS. This is useful for reducing unnecessary frame usage in scenarios where high FPS is not required.
            name: The name of video. This value is mainly used for your own identification of the video.
            style: Attributes used to dictate the style of the output
            width: `width` is deprecated and no longer influences the output video's resolution.
            assets: Provide the assets for lip-sync. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
            start_seconds: The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Lip Sync API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.lip_sync.generate(
            assets={
                "audio_file_path": "path/to/audio.mp3",
                "video_file_path": "path/to/video.mp4",
                "video_source": "file",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            max_fps_limit=12.0,
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = FilesClient(base_client=self._base_client)

        # Upload audio file (always required)
        audio_file_path = assets["audio_file_path"]
        assets["audio_file_path"] = file_client.upload_file(file=audio_file_path)

        # Upload video file if video_source is "file" and video_file_path is provided
        if (
            assets.get("video_source") == "file"
            and "video_file_path" in assets
            and assets["video_file_path"]
        ):
            video_file_path = assets["video_file_path"]
            assets["video_file_path"] = file_client.upload_file(file=video_file_path)

        create_response = self.create(
            assets=assets,
            end_seconds=end_seconds,
            start_seconds=start_seconds,
            height=height,
            max_fps_limit=max_fps_limit,
            name=name,
            style=style,
            width=width,
            request_options=request_options,
        )
        logger.info(f"Lip Sync response: {create_response}")

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
        assets: params.V1LipSyncCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        max_fps_limit: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1LipSyncCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        width: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1LipSyncCreateResponse:
        """
        Lip Sync

        Create a Lip Sync video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](https://magichour.ai/products/lip-sync).


        POST /v1/lip-sync

        Args:
            height: `height` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            max_fps_limit: Defines the maximum FPS (frames per second) for the output video. If the input video's FPS is lower than this limit, the output video will retain the input FPS. This is useful for reducing unnecessary frame usage in scenarios where high FPS is not required.
            name: The name of video. This value is mainly used for your own identification of the video.
            style: Attributes used to dictate the style of the output
            width: `width` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            assets: Provide the assets for lip-sync. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
            start_seconds: The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.lip_sync.create(
            assets={
                "audio_file_path": "api-assets/id/1234.mp3",
                "video_file_path": "api-assets/id/1234.mp4",
                "video_source": "file",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            max_fps_limit=12.0,
            name="Lip Sync video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "height": height,
                "max_fps_limit": max_fps_limit,
                "name": name,
                "style": style,
                "width": width,
                "assets": assets,
                "end_seconds": end_seconds,
                "start_seconds": start_seconds,
            },
            dump_with=params._SerializerV1LipSyncCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/lip-sync",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1LipSyncCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncLipSyncClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1LipSyncGenerateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        max_fps_limit: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        width: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate lip sync video (alias for create with additional functionality).

        Create a Lip Sync video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Args:
            height: `height` is deprecated and no longer influences the output video's resolution.
            max_fps_limit: Defines the maximum FPS (frames per second) for the output video. If the input video's FPS is lower than this limit, the output video will retain the input FPS. This is useful for reducing unnecessary frame usage in scenarios where high FPS is not required.
            name: The name of video. This value is mainly used for your own identification of the video.
            width: `width` is deprecated and no longer influences the output video's resolution.
            assets: Provide the assets for lip-sync. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
            start_seconds: The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Lip Sync API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.lip_sync.generate(
            assets={
                "audio_file_path": "path/to/audio.mp3",
                "video_file_path": "path/to/video.mp4",
                "video_source": "file",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            max_fps_limit=12.0,
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = AsyncFilesClient(base_client=self._base_client)

        # Upload audio file (always required)
        audio_file_path = assets["audio_file_path"]
        assets["audio_file_path"] = await file_client.upload_file(file=audio_file_path)

        # Upload video file if video_source is "file" and video_file_path is provided
        if (
            assets.get("video_source") == "file"
            and "video_file_path" in assets
            and assets["video_file_path"]
        ):
            video_file_path = assets["video_file_path"]
            assets["video_file_path"] = await file_client.upload_file(
                file=video_file_path
            )

        create_response = await self.create(
            assets=assets,
            end_seconds=end_seconds,
            start_seconds=start_seconds,
            height=height,
            max_fps_limit=max_fps_limit,
            name=name,
            width=width,
            request_options=request_options,
        )
        logger.info(f"Lip Sync response: {create_response}")

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
        assets: params.V1LipSyncCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        max_fps_limit: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1LipSyncCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        width: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1LipSyncCreateResponse:
        """
        Lip Sync

        Create a Lip Sync video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](https://magichour.ai/products/lip-sync).


        POST /v1/lip-sync

        Args:
            height: `height` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            max_fps_limit: Defines the maximum FPS (frames per second) for the output video. If the input video's FPS is lower than this limit, the output video will retain the input FPS. This is useful for reducing unnecessary frame usage in scenarios where high FPS is not required.
            name: The name of video. This value is mainly used for your own identification of the video.
            style: Attributes used to dictate the style of the output
            width: `width` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            assets: Provide the assets for lip-sync. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
            start_seconds: The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.lip_sync.create(
            assets={
                "audio_file_path": "api-assets/id/1234.mp3",
                "video_file_path": "api-assets/id/1234.mp4",
                "video_source": "file",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            max_fps_limit=12.0,
            name="Lip Sync video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "height": height,
                "max_fps_limit": max_fps_limit,
                "name": name,
                "style": style,
                "width": width,
                "assets": assets,
                "end_seconds": end_seconds,
                "start_seconds": start_seconds,
            },
            dump_with=params._SerializerV1LipSyncCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/lip-sync",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1LipSyncCreateResponse,
            request_options=request_options or default_request_options(),
        )
