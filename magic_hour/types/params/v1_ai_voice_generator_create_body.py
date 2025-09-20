import pydantic
import typing
import typing_extensions

from .v1_ai_voice_generator_create_body_style import (
    V1AiVoiceGeneratorCreateBodyStyle,
    _SerializerV1AiVoiceGeneratorCreateBodyStyle,
)


class V1AiVoiceGeneratorCreateBody(typing_extensions.TypedDict):
    """
    V1AiVoiceGeneratorCreateBody
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of audio. This value is mainly used for your own identification of the audio.
    """

    style: typing_extensions.Required[V1AiVoiceGeneratorCreateBodyStyle]
    """
    The content used to generate speech.
    """


class _SerializerV1AiVoiceGeneratorCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiVoiceGeneratorCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    style: _SerializerV1AiVoiceGeneratorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
