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


class FaceSwapClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1FaceSwapGenerateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1FaceSwapCreateBodyStyle], type_utils.NotGiven
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
        Generate face swap video (alias for create with additional functionality).

        Create a Face Swap video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Args:
            height: `height` is deprecated and no longer influences the output video's resolution.
            name: The name of video. This value is mainly used for your own identification of the video.
            width: `width` is deprecated and no longer influences the output video's resolution.
            assets: Provide the assets for face swap. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
            start_seconds: The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Face Swap API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.face_swap.generate(
            assets={
                "face_swap_mode": "all-faces",
                "video_file_path": "path/to/video.mp4",
                "video_source": "file",
                "image_file_path": "path/to/image.png",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = FilesClient(base_client=self._base_client)

        # Upload image file if provided (required for all-faces mode)
        if "image_file_path" in assets and assets["image_file_path"]:
            image_file_path = assets["image_file_path"]
            assets["image_file_path"] = file_client.upload_file(file=image_file_path)

        # Upload video file if video_source is "file" and video_file_path is provided
        if (
            assets.get("video_source") == "file"
            and "video_file_path" in assets
            and assets["video_file_path"]
        ):
            video_file_path = assets["video_file_path"]
            assets["video_file_path"] = file_client.upload_file(file=video_file_path)

        # Upload face mappings if present
        if "face_mappings" in assets and assets["face_mappings"]:
            for face_mapping in assets["face_mappings"]:
                if "new_face" in face_mapping and face_mapping["new_face"]:
                    new_face_file_path = face_mapping["new_face"]
                    face_mapping["new_face"] = file_client.upload_file(
                        file=new_face_file_path
                    )

        create_response = self.create(
            assets=assets,
            end_seconds=end_seconds,
            start_seconds=start_seconds,
            height=height,
            name=name,
            style=style,
            width=width,
            request_options=request_options,
        )
        logger.info(f"Face Swap response: {create_response}")

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
        assets: params.V1FaceSwapCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1FaceSwapCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        width: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1FaceSwapCreateResponse:
        """
        Face Swap Video

        Create a Face Swap video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](https://magichour.ai/products/face-swap).


        POST /v1/face-swap

        Args:
            height: `height` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            name: The name of video. This value is mainly used for your own identification of the video.
            style: Style of the face swap video.
            width: `width` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            assets: Provide the assets for face swap. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
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
        client.v1.face_swap.create(
            assets={
                "face_mappings": [
                    {
                        "new_face": "api-assets/id/1234.png",
                        "original_face": "api-assets/id/0-0.png",
                    }
                ],
                "face_swap_mode": "all-faces",
                "image_file_path": "image/id/1234.png",
                "video_file_path": "api-assets/id/1234.mp4",
                "video_source": "file",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            name="Face Swap video",
            style={"version": "default"},
        )
        ```
        """
        _json = to_encodable(
            item={
                "height": height,
                "name": name,
                "style": style,
                "width": width,
                "assets": assets,
                "end_seconds": end_seconds,
                "start_seconds": start_seconds,
            },
            dump_with=params._SerializerV1FaceSwapCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/face-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1FaceSwapCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncFaceSwapClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1FaceSwapGenerateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1FaceSwapCreateBodyStyle], type_utils.NotGiven
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
        Generate face swap video (alias for create with additional functionality).

        Create a Face Swap video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Args:
            height: `height` is deprecated and no longer influences the output video's resolution.
            name: The name of video. This value is mainly used for your own identification of the video.
            width: `width` is deprecated and no longer influences the output video's resolution.
            assets: Provide the assets for face swap. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
            start_seconds: The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Face Swap API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.face_swap.generate(
            assets={
                "face_swap_mode": "all-faces",
                "video_file_path": "path/to/video.mp4",
                "video_source": "file",
                "image_file_path": "path/to/image.png",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = AsyncFilesClient(base_client=self._base_client)

        # Upload image file if provided (required for all-faces mode)
        if "image_file_path" in assets and assets["image_file_path"]:
            image_file_path = assets["image_file_path"]
            assets["image_file_path"] = await file_client.upload_file(
                file=image_file_path
            )

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

        # Upload face mappings if present
        if "face_mappings" in assets and assets["face_mappings"]:
            for face_mapping in assets["face_mappings"]:
                if "new_face" in face_mapping and face_mapping["new_face"]:
                    new_face_file_path = face_mapping["new_face"]
                    face_mapping["new_face"] = await file_client.upload_file(
                        file=new_face_file_path
                    )

        create_response = await self.create(
            assets=assets,
            end_seconds=end_seconds,
            start_seconds=start_seconds,
            height=height,
            name=name,
            style=style,
            width=width,
            request_options=request_options,
        )
        logger.info(f"Face Swap response: {create_response}")

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
        assets: params.V1FaceSwapCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1FaceSwapCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        width: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1FaceSwapCreateResponse:
        """
        Face Swap Video

        Create a Face Swap video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](https://magichour.ai/products/face-swap).


        POST /v1/face-swap

        Args:
            height: `height` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            name: The name of video. This value is mainly used for your own identification of the video.
            style: Style of the face swap video.
            width: `width` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            assets: Provide the assets for face swap. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
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
        await client.v1.face_swap.create(
            assets={
                "face_mappings": [
                    {
                        "new_face": "api-assets/id/1234.png",
                        "original_face": "api-assets/id/0-0.png",
                    }
                ],
                "face_swap_mode": "all-faces",
                "image_file_path": "image/id/1234.png",
                "video_file_path": "api-assets/id/1234.mp4",
                "video_source": "file",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            name="Face Swap video",
            style={"version": "default"},
        )
        ```
        """
        _json = to_encodable(
            item={
                "height": height,
                "name": name,
                "style": style,
                "width": width,
                "assets": assets,
                "end_seconds": end_seconds,
                "start_seconds": start_seconds,
            },
            dump_with=params._SerializerV1FaceSwapCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/face-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1FaceSwapCreateResponse,
            request_options=request_options or default_request_options(),
        )
