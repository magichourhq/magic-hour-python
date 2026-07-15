import pydantic
import typing_extensions


class V1AiVideoEditorCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1AiVideoEditorCreateBodyStyle
    """

    prompt: typing_extensions.Required[str]
    """
    The prompt used to edit the video.
    """


class _SerializerV1AiVideoEditorCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiVideoEditorCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: str = pydantic.Field(
        alias="prompt",
    )
