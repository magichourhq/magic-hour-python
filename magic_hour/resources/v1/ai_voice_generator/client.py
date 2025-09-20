import typing

from magic_hour.helpers.logger import get_sdk_logger
from magic_hour.resources.v1.audio_projects.client import (
    AsyncAudioProjectsClient,
    AudioProjectsClient,
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


class AiVoiceGeneratorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        style: params.V1AiVoiceGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate AI voice (alias for create with additional functionality).

        Generate speech from text. Each character costs 0.05 credits. The cost is rounded up to the nearest whole number.

        Args:
            style: The content used to generate speech.
            name: The name of audio. This value is mainly used for your own identification of the audio.
            wait_for_completion: Whether to wait for the audio project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1AudioProjectsGetResponseWithDownloads: The response from the AI Voice Generator API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.ai_voice_generator.generate(
            style={"prompt": "Hello, how are you?", "voice_name": "Elon Musk"},
            name="Generated Voice",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        create_response = self.create(
            style=style,
            name=name,
            request_options=request_options,
        )
        logger.info(f"AI Voice Generator response: {create_response}")

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
        style: params.V1AiVoiceGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiVoiceGeneratorCreateResponse:
        """
        AI Voice Generator

        Generate speech from text. Each character costs 0.05 credits. The cost is rounded up to the nearest whole number.

        POST /v1/ai-voice-generator

        Args:
            name: The name of audio. This value is mainly used for your own identification of the audio.
            style: The content used to generate speech.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_voice_generator.create(
            style={"prompt": "Hello, how are you?", "voice_name": "Elon Musk"},
            name="Voice Generator audio",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "style": style},
            dump_with=params._SerializerV1AiVoiceGeneratorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-voice-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVoiceGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiVoiceGeneratorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        style: params.V1AiVoiceGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate AI voice (alias for create with additional functionality).

        Generate speech from text. Each character costs 0.05 credits. The cost is rounded up to the nearest whole number.

        Args:
            style: The content used to generate speech.
            name: The name of audio. This value is mainly used for your own identification of the audio.
            wait_for_completion: Whether to wait for the audio project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1AudioProjectsGetResponseWithDownloads: The response from the AI Voice Generator API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.ai_voice_generator.generate(
            style={"prompt": "Hello, how are you?", "voice_name": "Elon Musk"},
            name="Generated Voice",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        create_response = await self.create(
            style=style,
            name=name,
            request_options=request_options,
        )
        logger.info(f"AI Voice Generator response: {create_response}")

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
        style: params.V1AiVoiceGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiVoiceGeneratorCreateResponse:
        """
        AI Voice Generator

        Generate speech from text. Each character costs 0.05 credits. The cost is rounded up to the nearest whole number.

        POST /v1/ai-voice-generator

        Args:
            name: The name of audio. This value is mainly used for your own identification of the audio.
            style: The content used to generate speech.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_voice_generator.create(
            style={"prompt": "Hello, how are you?", "voice_name": "Elon Musk"},
            name="Voice Generator audio",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "style": style},
            dump_with=params._SerializerV1AiVoiceGeneratorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-voice-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVoiceGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )
