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


class AiVideoTranslatorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1AiVideoTranslatorGenerateBodyAssets,
        end_seconds: float,
        target_language: typing_extensions.Literal[
            "Afrikaans",
            "Arabic",
            "Bengali",
            "Bulgarian",
            "Catalan",
            "Chinese (Simplified)",
            "Chinese (Traditional)",
            "Croatian",
            "Czech",
            "Danish",
            "Dutch",
            "English",
            "Estonian",
            "Finnish",
            "French",
            "German",
            "Greek",
            "Gujarati",
            "Hebrew",
            "Hindi",
            "Hungarian",
            "Indonesian",
            "Italian",
            "Japanese",
            "Kannada",
            "Kazakh",
            "Korean",
            "Latvian",
            "Lithuanian",
            "Malay",
            "Malayalam",
            "Marathi",
            "Norwegian",
            "Persian",
            "Polish",
            "Portuguese",
            "Punjabi",
            "Romanian",
            "Russian",
            "Serbian",
            "Slovak",
            "Slovenian",
            "Spanish",
            "Swahili",
            "Swedish",
            "Tamil",
            "Telugu",
            "Thai",
            "Turkish",
            "Ukrainian",
            "Urdu",
            "Vietnamese",
            "Welsh",
        ],
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
        """Upload a video, create a translation job, and optionally wait and download.

        ``assets["video_file_path"]`` accepts a local path, URL, or uploaded asset path.
        """
        uploaded_assets: params.V1AiVideoTranslatorCreateBodyAssets = {
            "video_file_path": FilesClient(base_client=self._base_client).upload_file(
                file=assets["video_file_path"]
            ),
        }
        create_response = self.create(
            assets=uploaded_assets,
            end_seconds=end_seconds,
            target_language=target_language,
            name=name,
            resolution=resolution,
            start_seconds=start_seconds,
            request_options=request_options,
        )
        logger.info(f"AI Video Translator response: {create_response}")
        return VideoProjectsClient(base_client=self._base_client).check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

    def create(
        self,
        *,
        assets: params.V1AiVideoTranslatorCreateBodyAssets,
        end_seconds: float,
        target_language: typing_extensions.Literal[
            "Afrikaans",
            "Arabic",
            "Bengali",
            "Bulgarian",
            "Catalan",
            "Chinese (Simplified)",
            "Chinese (Traditional)",
            "Croatian",
            "Czech",
            "Danish",
            "Dutch",
            "English",
            "Estonian",
            "Finnish",
            "French",
            "German",
            "Greek",
            "Gujarati",
            "Hebrew",
            "Hindi",
            "Hungarian",
            "Indonesian",
            "Italian",
            "Japanese",
            "Kannada",
            "Kazakh",
            "Korean",
            "Latvian",
            "Lithuanian",
            "Malay",
            "Malayalam",
            "Marathi",
            "Norwegian",
            "Persian",
            "Polish",
            "Portuguese",
            "Punjabi",
            "Romanian",
            "Russian",
            "Serbian",
            "Slovak",
            "Slovenian",
            "Spanish",
            "Swahili",
            "Swedish",
            "Tamil",
            "Telugu",
            "Thai",
            "Turkish",
            "Ukrainian",
            "Urdu",
            "Vietnamese",
            "Welsh",
        ],
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
    ) -> models.V1AiVideoTranslatorCreateResponse:
        """
        AI Video Translator

        **What this API does**

        Create the same Video Translator you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding video translator into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a video translator job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/ai-video-translator).

        POST /v1/ai-video-translator

        Args:
            name: Give your video a custom name for easy identification.
            resolution: Output video resolution. Defaults to 480p. 720p and 1080p require a paid plan.
            start_seconds: Start time of your clip (seconds). Must be ≥ 0.
            assets: Source video for the translation job.
            end_seconds: End time of your clip (seconds). Must be greater than start_seconds. The clip must be 1-30 seconds long.
            target_language: Language to translate the video's speech into.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_video_translator.create(
            assets={"video_file_path": "api-assets/id/1234.mp4"},
            end_seconds=15.0,
            target_language="Spanish",
            name="My Video Translator video",
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
                "assets": assets,
                "end_seconds": end_seconds,
                "target_language": target_language,
            },
            dump_with=params._SerializerV1AiVideoTranslatorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-video-translator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVideoTranslatorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiVideoTranslatorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1AiVideoTranslatorGenerateBodyAssets,
        end_seconds: float,
        target_language: typing_extensions.Literal[
            "Afrikaans",
            "Arabic",
            "Bengali",
            "Bulgarian",
            "Catalan",
            "Chinese (Simplified)",
            "Chinese (Traditional)",
            "Croatian",
            "Czech",
            "Danish",
            "Dutch",
            "English",
            "Estonian",
            "Finnish",
            "French",
            "German",
            "Greek",
            "Gujarati",
            "Hebrew",
            "Hindi",
            "Hungarian",
            "Indonesian",
            "Italian",
            "Japanese",
            "Kannada",
            "Kazakh",
            "Korean",
            "Latvian",
            "Lithuanian",
            "Malay",
            "Malayalam",
            "Marathi",
            "Norwegian",
            "Persian",
            "Polish",
            "Portuguese",
            "Punjabi",
            "Romanian",
            "Russian",
            "Serbian",
            "Slovak",
            "Slovenian",
            "Spanish",
            "Swahili",
            "Swedish",
            "Tamil",
            "Telugu",
            "Thai",
            "Turkish",
            "Ukrainian",
            "Urdu",
            "Vietnamese",
            "Welsh",
        ],
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
        """Upload a video, create a translation job, and optionally wait and download.

        ``assets["video_file_path"]`` accepts a local path, URL, or uploaded asset path.
        """
        uploaded_assets: params.V1AiVideoTranslatorCreateBodyAssets = {
            "video_file_path": await AsyncFilesClient(
                base_client=self._base_client
            ).upload_file(file=assets["video_file_path"]),
        }
        create_response = await self.create(
            assets=uploaded_assets,
            end_seconds=end_seconds,
            target_language=target_language,
            name=name,
            resolution=resolution,
            start_seconds=start_seconds,
            request_options=request_options,
        )
        logger.info(f"AI Video Translator response: {create_response}")
        return await AsyncVideoProjectsClient(
            base_client=self._base_client
        ).check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

    async def create(
        self,
        *,
        assets: params.V1AiVideoTranslatorCreateBodyAssets,
        end_seconds: float,
        target_language: typing_extensions.Literal[
            "Afrikaans",
            "Arabic",
            "Bengali",
            "Bulgarian",
            "Catalan",
            "Chinese (Simplified)",
            "Chinese (Traditional)",
            "Croatian",
            "Czech",
            "Danish",
            "Dutch",
            "English",
            "Estonian",
            "Finnish",
            "French",
            "German",
            "Greek",
            "Gujarati",
            "Hebrew",
            "Hindi",
            "Hungarian",
            "Indonesian",
            "Italian",
            "Japanese",
            "Kannada",
            "Kazakh",
            "Korean",
            "Latvian",
            "Lithuanian",
            "Malay",
            "Malayalam",
            "Marathi",
            "Norwegian",
            "Persian",
            "Polish",
            "Portuguese",
            "Punjabi",
            "Romanian",
            "Russian",
            "Serbian",
            "Slovak",
            "Slovenian",
            "Spanish",
            "Swahili",
            "Swedish",
            "Tamil",
            "Telugu",
            "Thai",
            "Turkish",
            "Ukrainian",
            "Urdu",
            "Vietnamese",
            "Welsh",
        ],
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
    ) -> models.V1AiVideoTranslatorCreateResponse:
        """
        AI Video Translator

        **What this API does**

        Create the same Video Translator you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding video translator into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a video translator job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/ai-video-translator).

        POST /v1/ai-video-translator

        Args:
            name: Give your video a custom name for easy identification.
            resolution: Output video resolution. Defaults to 480p. 720p and 1080p require a paid plan.
            start_seconds: Start time of your clip (seconds). Must be ≥ 0.
            assets: Source video for the translation job.
            end_seconds: End time of your clip (seconds). Must be greater than start_seconds. The clip must be 1-30 seconds long.
            target_language: Language to translate the video's speech into.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_video_translator.create(
            assets={"video_file_path": "api-assets/id/1234.mp4"},
            end_seconds=15.0,
            target_language="Spanish",
            name="My Video Translator video",
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
                "assets": assets,
                "end_seconds": end_seconds,
                "target_language": target_language,
            },
            dump_with=params._SerializerV1AiVideoTranslatorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-video-translator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVideoTranslatorCreateResponse,
            request_options=request_options or default_request_options(),
        )
