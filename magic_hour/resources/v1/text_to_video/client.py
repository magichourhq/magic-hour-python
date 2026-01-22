import typing
import typing_extensions

from magic_hour.helpers.logger import get_sdk_logger
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


class TextToVideoClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        end_seconds: float,
        orientation: typing_extensions.Literal["landscape", "portrait", "square"],
        style: params.V1TextToVideoCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate text-to-video (alias for create with additional functionality).

        Create a Text To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Args:
            name: The name of video. This value is mainly used for your own identification of the video.
            resolution: Controls the output video resolution. Defaults to `720p` if not specified.
            end_seconds: The total duration of the output video in seconds.
            orientation: Determines the orientation of the output video
            style: V1TextToVideoCreateBodyStyle
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Text-to-Video API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.text_to_video.generate(
            end_seconds=5.0,
            orientation="landscape",
            style={"prompt": "a dog running through a meadow"},
            resolution="720p",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        create_response = self.create(
            end_seconds=end_seconds,
            orientation=orientation,
            style=style,
            name=name,
            resolution=resolution,
            request_options=request_options,
        )
        logger.info(f"Text-to-Video response: {create_response}")

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
        end_seconds: float,
        style: params.V1TextToVideoCreateBodyStyle,
        aspect_ratio: typing.Union[
            typing.Optional[typing_extensions.Literal["16:9", "1:1", "9:16"]],
            type_utils.NotGiven,
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
        orientation: typing.Union[
            typing.Optional[
                typing_extensions.Literal["landscape", "portrait", "square"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1TextToVideoCreateResponse:
        """
        Text-to-Video

        **What this API does**

        Create the same Text To Video you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding text to video into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a text to video job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/text-to-video).

        POST /v1/text-to-video

        Args:
            aspect_ratio: Determines the aspect ratio of the output video.
        * **Seedance**: Supports `9:16`, `16:9`, `1:1`.
        * **Kling 2.5 Audio**: Supports `9:16`, `16:9`, `1:1`.
        * **Sora 2**: Supports `9:16`, `16:9`.
        * **Veo 3.1 Audio**: Supports `9:16`, `16:9`.
        * **Veo 3.1**: Supports `9:16`, `16:9`.
        * **Kling 1.6**: Supports `9:16`, `16:9`, `1:1`.
            model: The AI model to use for video generation.
        * `default`: Our recommended model for general use (Kling 2.5 Audio). Note: For backward compatibility, if you use default and end_seconds > 10, we'll fall back to Kling 1.6.
        * `seedance`: Great for fast iteration and start/end frame
        * `kling-2.5-audio`: Great for motion, action, and camera control
        * `sora-2`: Great for story-telling, dialogue & creativity
        * `veo3.1-audio`: Great for dialogue + SFX generated natively
        * `veo3.1`: Great for realism, polish, & prompt adherence
        * `kling-1.6`: Great for dependable clips with smooth motion
            name: Give your video a custom name for easy identification.
            orientation: Deprecated. Use `aspect_ratio` instead.
            resolution: Controls the output video resolution. Defaults to `720p` if not specified.

        * **Default**: Supports `480p`, `720p`, and `1080p`.
        * **Seedance**: Supports `480p`, `720p`, `1080p`.
        * **Kling 2.5 Audio**: Supports `720p`, `1080p`.
        * **Sora 2**: Supports `720p`.
        * **Veo 3.1 Audio**: Supports `720p`, `1080p`.
        * **Veo 3.1**: Supports `720p`, `1080p`.
        * **Kling 1.6**: Supports `720p`, `1080p`.
            end_seconds: The total duration of the output video in seconds.

        Supported durations depend on the chosen model:
        * **Default**: 5-60 seconds (either 5 or 10 for 480p).
        * **Seedance**: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        * **Kling 2.5 Audio**: 5, 10
        * **Sora 2**: 4, 8, 12, 24, 36, 48, 60
        * **Veo 3.1 Audio**: 4, 6, 8, 16, 24, 32, 40, 48, 56
        * **Veo 3.1**: 4, 6, 8, 16, 24, 32, 40, 48, 56
        * **Kling 1.6**: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60
            style: V1TextToVideoCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.text_to_video.create(
            end_seconds=5.0,
            style={"prompt": "a dog running"},
            aspect_ratio="16:9",
            model="sora-2",
            name="My Text To Video video",
            orientation="landscape",
            resolution="720p",
        )
        ```
        """
        _json = to_encodable(
            item={
                "aspect_ratio": aspect_ratio,
                "model": model,
                "name": name,
                "orientation": orientation,
                "resolution": resolution,
                "end_seconds": end_seconds,
                "style": style,
            },
            dump_with=params._SerializerV1TextToVideoCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/text-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1TextToVideoCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncTextToVideoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        end_seconds: float,
        orientation: typing_extensions.Literal["landscape", "portrait", "square"],
        style: params.V1TextToVideoCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate text-to-video (alias for create with additional functionality).

        Create a Text To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Args:
            name: The name of video. This value is mainly used for your own identification of the video.
            resolution: Controls the output video resolution. Defaults to `720p` if not specified.
            end_seconds: The total duration of the output video in seconds.
            orientation: Determines the orientation of the output video
            style: V1TextToVideoCreateBodyStyle
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Text-to-Video API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.text_to_video.generate(
            end_seconds=5.0,
            orientation="landscape",
            style={"prompt": "a dog running through a meadow"},
            resolution="720p",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        create_response = await self.create(
            end_seconds=end_seconds,
            orientation=orientation,
            style=style,
            name=name,
            resolution=resolution,
            request_options=request_options,
        )
        logger.info(f"Text-to-Video response: {create_response}")

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
        end_seconds: float,
        style: params.V1TextToVideoCreateBodyStyle,
        aspect_ratio: typing.Union[
            typing.Optional[typing_extensions.Literal["16:9", "1:1", "9:16"]],
            type_utils.NotGiven,
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
        orientation: typing.Union[
            typing.Optional[
                typing_extensions.Literal["landscape", "portrait", "square"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1TextToVideoCreateResponse:
        """
        Text-to-Video

        **What this API does**

        Create the same Text To Video you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding text to video into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a text to video job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/text-to-video).

        POST /v1/text-to-video

        Args:
            aspect_ratio: Determines the aspect ratio of the output video.
        * **Seedance**: Supports `9:16`, `16:9`, `1:1`.
        * **Kling 2.5 Audio**: Supports `9:16`, `16:9`, `1:1`.
        * **Sora 2**: Supports `9:16`, `16:9`.
        * **Veo 3.1 Audio**: Supports `9:16`, `16:9`.
        * **Veo 3.1**: Supports `9:16`, `16:9`.
        * **Kling 1.6**: Supports `9:16`, `16:9`, `1:1`.
            model: The AI model to use for video generation.
        * `default`: Our recommended model for general use (Kling 2.5 Audio). Note: For backward compatibility, if you use default and end_seconds > 10, we'll fall back to Kling 1.6.
        * `seedance`: Great for fast iteration and start/end frame
        * `kling-2.5-audio`: Great for motion, action, and camera control
        * `sora-2`: Great for story-telling, dialogue & creativity
        * `veo3.1-audio`: Great for dialogue + SFX generated natively
        * `veo3.1`: Great for realism, polish, & prompt adherence
        * `kling-1.6`: Great for dependable clips with smooth motion
            name: Give your video a custom name for easy identification.
            orientation: Deprecated. Use `aspect_ratio` instead.
            resolution: Controls the output video resolution. Defaults to `720p` if not specified.

        * **Default**: Supports `480p`, `720p`, and `1080p`.
        * **Seedance**: Supports `480p`, `720p`, `1080p`.
        * **Kling 2.5 Audio**: Supports `720p`, `1080p`.
        * **Sora 2**: Supports `720p`.
        * **Veo 3.1 Audio**: Supports `720p`, `1080p`.
        * **Veo 3.1**: Supports `720p`, `1080p`.
        * **Kling 1.6**: Supports `720p`, `1080p`.
            end_seconds: The total duration of the output video in seconds.

        Supported durations depend on the chosen model:
        * **Default**: 5-60 seconds (either 5 or 10 for 480p).
        * **Seedance**: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        * **Kling 2.5 Audio**: 5, 10
        * **Sora 2**: 4, 8, 12, 24, 36, 48, 60
        * **Veo 3.1 Audio**: 4, 6, 8, 16, 24, 32, 40, 48, 56
        * **Veo 3.1**: 4, 6, 8, 16, 24, 32, 40, 48, 56
        * **Kling 1.6**: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60
            style: V1TextToVideoCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.text_to_video.create(
            end_seconds=5.0,
            style={"prompt": "a dog running"},
            aspect_ratio="16:9",
            model="sora-2",
            name="My Text To Video video",
            orientation="landscape",
            resolution="720p",
        )
        ```
        """
        _json = to_encodable(
            item={
                "aspect_ratio": aspect_ratio,
                "model": model,
                "name": name,
                "orientation": orientation,
                "resolution": resolution,
                "end_seconds": end_seconds,
                "style": style,
            },
            dump_with=params._SerializerV1TextToVideoCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/text-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1TextToVideoCreateResponse,
            request_options=request_options or default_request_options(),
        )
