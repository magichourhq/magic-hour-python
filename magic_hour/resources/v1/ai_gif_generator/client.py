import typing
import typing_extensions

from magic_hour.helpers.logger import get_sdk_logger
from magic_hour.resources.v1.image_projects.client import (
    AsyncImageProjectsClient,
    ImageProjectsClient,
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


class AiGifGeneratorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        style: params.V1AiGifGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        output_format: typing.Union[
            typing.Optional[typing_extensions.Literal["gif", "mp4", "webm"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate GIF (alias for create with additional functionality).

        Create an AI GIF. Each GIF costs 5 credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            style: The art style to use for GIF generation
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the AI GIF Generator API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.ai_gif_generator.generate(
            style={"prompt": "Cute dancing cat, pixel art"},
            name="Dancing Cat GIF",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        create_response = self.create(
            style=style,
            name=name,
            output_format=output_format,
            request_options=request_options,
        )
        logger.info(f"AI GIF Generator response: {create_response}")

        image_projects_client = ImageProjectsClient(base_client=self._base_client)
        response = image_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

        return response

    def create(
        self,
        *,
        style: params.V1AiGifGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        output_format: typing.Union[
            typing.Optional[typing_extensions.Literal["gif", "mp4", "webm"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiGifGeneratorCreateResponse:
        """
        AI GIF Generator

        Create an AI GIF. Each GIF costs 50 credits.

        POST /v1/ai-gif-generator

        Args:
            name: The name of gif. This value is mainly used for your own identification of the gif.
            output_format: The output file format for the generated animation.
            style: V1AiGifGeneratorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_gif_generator.create(
            style={"prompt": "Cute dancing cat, pixel art"},
            name="Ai Gif gif",
            output_format="gif",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "output_format": output_format, "style": style},
            dump_with=params._SerializerV1AiGifGeneratorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-gif-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiGifGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiGifGeneratorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        style: params.V1AiGifGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate GIF (alias for create with additional functionality).

        Create an AI GIF. Each GIF costs 5 credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            style: The art style to use for GIF generation
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the AI GIF Generator API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.ai_gif_generator.generate(
            style={"prompt": "Cute dancing cat, pixel art"},
            name="Dancing Cat GIF",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        create_response = await self.create(
            style=style, name=name, request_options=request_options
        )
        logger.info(f"AI GIF Generator response: {create_response}")

        image_projects_client = AsyncImageProjectsClient(base_client=self._base_client)
        response = await image_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

        return response

    async def create(
        self,
        *,
        style: params.V1AiGifGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        output_format: typing.Union[
            typing.Optional[typing_extensions.Literal["gif", "mp4", "webm"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiGifGeneratorCreateResponse:
        """
        AI GIF Generator

        Create an AI GIF. Each GIF costs 50 credits.

        POST /v1/ai-gif-generator

        Args:
            name: The name of gif. This value is mainly used for your own identification of the gif.
            output_format: The output file format for the generated animation.
            style: V1AiGifGeneratorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_gif_generator.create(
            style={"prompt": "Cute dancing cat, pixel art"},
            name="Ai Gif gif",
            output_format="gif",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "output_format": output_format, "style": style},
            dump_with=params._SerializerV1AiGifGeneratorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-gif-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiGifGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )
