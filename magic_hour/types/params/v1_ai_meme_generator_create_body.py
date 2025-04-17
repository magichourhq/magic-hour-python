import pydantic
import typing
import typing_extensions

from .v1_ai_meme_generator_create_body_style import (
    V1AiMemeGeneratorCreateBodyStyle,
    _SerializerV1AiMemeGeneratorCreateBodyStyle,
)


class V1AiMemeGeneratorCreateBody(typing_extensions.TypedDict):
    """
    V1AiMemeGeneratorCreateBody
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of the meme.
    """

    style: typing_extensions.Required[V1AiMemeGeneratorCreateBodyStyle]


class _SerializerV1AiMemeGeneratorCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiMemeGeneratorCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    style: _SerializerV1AiMemeGeneratorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
