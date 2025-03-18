import pydantic
import typing
import typing_extensions

from .post_v1_ai_qr_code_generator_body_style import (
    PostV1AiQrCodeGeneratorBodyStyle,
    _SerializerPostV1AiQrCodeGeneratorBodyStyle,
)


class PostV1AiQrCodeGeneratorBody(typing_extensions.TypedDict):
    """
    PostV1AiQrCodeGeneratorBody
    """

    content: typing_extensions.Required[str]
    """
    The content of the QR code.
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image
    """

    style: typing_extensions.Required[PostV1AiQrCodeGeneratorBodyStyle]


class _SerializerPostV1AiQrCodeGeneratorBody(pydantic.BaseModel):
    """
    Serializer for PostV1AiQrCodeGeneratorBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    content: str = pydantic.Field(
        alias="content",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    style: _SerializerPostV1AiQrCodeGeneratorBodyStyle = pydantic.Field(
        alias="style",
    )
