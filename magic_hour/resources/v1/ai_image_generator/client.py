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
        style: params.V1AiImageGeneratorCreateBodyStyle,
        aspect_ratio: typing.Union[
            typing.Optional[typing_extensions.Literal["16:9", "1:1", "9:16"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "default",
                    "flux-schnell",
                    "nano-banana-pro",
                    "seedream",
                    "z-image-turbo",
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
            typing.Optional[typing_extensions.Literal["2k", "4k", "auto"]],
            type_utils.NotGiven,
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
            aspect_ratio="1:1",
            model="default",
            style={"prompt": "Cool image", "tool": "ai-anime-generator"},
            name="Generated Image",
            wait_for_completion=True,
            download_outputs=True,
            download_directory=".",
        )
        ```
        """

        create_response = self.create(
            image_count=image_count,
            style=style,
            aspect_ratio=aspect_ratio,
            model=model,
            orientation=orientation,
            resolution=resolution,
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
        style: params.V1AiImageGeneratorCreateBodyStyle,
        aspect_ratio: typing.Union[
            typing.Optional[typing_extensions.Literal["16:9", "1:1", "9:16"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "default",
                    "flux-schnell",
                    "nano-banana-pro",
                    "seedream",
                    "z-image-turbo",
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
            typing.Optional[typing_extensions.Literal["2k", "4k", "auto"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiImageGeneratorCreateResponse:
        """
        AI Image Generator

        Create an AI image with advanced model selection and quality controls.

        POST /v1/ai-image-generator

        Args:
            aspect_ratio: The aspect ratio of the output image(s). If not specified, defaults to `1:1` (square).
            model: The AI model to use for image generation. Each model has different capabilities and costs.

        **Models:**
        - `default` - Use the model we recommend, which will change over time. This is recommended unless you need a specific model. This is the default behavior.
        - `flux-schnell` - 5 credits/image
          - Supported resolutions: auto
          - Available for tiers: free, creator, pro, business
          - Image count allowed: 1, 2, 3, 4
        - `z-image-turbo` - 5 credits/image
          - Supported resolutions: auto, 2k
          - Available for tiers: free, creator, pro, business
          - Image count allowed: 1, 2, 3, 4
        - `seedream` - 30 credits/image
          - Supported resolutions: auto, 2k, 4k
          - Available for tiers: free, creator, pro, business
          - Image count allowed: 1, 2, 3, 4
        - `nano-banana-pro` - 150 credits/image
          - Supported resolutions: auto
          - Available for tiers: creator, pro, business
          - Image count allowed: 1, 4, 9, 16

            name: Give your image a custom name for easy identification.
            orientation: DEPRECATED: Use `aspect_ratio` instead.

        The orientation of the output image(s). `aspect_ratio` takes precedence when `orientation` if both are provided.
            resolution: Maximum resolution for the generated image.

        **Options:**
        - `auto` - Automatic resolution (all tiers, default)
        - `2k` - Up to 2048px (requires Pro or Business tier)
        - `4k` - Up to 4096px (requires Business tier)

        Note: Resolution availability depends on the model and your subscription tier. See `model` field for which resolutions each model supports. Defaults to `auto` if not specified.
            image_count: Number of images to generate. Maximum varies by model.
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
            style={"prompt": "Cool image", "tool": "ai-anime-generator"},
            aspect_ratio="1:1",
            model="default",
            name="My Ai Image image",
            resolution="auto",
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
                "image_count": image_count,
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
            download_directory=".",
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
        style: params.V1AiImageGeneratorCreateBodyStyle,
        aspect_ratio: typing.Union[
            typing.Optional[typing_extensions.Literal["16:9", "1:1", "9:16"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "default",
                    "flux-schnell",
                    "nano-banana-pro",
                    "seedream",
                    "z-image-turbo",
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
            typing.Optional[typing_extensions.Literal["2k", "4k", "auto"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiImageGeneratorCreateResponse:
        """
        AI Image Generator

        Create an AI image with advanced model selection and quality controls.

        POST /v1/ai-image-generator

        Args:
            aspect_ratio: The aspect ratio of the output image(s). If not specified, defaults to `1:1` (square).
            model: The AI model to use for image generation. Each model has different capabilities and costs.

        **Models:**
        - `default` - Use the model we recommend, which will change over time. This is recommended unless you need a specific model. This is the default behavior.
        - `flux-schnell` - 5 credits/image
          - Supported resolutions: auto
          - Available for tiers: free, creator, pro, business
          - Image count allowed: 1, 2, 3, 4
        - `z-image-turbo` - 5 credits/image
          - Supported resolutions: auto, 2k
          - Available for tiers: free, creator, pro, business
          - Image count allowed: 1, 2, 3, 4
        - `seedream` - 30 credits/image
          - Supported resolutions: auto, 2k, 4k
          - Available for tiers: free, creator, pro, business
          - Image count allowed: 1, 2, 3, 4
        - `nano-banana-pro` - 150 credits/image
          - Supported resolutions: auto
          - Available for tiers: creator, pro, business
          - Image count allowed: 1, 4, 9, 16

            name: Give your image a custom name for easy identification.
            orientation: DEPRECATED: Use `aspect_ratio` instead.

        The orientation of the output image(s). `aspect_ratio` takes precedence when `orientation` if both are provided.
            resolution: Maximum resolution for the generated image.

        **Options:**
        - `auto` - Automatic resolution (all tiers, default)
        - `2k` - Up to 2048px (requires Pro or Business tier)
        - `4k` - Up to 4096px (requires Business tier)

        Note: Resolution availability depends on the model and your subscription tier. See `model` field for which resolutions each model supports. Defaults to `auto` if not specified.
            image_count: Number of images to generate. Maximum varies by model.
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
            style={"prompt": "Cool image", "tool": "ai-anime-generator"},
            aspect_ratio="1:1",
            model="default",
            name="My Ai Image image",
            resolution="auto",
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
                "image_count": image_count,
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
