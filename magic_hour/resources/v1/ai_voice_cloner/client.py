import typing

from magic_hour.helpers.logger import get_sdk_logger
from magic_hour.resources.v1.audio_projects.client import (
    AsyncAudioProjectsClient,
    AudioProjectsClient,
)
from magic_hour.resources.v1.files.client import AsyncFilesClient, FilesClient
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


class AiVoiceClonerClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1AiVoiceClonerGenerateBodyAssets,
        style: params.V1AiVoiceClonerCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate cloned voice audio (alias for create with additional functionality).

        Clone a voice from an audio sample and generate speech with automatic file upload,
        completion waiting, and output downloading.

        Args:
            assets: Provide the assets for voice cloning (local file paths will be auto-uploaded)
            style: Voice cloning style parameters including the text prompt
            name: The name of audio. This value is mainly used for your own identification of the audio.
            wait_for_completion: Whether to wait for the audio project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1AudioProjectsGetResponseWithDownloads: The response from the AI Voice Cloner API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.ai_voice_cloner.generate(
            assets={"audio_file_path": "path/to/voice_sample.mp3"},
            style={"prompt": "Hello, this is my cloned voice speaking."},
            name="Cloned Voice Audio",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = FilesClient(base_client=self._base_client)

        audio_file_path = assets["audio_file_path"]
        assets["audio_file_path"] = file_client.upload_file(file=audio_file_path)

        create_response = self.create(
            assets=assets,
            style=style,
            name=name,
            request_options=request_options,
        )
        logger.info(f"AI Voice Cloner response: {create_response}")

        audio_projects_client = AudioProjectsClient(base_client=self._base_client)
        response = audio_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

        return response

    def create(
        self,
        *,
        assets: params.V1AiVoiceClonerCreateBodyAssets,
        style: params.V1AiVoiceClonerCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiVoiceClonerCreateResponse:
        """
        AI Voice Cloner

        Clone a voice from an audio sample and generate speech.
        * Each character costs 0.05 credits.
        * The cost is rounded up to the nearest whole number

        POST /v1/ai-voice-cloner

        Args:
            name: Give your audio a custom name for easy identification.
            assets: Provide the assets for voice cloning.
            style: V1AiVoiceClonerCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_voice_cloner.create(
            assets={"audio_file_path": "api-assets/id/1234.mp3"},
            style={"prompt": "Hello, this is my cloned voice."},
            name="My Voice Cloner audio",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets, "style": style},
            dump_with=params._SerializerV1AiVoiceClonerCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-voice-cloner",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVoiceClonerCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiVoiceClonerClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1AiVoiceClonerGenerateBodyAssets,
        style: params.V1AiVoiceClonerCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate cloned voice audio (alias for create with additional functionality).

        Clone a voice from an audio sample and generate speech with automatic file upload,
        completion waiting, and output downloading.

        Args:
            assets: Provide the assets for voice cloning (local file paths will be auto-uploaded)
            style: Voice cloning style parameters including the text prompt
            name: The name of audio. This value is mainly used for your own identification of the audio.
            wait_for_completion: Whether to wait for the audio project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1AudioProjectsGetResponseWithDownloads: The response from the AI Voice Cloner API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.ai_voice_cloner.generate(
            assets={"audio_file_path": "path/to/voice_sample.mp3"},
            style={"prompt": "Hello, this is my cloned voice speaking."},
            name="Cloned Voice Audio",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = AsyncFilesClient(base_client=self._base_client)

        audio_file_path = assets["audio_file_path"]
        assets["audio_file_path"] = await file_client.upload_file(file=audio_file_path)

        create_response = await self.create(
            assets=assets,
            style=style,
            name=name,
            request_options=request_options,
        )
        logger.info(f"AI Voice Cloner response: {create_response}")

        audio_projects_client = AsyncAudioProjectsClient(base_client=self._base_client)
        response = await audio_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

        return response

    async def create(
        self,
        *,
        assets: params.V1AiVoiceClonerCreateBodyAssets,
        style: params.V1AiVoiceClonerCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiVoiceClonerCreateResponse:
        """
        AI Voice Cloner

        Clone a voice from an audio sample and generate speech.
        * Each character costs 0.05 credits.
        * The cost is rounded up to the nearest whole number

        POST /v1/ai-voice-cloner

        Args:
            name: Give your audio a custom name for easy identification.
            assets: Provide the assets for voice cloning.
            style: V1AiVoiceClonerCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_voice_cloner.create(
            assets={"audio_file_path": "api-assets/id/1234.mp3"},
            style={"prompt": "Hello, this is my cloned voice."},
            name="My Voice Cloner audio",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets, "style": style},
            dump_with=params._SerializerV1AiVoiceClonerCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-voice-cloner",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVoiceClonerCreateResponse,
            request_options=request_options or default_request_options(),
        )
