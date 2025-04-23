import pydantic
import typing
import typing_extensions

from .v1_ai_gif_generator_create_body_style import (
    V1AiGifGeneratorCreateBodyStyle,
    _SerializerV1AiGifGeneratorCreateBodyStyle,
)


class V1AiGifGeneratorCreateBody(typing_extensions.TypedDict):
    """
    V1AiGifGeneratorCreateBody
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of gif
    """

    style: typing_extensions.Required[V1AiGifGeneratorCreateBodyStyle]


class _SerializerV1AiGifGeneratorCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiGifGeneratorCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    style: _SerializerV1AiGifGeneratorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
