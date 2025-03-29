import pydantic
import typing_extensions


class V1AiImageGeneratorCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1AiImageGeneratorCreateBodyStyle
    """

    prompt: typing_extensions.Required[str]
    """
    The prompt used for the image.
    """


class _SerializerV1AiImageGeneratorCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiImageGeneratorCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: str = pydantic.Field(
        alias="prompt",
    )
