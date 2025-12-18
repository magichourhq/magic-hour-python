import typing

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


class AiQrCodeGeneratorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        content: str,
        style: params.V1AiQrCodeGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate QR code (alias for create with additional functionality).

        Create an AI QR code. Each QR code costs 5 credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            style: The art style to use for QR code generation
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the AI QR Code Generator API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.ai_qr_code_generator.generate(
            content="https://magichour.ai",
            style={"art_style": "Watercolor"},
            name="Artistic QR Code",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        create_response = self.create(
            content=content, style=style, name=name, request_options=request_options
        )
        logger.info(f"AI QR Code Generator response: {create_response}")

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
        content: str,
        style: params.V1AiQrCodeGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiQrCodeGeneratorCreateResponse:
        """
        AI QR Code Generator

        Create an AI QR code. Each QR code costs 0 credits.

        POST /v1/ai-qr-code-generator

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            content: The content of the QR code.
            style: V1AiQrCodeGeneratorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_qr_code_generator.create(
            content="https://magichour.ai",
            style={"art_style": "Watercolor"},
            name="Qr Code image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "content": content, "style": style},
            dump_with=params._SerializerV1AiQrCodeGeneratorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-qr-code-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiQrCodeGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiQrCodeGeneratorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        content: str,
        style: params.V1AiQrCodeGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate QR code (alias for create with additional functionality).

        Create an AI QR code. Each QR code costs 5 credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            style: The art style to use for QR code generation
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the AI QR Code Generator API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.ai_qr_code_generator.generate(
            content="https://magichour.ai",
            style={"art_style": "Watercolor"},
            name="Artistic QR Code",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        create_response = await self.create(
            content=content, style=style, name=name, request_options=request_options
        )
        logger.info(f"AI QR Code Generator response: {create_response}")

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
        content: str,
        style: params.V1AiQrCodeGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiQrCodeGeneratorCreateResponse:
        """
        AI QR Code Generator

        Create an AI QR code. Each QR code costs 0 credits.

        POST /v1/ai-qr-code-generator

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            content: The content of the QR code.
            style: V1AiQrCodeGeneratorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_qr_code_generator.create(
            content="https://magichour.ai",
            style={"art_style": "Watercolor"},
            name="Qr Code image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "content": content, "style": style},
            dump_with=params._SerializerV1AiQrCodeGeneratorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-qr-code-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiQrCodeGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )
