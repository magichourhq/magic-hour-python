import typing

from magic_hour.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from magic_hour.types import models, params


class AiQrCodeGeneratorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

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
        AI QR Code

        Create an AI QR code. Each QR code costs 20 credits.

        POST /v1/ai-qr-code-generator

        Args:
            name: The name of image
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
        AI QR Code

        Create an AI QR code. Each QR code costs 20 credits.

        POST /v1/ai-qr-code-generator

        Args:
            name: The name of image
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
