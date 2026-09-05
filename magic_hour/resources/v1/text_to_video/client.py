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
        audio: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
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
            download_directory=".",
        )
        ```
        """

        create_response = self.create(
            end_seconds=end_seconds,
            orientation=orientation,
            style=style,
            name=name,
            resolution=resolution,
            model=model,
            aspect_ratio=aspect_ratio,
            audio=audio,
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
        audio: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "default",
                    "gemini-omni-1.1",
                    "kling-1.6",
                    "kling-2.5",
                    "kling-2.5-audio",
                    "kling-2.6",
                    "kling-3.0",
                    "ltx-2",
                    "ltx-2.3",
                    "ltx-2.5",
                    "minimax-h3",
                    "seedance",
                    "seedance-1.5",
                    "seedance-2.0",
                    "seedance-2.0-mini",
                    "seedance-2.5",
                    "sora-2",
                    "veo3.1",
                    "veo3.1-audio",
                    "veo3.1-lite",
                    "wan-2.2",
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
            typing.Optional[
                typing_extensions.Literal["1080p", "360p", "480p", "4k", "720p"]
            ],
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

        * **`gemini-omni-1.1`**: Supports 16:9, 9:16.
        * **`kling-2.6`**: Supports 9:16, 16:9, 1:1.
        * **`kling-3.0`**: Supports 9:16, 16:9, 1:1.
        * **`ltx-2.3`**: Supports 9:16, 16:9, 1:1.
        * **`ltx-2.5`**: Supports 9:16, 16:9, 1:1.
        * **`minimax-h3`**: Supports 16:9, 9:16, 1:1.
        * **`seedance-1.5`**: Supports 9:16, 16:9, 1:1.
        * **`seedance-2.0`**: Supports 9:16, 16:9, 1:1.
        * **`seedance-2.0-mini`**: Supports 9:16, 16:9, 1:1.
        * **`seedance-2.5`**: Supports 9:16, 16:9, 1:1.
        * **`sora-2`**: Supports 9:16, 16:9.
        * **`veo3.1`**: Supports 9:16, 16:9.
        * **`veo3.1-lite`**: Supports 9:16, 16:9.
        * **`wan-2.2`**: Supports 9:16, 16:9, 1:1.

            audio: Whether to include audio in the video. Defaults to `false` if not specified.

        Audio support varies by model:
        * **`gemini-omni-1.1`**: Not supported
        * **`kling-2.6`**: Not supported
        * **`kling-3.0`**: Toggle-able: audio adds extra credits when enabled
        * **`ltx-2.3`**: Toggle-able: no additional credits for audio
        * **`ltx-2.5`**: Toggle-able: no additional credits for audio
        * **`minimax-h3`**: Toggle-able: no additional credits for audio
        * **`seedance-1.5`**: Toggle-able: audio adds extra credits when enabled
        * **`seedance-2.0`**: Toggle-able: no additional credits for audio
        * **`seedance-2.0-mini`**: Toggle-able: no additional credits for audio
        * **`seedance-2.5`**: Toggle-able: no additional credits for audio
        * **`sora-2`**: Toggle-able: no additional credits for audio
        * **`veo3.1`**: Toggle-able: audio adds extra credits when enabled
        * **`veo3.1-lite`**: Toggle-able: audio adds extra credits when enabled
        * **`wan-2.2`**: Not supported

            model: The AI model to use for video generation.

        * `default`: uses our currently recommended model for general use. For paid tiers, defaults to `kling-3.0`. For free tiers, it defaults to `ltx-2.5`.
        * `gemini-omni-1.1`: Best for precise short clips, first/last frames, and high-resolution output.
        * `kling-2.6`: Best for action, motion blur, and controlled camera moves.
        * `kling-3.0`: Best for cinematic stories, references, and optional audio.
        * `ltx-2.3`: Fastest for general scenes, long clips, audio, and rapid iteration.
        * `ltx-2.5`: Fastest for general scenes, long clips, audio, and rapid iteration.
        * `minimax-h3`: Great for reference-driven clips with native audio and longer durations.
        * `seedance-1.5`: Best for smooth, consistent motion with an end frame.
        * `seedance-2.0`: Best for reference-led clips with precise subject control.
        * `seedance-2.0-mini`: Faster reference-led clips with consistent motion and audio.
        * `seedance-2.5`: Best for premium realism, detail, and natural motion.
        * `sora-2`: Best for creative concepts and longer clips with audio.
        * `veo3.1`: Best for romantic interactions and expressive action, with realistic detail.
        * `veo3.1-lite`: Balanced realism and audio at a lower cost than Veo 3.1.
        * `wan-2.2`: Best for physical motion, action, and camera movement.

        If you specify the deprecated model value that includes the `-audio` suffix, this will be the same as included `audio` as `true`.
            name: Give your video a custom name for easy identification.
            orientation: Deprecated. Use `aspect_ratio` instead.
            resolution: Controls the output video resolution. Defaults to `720p` on paid tiers and `480p` on free tiers.

        * **`gemini-omni-1.1`**: Supports 360p, 720p, 1080p, 4k.
        * **`kling-2.6`**: Supports 720p, 1080p.
        * **`kling-3.0`**: Supports 720p, 1080p, 4k.
        * **`ltx-2.3`**: Supports 480p, 720p, 1080p.
        * **`ltx-2.5`**: Supports 480p, 720p, 1080p.
        * **`minimax-h3`**: Supports 480p, 720p, 1080p.
        * **`seedance-1.5`**: Supports 480p, 720p, 1080p.
        * **`seedance-2.0`**: Supports 480p, 720p.
        * **`seedance-2.0-mini`**: Supports 480p, 720p.
        * **`seedance-2.5`**: Supports 480p, 720p.
        * **`sora-2`**: Supports 720p.
        * **`veo3.1`**: Supports 720p, 1080p.
        * **`veo3.1-lite`**: Supports 720p, 1080p.
        * **`wan-2.2`**: Supports 480p, 720p, 1080p.

            end_seconds: The total duration of the output video in seconds. Supported durations depend on the chosen model:

        * **`gemini-omni-1.1`**: 3, 4, 5, 6, 7, 8, 9, 10
        * **`kling-2.6`**: 5, 10
        * **`kling-3.0`**: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
        * **`ltx-2.3`**: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30
        * **`ltx-2.5`**: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60
        * **`minimax-h3`**: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30
        * **`seedance-1.5`**: 4, 5, 6, 7, 8, 9, 10, 11, 12
        * **`seedance-2.0`**: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
        * **`seedance-2.0-mini`**: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
        * **`seedance-2.5`**: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
        * **`sora-2`**: 4, 8, 12, 24, 36, 48, 60
        * **`veo3.1`**: 4, 6, 8, 16, 24, 32, 40, 48, 56
        * **`veo3.1-lite`**: 4, 6, 8, 16, 24, 32, 40, 48, 56
        * **`wan-2.2`**: 3, 4, 5, 6, 7, 8, 9, 10, 15

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
            audio=True,
            model="kling-3.0",
            name="My Text To Video video",
            resolution="720p",
        )
        ```
        """
        _json = to_encodable(
            item={
                "aspect_ratio": aspect_ratio,
                "audio": audio,
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
        audio: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
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
            download_directory=".",
        )
        ```
        """

        create_response = await self.create(
            end_seconds=end_seconds,
            orientation=orientation,
            style=style,
            name=name,
            resolution=resolution,
            aspect_ratio=aspect_ratio,
            model=model,
            audio=audio,
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
        audio: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "default",
                    "gemini-omni-1.1",
                    "kling-1.6",
                    "kling-2.5",
                    "kling-2.5-audio",
                    "kling-2.6",
                    "kling-3.0",
                    "ltx-2",
                    "ltx-2.3",
                    "ltx-2.5",
                    "minimax-h3",
                    "seedance",
                    "seedance-1.5",
                    "seedance-2.0",
                    "seedance-2.0-mini",
                    "seedance-2.5",
                    "sora-2",
                    "veo3.1",
                    "veo3.1-audio",
                    "veo3.1-lite",
                    "wan-2.2",
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
            typing.Optional[
                typing_extensions.Literal["1080p", "360p", "480p", "4k", "720p"]
            ],
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

        * **`gemini-omni-1.1`**: Supports 16:9, 9:16.
        * **`kling-2.6`**: Supports 9:16, 16:9, 1:1.
        * **`kling-3.0`**: Supports 9:16, 16:9, 1:1.
        * **`ltx-2.3`**: Supports 9:16, 16:9, 1:1.
        * **`ltx-2.5`**: Supports 9:16, 16:9, 1:1.
        * **`minimax-h3`**: Supports 16:9, 9:16, 1:1.
        * **`seedance-1.5`**: Supports 9:16, 16:9, 1:1.
        * **`seedance-2.0`**: Supports 9:16, 16:9, 1:1.
        * **`seedance-2.0-mini`**: Supports 9:16, 16:9, 1:1.
        * **`seedance-2.5`**: Supports 9:16, 16:9, 1:1.
        * **`sora-2`**: Supports 9:16, 16:9.
        * **`veo3.1`**: Supports 9:16, 16:9.
        * **`veo3.1-lite`**: Supports 9:16, 16:9.
        * **`wan-2.2`**: Supports 9:16, 16:9, 1:1.

            audio: Whether to include audio in the video. Defaults to `false` if not specified.

        Audio support varies by model:
        * **`gemini-omni-1.1`**: Not supported
        * **`kling-2.6`**: Not supported
        * **`kling-3.0`**: Toggle-able: audio adds extra credits when enabled
        * **`ltx-2.3`**: Toggle-able: no additional credits for audio
        * **`ltx-2.5`**: Toggle-able: no additional credits for audio
        * **`minimax-h3`**: Toggle-able: no additional credits for audio
        * **`seedance-1.5`**: Toggle-able: audio adds extra credits when enabled
        * **`seedance-2.0`**: Toggle-able: no additional credits for audio
        * **`seedance-2.0-mini`**: Toggle-able: no additional credits for audio
        * **`seedance-2.5`**: Toggle-able: no additional credits for audio
        * **`sora-2`**: Toggle-able: no additional credits for audio
        * **`veo3.1`**: Toggle-able: audio adds extra credits when enabled
        * **`veo3.1-lite`**: Toggle-able: audio adds extra credits when enabled
        * **`wan-2.2`**: Not supported

            model: The AI model to use for video generation.

        * `default`: uses our currently recommended model for general use. For paid tiers, defaults to `kling-3.0`. For free tiers, it defaults to `ltx-2.5`.
        * `gemini-omni-1.1`: Best for precise short clips, first/last frames, and high-resolution output.
        * `kling-2.6`: Best for action, motion blur, and controlled camera moves.
        * `kling-3.0`: Best for cinematic stories, references, and optional audio.
        * `ltx-2.3`: Fastest for general scenes, long clips, audio, and rapid iteration.
        * `ltx-2.5`: Fastest for general scenes, long clips, audio, and rapid iteration.
        * `minimax-h3`: Great for reference-driven clips with native audio and longer durations.
        * `seedance-1.5`: Best for smooth, consistent motion with an end frame.
        * `seedance-2.0`: Best for reference-led clips with precise subject control.
        * `seedance-2.0-mini`: Faster reference-led clips with consistent motion and audio.
        * `seedance-2.5`: Best for premium realism, detail, and natural motion.
        * `sora-2`: Best for creative concepts and longer clips with audio.
        * `veo3.1`: Best for romantic interactions and expressive action, with realistic detail.
        * `veo3.1-lite`: Balanced realism and audio at a lower cost than Veo 3.1.
        * `wan-2.2`: Best for physical motion, action, and camera movement.

        If you specify the deprecated model value that includes the `-audio` suffix, this will be the same as included `audio` as `true`.
            name: Give your video a custom name for easy identification.
            orientation: Deprecated. Use `aspect_ratio` instead.
            resolution: Controls the output video resolution. Defaults to `720p` on paid tiers and `480p` on free tiers.

        * **`gemini-omni-1.1`**: Supports 360p, 720p, 1080p, 4k.
        * **`kling-2.6`**: Supports 720p, 1080p.
        * **`kling-3.0`**: Supports 720p, 1080p, 4k.
        * **`ltx-2.3`**: Supports 480p, 720p, 1080p.
        * **`ltx-2.5`**: Supports 480p, 720p, 1080p.
        * **`minimax-h3`**: Supports 480p, 720p, 1080p.
        * **`seedance-1.5`**: Supports 480p, 720p, 1080p.
        * **`seedance-2.0`**: Supports 480p, 720p.
        * **`seedance-2.0-mini`**: Supports 480p, 720p.
        * **`seedance-2.5`**: Supports 480p, 720p.
        * **`sora-2`**: Supports 720p.
        * **`veo3.1`**: Supports 720p, 1080p.
        * **`veo3.1-lite`**: Supports 720p, 1080p.
        * **`wan-2.2`**: Supports 480p, 720p, 1080p.

            end_seconds: The total duration of the output video in seconds. Supported durations depend on the chosen model:

        * **`gemini-omni-1.1`**: 3, 4, 5, 6, 7, 8, 9, 10
        * **`kling-2.6`**: 5, 10
        * **`kling-3.0`**: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
        * **`ltx-2.3`**: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30
        * **`ltx-2.5`**: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60
        * **`minimax-h3`**: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30
        * **`seedance-1.5`**: 4, 5, 6, 7, 8, 9, 10, 11, 12
        * **`seedance-2.0`**: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
        * **`seedance-2.0-mini`**: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
        * **`seedance-2.5`**: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
        * **`sora-2`**: 4, 8, 12, 24, 36, 48, 60
        * **`veo3.1`**: 4, 6, 8, 16, 24, 32, 40, 48, 56
        * **`veo3.1-lite`**: 4, 6, 8, 16, 24, 32, 40, 48, 56
        * **`wan-2.2`**: 3, 4, 5, 6, 7, 8, 9, 10, 15

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
            audio=True,
            model="kling-3.0",
            name="My Text To Video video",
            resolution="720p",
        )
        ```
        """
        _json = to_encodable(
            item={
                "aspect_ratio": aspect_ratio,
                "audio": audio,
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
