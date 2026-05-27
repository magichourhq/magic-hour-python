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


class AudioToVideoClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1AudioToVideoGenerateBodyAssets,
        end_seconds: float,
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
        style: typing.Union[
            typing.Optional[params.V1AudioToVideoCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate audio-to-video (alias for create with additional functionality).

        Create an Audio To Video video. Credits are only charged for the frames that actually render.

        Args:
            name: Give your video a custom name for easy identification.
            resolution: Output video resolution. Defaults to `720p` on paid tiers and `480p` on free tiers.
            start_seconds: Start time of your clip (seconds). Must be ≥ 0.
            style: Attributes used to dictate the style of the output
            assets: Provide the audio file and an optional reference image.
            end_seconds: End time of your clip (seconds). Must be greater than start_seconds.
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Audio-to-Video API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.audio_to_video.generate(
            assets={
                "audio_file_path": "path/to/audio.mp3",
                "image_file_path": "path/to/image.png",
            },
            end_seconds=15.0,
            name="My Audio To Video video",
            resolution="720p",
            start_seconds=0.0,
            wait_for_completion=True,
            download_outputs=True,
            download_directory=".",
        )
        ```
        """

        file_client = FilesClient(base_client=self._base_client)

        audio_file_path = assets["audio_file_path"]
        assets["audio_file_path"] = file_client.upload_file(file=audio_file_path)

        if "image_file_path" in assets and assets["image_file_path"]:
            image_file_path = assets["image_file_path"]
            assets["image_file_path"] = file_client.upload_file(file=image_file_path)

        create_response = self.create(
            assets=assets,
            end_seconds=end_seconds,
            name=name,
            resolution=resolution,
            start_seconds=start_seconds,
            style=style,
            request_options=request_options,
        )
        logger.info(f"Audio-to-Video response: {create_response}")

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
        assets: params.V1AudioToVideoCreateBodyAssets,
        end_seconds: float,
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
        style: typing.Union[
            typing.Optional[params.V1AudioToVideoCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AudioToVideoCreateResponse:
        """
        Audio-to-Video

        **What this API does**

        Create the same Audio To Video you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding audio to video into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a audio to video job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/audio-to-video).

        POST /v1/audio-to-video

        Args:
            name: Give your video a custom name for easy identification.
            resolution: Output video resolution. Defaults to `720p` on paid tiers and `480p` on free tiers.
            start_seconds: Start time of your clip (seconds). Must be ≥ 0.
            style: Attributes used to dictate the style of the output
            assets: Provide the audio file and an optional reference image.
            end_seconds: End time of your clip (seconds). Must be greater than start_seconds.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.audio_to_video.create(
            assets={
                "audio_file_path": "api-assets/id/1234.mp3",
                "image_file_path": "api-assets/id/1234.png",
            },
            end_seconds=15.0,
            name="My Audio To Video video",
            resolution="720p",
            start_seconds=0.0,
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "resolution": resolution,
                "start_seconds": start_seconds,
                "style": style,
                "assets": assets,
                "end_seconds": end_seconds,
            },
            dump_with=params._SerializerV1AudioToVideoCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/audio-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AudioToVideoCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAudioToVideoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1AudioToVideoGenerateBodyAssets,
        end_seconds: float,
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
        style: typing.Union[
            typing.Optional[params.V1AudioToVideoCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate audio-to-video (alias for create with additional functionality).

        Create an Audio To Video video. Credits are only charged for the frames that actually render.

        Args:
            name: Give your video a custom name for easy identification.
            resolution: Output video resolution. Defaults to `720p` on paid tiers and `480p` on free tiers.
            start_seconds: Start time of your clip (seconds). Must be ≥ 0.
            style: Attributes used to dictate the style of the output
            assets: Provide the audio file and an optional reference image.
            end_seconds: End time of your clip (seconds). Must be greater than start_seconds.
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Audio-to-Video API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.audio_to_video.generate(
            assets={
                "audio_file_path": "path/to/audio.mp3",
                "image_file_path": "path/to/image.png",
            },
            end_seconds=15.0,
            name="My Audio To Video video",
            resolution="720p",
            start_seconds=0.0,
            wait_for_completion=True,
            download_outputs=True,
            download_directory=".",
        )
        ```
        """

        file_client = AsyncFilesClient(base_client=self._base_client)

        audio_file_path = assets["audio_file_path"]
        assets["audio_file_path"] = await file_client.upload_file(file=audio_file_path)

        if "image_file_path" in assets and assets["image_file_path"]:
            image_file_path = assets["image_file_path"]
            assets["image_file_path"] = await file_client.upload_file(
                file=image_file_path
            )

        create_response = await self.create(
            assets=assets,
            end_seconds=end_seconds,
            name=name,
            resolution=resolution,
            start_seconds=start_seconds,
            style=style,
            request_options=request_options,
        )
        logger.info(f"Audio-to-Video response: {create_response}")

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
        assets: params.V1AudioToVideoCreateBodyAssets,
        end_seconds: float,
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
        style: typing.Union[
            typing.Optional[params.V1AudioToVideoCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AudioToVideoCreateResponse:
        """
        Audio-to-Video

        **What this API does**

        Create the same Audio To Video you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding audio to video into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a audio to video job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/audio-to-video).

        POST /v1/audio-to-video

        Args:
            name: Give your video a custom name for easy identification.
            resolution: Output video resolution. Defaults to `720p` on paid tiers and `480p` on free tiers.
            start_seconds: Start time of your clip (seconds). Must be ≥ 0.
            style: Attributes used to dictate the style of the output
            assets: Provide the audio file and an optional reference image.
            end_seconds: End time of your clip (seconds). Must be greater than start_seconds.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.audio_to_video.create(
            assets={
                "audio_file_path": "api-assets/id/1234.mp3",
                "image_file_path": "api-assets/id/1234.png",
            },
            end_seconds=15.0,
            name="My Audio To Video video",
            resolution="720p",
            start_seconds=0.0,
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "resolution": resolution,
                "start_seconds": start_seconds,
                "style": style,
                "assets": assets,
                "end_seconds": end_seconds,
            },
            dump_with=params._SerializerV1AudioToVideoCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/audio-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AudioToVideoCreateResponse,
            request_options=request_options or default_request_options(),
        )
