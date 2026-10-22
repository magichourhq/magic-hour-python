import typing
import typing_extensions

from magic_hour.types import models, params
from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)


class AiVideoUpscalerClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.V1AiVideoUpscalerCreateBodyAssets,
        end_seconds: float,
        resolution: typing_extensions.Literal["1080p", "2k", "4k", "720p"],
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        start_seconds: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiVideoUpscalerCreateResponse:
        """
        AI Video Upscaler

        **What this API does**

        Create the same Video Upscaler you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding video upscaler into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a video upscaler job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: output size and plan requirements vary by workflow and model. Some workflows derive output size from the input video.
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are charged when the job is queued (`credits_charged` in the response). Tools billed per frame charge an estimate and settle to the frames that actually render once the job finishes; tools billed per second charge the final amount upfront. Failed jobs are refunded.

        For detailed examples, see the [product page](https://magichour.ai/products/video-upscaler).

        POST /v1/ai-video-upscaler

        Args:
            name: Give your video a custom name for easy identification.
            start_seconds: Start time of your clip (seconds). Must be ≥ 0.
            assets: Source video for the upscale job.
            end_seconds: End time of your clip (seconds). Must be greater than start_seconds.
            resolution: Output resolution. `720p` and `1080p` set the output's short side, `2k` and `4k` its long side; the aspect ratio is kept. Requires a paid plan.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_video_upscaler.create(
            assets={"video_file_path": "api-assets/id/1234.mp4"},
            end_seconds=5.0,
            resolution="1080p",
            name="My Video Upscaler video",
            start_seconds=0.0,
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "start_seconds": start_seconds,
                "assets": assets,
                "end_seconds": end_seconds,
                "resolution": resolution,
            },
            dump_with=params._SerializerV1AiVideoUpscalerCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-video-upscaler",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVideoUpscalerCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiVideoUpscalerClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.V1AiVideoUpscalerCreateBodyAssets,
        end_seconds: float,
        resolution: typing_extensions.Literal["1080p", "2k", "4k", "720p"],
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        start_seconds: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiVideoUpscalerCreateResponse:
        """
        AI Video Upscaler

        **What this API does**

        Create the same Video Upscaler you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding video upscaler into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a video upscaler job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: output size and plan requirements vary by workflow and model. Some workflows derive output size from the input video.
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are charged when the job is queued (`credits_charged` in the response). Tools billed per frame charge an estimate and settle to the frames that actually render once the job finishes; tools billed per second charge the final amount upfront. Failed jobs are refunded.

        For detailed examples, see the [product page](https://magichour.ai/products/video-upscaler).

        POST /v1/ai-video-upscaler

        Args:
            name: Give your video a custom name for easy identification.
            start_seconds: Start time of your clip (seconds). Must be ≥ 0.
            assets: Source video for the upscale job.
            end_seconds: End time of your clip (seconds). Must be greater than start_seconds.
            resolution: Output resolution. `720p` and `1080p` set the output's short side, `2k` and `4k` its long side; the aspect ratio is kept. Requires a paid plan.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_video_upscaler.create(
            assets={"video_file_path": "api-assets/id/1234.mp4"},
            end_seconds=5.0,
            resolution="1080p",
            name="My Video Upscaler video",
            start_seconds=0.0,
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "start_seconds": start_seconds,
                "assets": assets,
                "end_seconds": end_seconds,
                "resolution": resolution,
            },
            dump_with=params._SerializerV1AiVideoUpscalerCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-video-upscaler",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVideoUpscalerCreateResponse,
            request_options=request_options or default_request_options(),
        )
