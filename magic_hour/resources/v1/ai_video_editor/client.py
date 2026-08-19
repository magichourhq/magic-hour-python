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


class AiVideoEditorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1AiVideoEditorGenerateBodyAssets,
        end_seconds: float,
        style: params.V1AiVideoEditorCreateBodyStyle,
        model: typing.Union[
            typing.Optional[typing_extensions.Literal["gemini-omni", "ltx-2.3"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        start_seconds: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate AI video editor video (alias for create with additional functionality).

        Create a Video Editor video. Credits are only charged for the frames that actually render.

        Args:
            name: Give your video a custom name for easy identification.
            start_seconds: Start time of your clip (seconds). Must be ≥ 0.
            assets: Provide the assets for video editing.
            end_seconds: End time of your clip in seconds. Must be greater than `start_seconds`. Duration must be between 3 and 10 seconds.
            style: V1AiVideoEditorCreateBodyStyle
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the AI Video Editor API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.ai_video_editor.generate(
            assets={"video_file_path": "path/to/video.mp4"},
            end_seconds=5.0,
            style={"prompt": "Change the car color to blue"},
            name="My Video Editor video",
            start_seconds=0.0,
            wait_for_completion=True,
            download_outputs=True,
            download_directory=".",
        )
        ```
        """

        file_client = FilesClient(base_client=self._base_client)

        video_file_path = assets["video_file_path"]
        assets["video_file_path"] = file_client.upload_file(file=video_file_path)

        create_response = self.create(
            assets=assets,
            end_seconds=end_seconds,
            style=style,
            name=name,
            start_seconds=start_seconds,
            request_options=request_options,
        )
        logger.info(f"AI Video Editor response: {create_response}")

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
        assets: params.V1AiVideoEditorCreateBodyAssets,
        end_seconds: float,
        style: params.V1AiVideoEditorCreateBodyStyle,
        model: typing.Union[
            typing.Optional[typing_extensions.Literal["gemini-omni", "ltx-2.3"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        start_seconds: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiVideoEditorCreateResponse:
        """
        AI Video Editor

        **What this API does**

        Create the same Video Editor you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding video editor into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a video editor job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/ai-video-editor).

        POST /v1/ai-video-editor

        Args:
            model: Editing model. Defaults to `ltx-2.3` for free tier and `gemini-omni` for paid. Use `ltx-2.3` for LTX video edit.
            name: Give your video a custom name for easy identification.
            resolution: Output resolution. Defaults to `480p` for free tier and `720p` for paid. Google Omni supports 720p only; LTX-2.3 supports 480p, 720p, and 1080p.
            start_seconds: Start time of your clip (seconds). Must be ≥ 0.
            assets: Provide the assets for video editing.
            end_seconds: End time of your clip in seconds. Must be greater than `start_seconds`. Minimum duration is 3 seconds. Maximum duration depends on model: `gemini-omni`: 10s, `ltx-2.3`: 45s.
            style: V1AiVideoEditorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_video_editor.create(
            assets={"video_file_path": "api-assets/id/1234.mp4"},
            end_seconds=5.0,
            style={"prompt": "Change the car color to blue"},
            model="gemini-omni",
            name="My Video Editor video",
            resolution="720p",
            start_seconds=0.0,
        )
        ```
        """
        _json = to_encodable(
            item={
                "model": model,
                "name": name,
                "resolution": resolution,
                "start_seconds": start_seconds,
                "assets": assets,
                "end_seconds": end_seconds,
                "style": style,
            },
            dump_with=params._SerializerV1AiVideoEditorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-video-editor",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVideoEditorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiVideoEditorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1AiVideoEditorGenerateBodyAssets,
        end_seconds: float,
        style: params.V1AiVideoEditorCreateBodyStyle,
        model: typing.Union[
            typing.Optional[typing_extensions.Literal["gemini-omni", "ltx-2.3"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        start_seconds: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate AI video editor video (alias for create with additional functionality).

        Create a Video Editor video. Credits are only charged for the frames that actually render.

        Args:
            name: Give your video a custom name for easy identification.
            start_seconds: Start time of your clip (seconds). Must be ≥ 0.
            assets: Provide the assets for video editing.
            end_seconds: End time of your clip in seconds. Must be greater than `start_seconds`. Duration must be between 3 and 10 seconds.
            style: V1AiVideoEditorCreateBodyStyle
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the AI Video Editor API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.ai_video_editor.generate(
            assets={"video_file_path": "path/to/video.mp4"},
            end_seconds=5.0,
            style={"prompt": "Change the car color to blue"},
            name="My Video Editor video",
            start_seconds=0.0,
            wait_for_completion=True,
            download_outputs=True,
            download_directory=".",
        )
        ```
        """

        file_client = AsyncFilesClient(base_client=self._base_client)

        video_file_path = assets["video_file_path"]
        assets["video_file_path"] = await file_client.upload_file(file=video_file_path)

        create_response = await self.create(
            assets=assets,
            end_seconds=end_seconds,
            style=style,
            name=name,
            start_seconds=start_seconds,
            request_options=request_options,
        )
        logger.info(f"AI Video Editor response: {create_response}")

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
        assets: params.V1AiVideoEditorCreateBodyAssets,
        end_seconds: float,
        style: params.V1AiVideoEditorCreateBodyStyle,
        model: typing.Union[
            typing.Optional[typing_extensions.Literal["gemini-omni", "ltx-2.3"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        start_seconds: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiVideoEditorCreateResponse:
        """
        AI Video Editor

        **What this API does**

        Create the same Video Editor you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding video editor into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a video editor job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/ai-video-editor).

        POST /v1/ai-video-editor

        Args:
            model: Editing model. Defaults to `ltx-2.3` for free tier and `gemini-omni` for paid. Use `ltx-2.3` for LTX video edit.
            name: Give your video a custom name for easy identification.
            resolution: Output resolution. Defaults to `480p` for free tier and `720p` for paid. Google Omni supports 720p only; LTX-2.3 supports 480p, 720p, and 1080p.
            start_seconds: Start time of your clip (seconds). Must be ≥ 0.
            assets: Provide the assets for video editing.
            end_seconds: End time of your clip in seconds. Must be greater than `start_seconds`. Minimum duration is 3 seconds. Maximum duration depends on model: `gemini-omni`: 10s, `ltx-2.3`: 45s.
            style: V1AiVideoEditorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_video_editor.create(
            assets={"video_file_path": "api-assets/id/1234.mp4"},
            end_seconds=5.0,
            style={"prompt": "Change the car color to blue"},
            model="gemini-omni",
            name="My Video Editor video",
            resolution="720p",
            start_seconds=0.0,
        )
        ```
        """
        _json = to_encodable(
            item={
                "model": model,
                "name": name,
                "resolution": resolution,
                "start_seconds": start_seconds,
                "assets": assets,
                "end_seconds": end_seconds,
                "style": style,
            },
            dump_with=params._SerializerV1AiVideoEditorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-video-editor",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVideoEditorCreateResponse,
            request_options=request_options or default_request_options(),
        )
