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


class AiImageGeneratorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        image_count: int,
        orientation: typing_extensions.Literal["landscape", "portrait", "square"],
        style: params.V1AiImageGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate AI images (alias for create with additional functionality).

        Create AI images with text prompts. Each image costs 5 credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            image_count: Number of images to generate.
            orientation: The orientation of the output image(s).
            style: The art style to use for image generation.
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the AI Image Generator API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.ai_image_generator.generate(
            image_count=1,
            orientation="landscape",
            style={"prompt": "Cool image", "tool": "ai-anime-generator"},
            name="Generated Image",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        create_response = self.create(
            image_count=image_count,
            orientation=orientation,
            style=style,
            name=name,
            request_options=request_options,
        )
        logger.info(f"AI Image Generator response: {create_response}")

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
        image_count: int,
        orientation: typing_extensions.Literal["landscape", "portrait", "square"],
        style: params.V1AiImageGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiImageGeneratorCreateResponse:
        """
        AI Image Generator

        Create an AI image. Each standard image costs 5 credits. Pro quality images cost 30 credits.

        POST /v1/ai-image-generator

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            image_count: Number of images to generate.
            orientation: The orientation of the output image(s).
            style: The art style to use for image generation.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_image_generator.create(
            image_count=1,
            orientation="landscape",
            style={
                "prompt": "Cool image",
                "quality_mode": "standard",
                "tool": "ai-anime-generator",
            },
            name="Ai Image image",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "image_count": image_count,
                "orientation": orientation,
                "style": style,
            },
            dump_with=params._SerializerV1AiImageGeneratorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-image-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiImageGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiImageGeneratorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        image_count: int,
        orientation: typing_extensions.Literal["landscape", "portrait", "square"],
        style: params.V1AiImageGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate AI images (alias for create with additional functionality).

        Create AI images with text prompts. Each image costs 5 credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            image_count: Number of images to generate.
            orientation: The orientation of the output image(s).
            style: The art style to use for image generation.
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the AI Image Generator API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.ai_image_generator.generate(
            image_count=1,
            orientation="landscape",
            style={"prompt": "Cool image", "tool": "ai-anime-generator"},
            name="Generated Image",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        create_response = await self.create(
            image_count=image_count,
            orientation=orientation,
            style=style,
            name=name,
            request_options=request_options,
        )
        logger.info(f"AI Image Generator response: {create_response}")

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
        image_count: int,
        orientation: typing_extensions.Literal["landscape", "portrait", "square"],
        style: params.V1AiImageGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiImageGeneratorCreateResponse:
        """
        AI Image Generator

        Create an AI image. Each standard image costs 5 credits. Pro quality images cost 30 credits.

        POST /v1/ai-image-generator

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            image_count: Number of images to generate.
            orientation: The orientation of the output image(s).
            style: The art style to use for image generation.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_image_generator.create(
            image_count=1,
            orientation="landscape",
            style={
                "prompt": "Cool image",
                "quality_mode": "standard",
                "tool": "ai-anime-generator",
            },
            name="Ai Image image",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "image_count": image_count,
                "orientation": orientation,
                "style": style,
            },
            dump_with=params._SerializerV1AiImageGeneratorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-image-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiImageGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )
