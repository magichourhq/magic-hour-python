import pydantic
import typing
import typing_extensions


class V1AiMusicGeneratorCreateBodyStyle(typing_extensions.TypedDict, total=False):
    """
    V1AiMusicGeneratorCreateBodyStyle
    """

    instrumental: typing_extensions.NotRequired[bool]
    """
    Generate music without vocals. When true, lyrics is ignored.
    """

    lyrics: typing_extensions.NotRequired[str]
    """
    Custom lyrics. Omit or leave blank for AI-generated lyrics when instrumental is false.
    """

    prompt: typing_extensions.Required[str]
    """
    Describe the song, including genre, mood, and instruments.
    """


class _SerializerV1AiMusicGeneratorCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiMusicGeneratorCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    instrumental: typing.Optional[bool] = pydantic.Field(
        alias="instrumental", default=None
    )
    lyrics: typing.Optional[str] = pydantic.Field(alias="lyrics", default=None)
    prompt: str = pydantic.Field(
        alias="prompt",
    )
