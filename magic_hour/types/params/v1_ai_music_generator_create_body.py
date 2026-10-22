import pydantic
import typing
import typing_extensions

from .v1_ai_music_generator_create_body_style import (
    V1AiMusicGeneratorCreateBodyStyle,
    _SerializerV1AiMusicGeneratorCreateBodyStyle,
)


class V1AiMusicGeneratorCreateBody(typing_extensions.TypedDict, total=False):
    """
    V1AiMusicGeneratorCreateBody
    """

    duration: typing_extensions.Required[int]
    """
    Requested track duration in seconds, from 15 to 300. Determines credits charged.
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your audio a custom name for easy identification.
    """

    style: typing_extensions.Required[V1AiMusicGeneratorCreateBodyStyle]


class _SerializerV1AiMusicGeneratorCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiMusicGeneratorCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    duration: int = pydantic.Field(
        alias="duration",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    style: _SerializerV1AiMusicGeneratorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
