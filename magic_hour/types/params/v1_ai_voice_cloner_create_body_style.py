import pydantic
import typing_extensions


class V1AiVoiceClonerCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1AiVoiceClonerCreateBodyStyle
    """

    prompt: typing_extensions.Required[str]
    """
    Text used to generate speech from the cloned voice. The character limit is 1000 characters.
    """


class _SerializerV1AiVoiceClonerCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiVoiceClonerCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: str = pydantic.Field(
        alias="prompt",
    )
