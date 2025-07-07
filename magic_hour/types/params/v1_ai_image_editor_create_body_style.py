import pydantic
import typing_extensions


class V1AiImageEditorCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1AiImageEditorCreateBodyStyle
    """

    prompt: typing_extensions.Required[str]
    """
    The prompt used to edit the image.
    """


class _SerializerV1AiImageEditorCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiImageEditorCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: str = pydantic.Field(
        alias="prompt",
    )
