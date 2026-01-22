import typing
import typing_extensions

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


class ImageToVideoClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1ImageToVideoGenerateBodyAssets,
        end_seconds: float,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "default",
                    "kling-1.6",
                    "kling-2.5-audio",
                    "seedance",
                    "sora-2",
                    "veo3.1",
                    "veo3.1-audio",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1ImageToVideoCreateBodyStyle], type_utils.NotGiven
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
        Generate image-to-video (alias for create with additional functionality).

        Create a Image To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Args:
            height: `height` is deprecated and no longer influences the output video's resolution.
            name: The name of video. This value is mainly used for your own identification of the video.
            resolution: Controls the output video resolution. Defaults to `720p` if not specified.
            style: Attributed used to dictate the style of the output
            width: `width` is deprecated and no longer influences the output video's resolution.
            assets: Provide the assets for image-to-video.
            end_seconds: The total duration of the output video in seconds.
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Image-to-Video API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.image_to_video.generate(
            assets={"image_file_path": "path/to/image.png"},
            end_seconds=5.0,
            resolution="720p",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = FilesClient(base_client=self._base_client)

        # Upload image file
        image_file_path = assets["image_file_path"]
        assets["image_file_path"] = file_client.upload_file(file=image_file_path)

        create_response = self.create(
            assets=assets,
            end_seconds=end_seconds,
            height=height,
            model=model,
            name=name,
            resolution=resolution,
            style=style,
            width=width,
            request_options=request_options,
        )
        logger.info(f"Image-to-Video response: {create_response}")

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
        assets: params.V1ImageToVideoCreateBodyAssets,
        end_seconds: float,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "default",
                    "kling-1.6",
                    "kling-2.5-audio",
                    "seedance",
                    "sora-2",
                    "veo3.1",
                    "veo3.1-audio",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1ImageToVideoCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        width: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1ImageToVideoCreateResponse:
        """
        Image-to-Video

        **What this API does**

        Create the same Image To Video you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding image to video into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a image to video job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/image-to-video).

        POST /v1/image-to-video

        Args:
            height: `height` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            model: The AI model to use for video generation.
        * `default`: Our recommended model for general use (Kling 2.5 Audio). Note: For backward compatibility, if you use default and end_seconds > 10, we'll fall back to Kling 1.6.
        * `seedance`: Great for fast iteration and start/end frame
        * `kling-2.5-audio`: Great for motion, action, and camera control
        * `sora-2`: Great for story-telling, dialogue & creativity
        * `veo3.1-audio`: Great for dialogue + SFX generated natively
        * `veo3.1`: Great for realism, polish, & prompt adherence
        * `kling-1.6`: Great for dependable clips with smooth motion
            name: Give your video a custom name for easy identification.
            resolution: Controls the output video resolution. Defaults to `720p` if not specified.

        * **Default**: Supports `480p`, `720p`, and `1080p`.
        * **Seedance**: Supports `480p`, `720p`, `1080p`.
        * **Kling 2.5 Audio**: Supports `720p`, `1080p`.
        * **Sora 2**: Supports `720p`.
        * **Veo 3.1 Audio**: Supports `720p`, `1080p`.
        * **Veo 3.1**: Supports `720p`, `1080p`.
        * **Kling 1.6**: Supports `720p`, `1080p`.
            style: Attributed used to dictate the style of the output
            width: `width` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            assets: Provide the assets for image-to-video. Sora 2 only supports images with an aspect ratio of `9:16` or `16:9`.
            end_seconds: The total duration of the output video in seconds.

        Supported durations depend on the chosen model:
        * **Default**: 5-60 seconds (either 5 or 10 for 480p).
        * **Seedance**: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        * **Kling 2.5 Audio**: 5, 10
        * **Sora 2**: 4, 8, 12, 24, 36, 48, 60
        * **Veo 3.1 Audio**: 4, 6, 8, 16, 24, 32, 40, 48, 56
        * **Veo 3.1**: 4, 6, 8, 16, 24, 32, 40, 48, 56
        * **Kling 1.6**: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.image_to_video.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            end_seconds=5.0,
            model="sora-2",
            name="My Image To Video video",
            resolution="720p",
        )
        ```
        """
        _json = to_encodable(
            item={
                "height": height,
                "model": model,
                "name": name,
                "resolution": resolution,
                "style": style,
                "width": width,
                "assets": assets,
                "end_seconds": end_seconds,
            },
            dump_with=params._SerializerV1ImageToVideoCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/image-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1ImageToVideoCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncImageToVideoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1ImageToVideoGenerateBodyAssets,
        end_seconds: float,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1ImageToVideoCreateBodyStyle], type_utils.NotGiven
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
        Generate image-to-video (alias for create with additional functionality).

        Create a Image To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Args:
            height: `height` is deprecated and no longer influences the output video's resolution.
            name: The name of video. This value is mainly used for your own identification of the video.
            resolution: Controls the output video resolution. Defaults to `720p` if not specified.
            style: Attributed used to dictate the style of the output
            width: `width` is deprecated and no longer influences the output video's resolution.
            assets: Provide the assets for image-to-video.
            end_seconds: The total duration of the output video in seconds.
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Image-to-Video API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.image_to_video.generate(
            assets={"image_file_path": "path/to/image.png"},
            end_seconds=5.0,
            resolution="720p",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = AsyncFilesClient(base_client=self._base_client)

        # Upload image file
        image_file_path = assets["image_file_path"]
        assets["image_file_path"] = await file_client.upload_file(file=image_file_path)

        create_response = await self.create(
            assets=assets,
            end_seconds=end_seconds,
            height=height,
            name=name,
            resolution=resolution,
            style=style,
            width=width,
            request_options=request_options,
        )
        logger.info(f"Image-to-Video response: {create_response}")

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
        assets: params.V1ImageToVideoCreateBodyAssets,
        end_seconds: float,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "default",
                    "kling-1.6",
                    "kling-2.5-audio",
                    "seedance",
                    "sora-2",
                    "veo3.1",
                    "veo3.1-audio",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1ImageToVideoCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        width: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1ImageToVideoCreateResponse:
        """
        Image-to-Video

        **What this API does**

        Create the same Image To Video you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding image to video into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a image to video job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/image-to-video).

        POST /v1/image-to-video

        Args:
            height: `height` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            model: The AI model to use for video generation.
        * `default`: Our recommended model for general use (Kling 2.5 Audio). Note: For backward compatibility, if you use default and end_seconds > 10, we'll fall back to Kling 1.6.
        * `seedance`: Great for fast iteration and start/end frame
        * `kling-2.5-audio`: Great for motion, action, and camera control
        * `sora-2`: Great for story-telling, dialogue & creativity
        * `veo3.1-audio`: Great for dialogue + SFX generated natively
        * `veo3.1`: Great for realism, polish, & prompt adherence
        * `kling-1.6`: Great for dependable clips with smooth motion
            name: Give your video a custom name for easy identification.
            resolution: Controls the output video resolution. Defaults to `720p` if not specified.

        * **Default**: Supports `480p`, `720p`, and `1080p`.
        * **Seedance**: Supports `480p`, `720p`, `1080p`.
        * **Kling 2.5 Audio**: Supports `720p`, `1080p`.
        * **Sora 2**: Supports `720p`.
        * **Veo 3.1 Audio**: Supports `720p`, `1080p`.
        * **Veo 3.1**: Supports `720p`, `1080p`.
        * **Kling 1.6**: Supports `720p`, `1080p`.
            style: Attributed used to dictate the style of the output
            width: `width` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            assets: Provide the assets for image-to-video. Sora 2 only supports images with an aspect ratio of `9:16` or `16:9`.
            end_seconds: The total duration of the output video in seconds.

        Supported durations depend on the chosen model:
        * **Default**: 5-60 seconds (either 5 or 10 for 480p).
        * **Seedance**: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        * **Kling 2.5 Audio**: 5, 10
        * **Sora 2**: 4, 8, 12, 24, 36, 48, 60
        * **Veo 3.1 Audio**: 4, 6, 8, 16, 24, 32, 40, 48, 56
        * **Veo 3.1**: 4, 6, 8, 16, 24, 32, 40, 48, 56
        * **Kling 1.6**: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.image_to_video.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            end_seconds=5.0,
            model="sora-2",
            name="My Image To Video video",
            resolution="720p",
        )
        ```
        """
        _json = to_encodable(
            item={
                "height": height,
                "model": model,
                "name": name,
                "resolution": resolution,
                "style": style,
                "width": width,
                "assets": assets,
                "end_seconds": end_seconds,
            },
            dump_with=params._SerializerV1ImageToVideoCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/image-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1ImageToVideoCreateResponse,
            request_options=request_options or default_request_options(),
        )
