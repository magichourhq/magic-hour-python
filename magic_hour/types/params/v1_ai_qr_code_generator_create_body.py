import pydantic
import typing
import typing_extensions

from .v1_ai_qr_code_generator_create_body_style import (
    V1AiQrCodeGeneratorCreateBodyStyle,
    _SerializerV1AiQrCodeGeneratorCreateBodyStyle,
)


class V1AiQrCodeGeneratorCreateBody(typing_extensions.TypedDict):
    """
    V1AiQrCodeGeneratorCreateBody
    """

    content: typing_extensions.Required[str]
    """
    The content of the QR code.
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image. This value is mainly used for your own identification of the image.
    """

    style: typing_extensions.Required[V1AiQrCodeGeneratorCreateBodyStyle]


class _SerializerV1AiQrCodeGeneratorCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiQrCodeGeneratorCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    content: str = pydantic.Field(
        alias="content",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    style: _SerializerV1AiQrCodeGeneratorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
