import pydantic
import typing_extensions


class V1AiGifGeneratorCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1AiGifGeneratorCreateBodyStyle
    """

    prompt: typing_extensions.Required[str]
    """
    The prompt used for the GIF.
    """


class _SerializerV1AiGifGeneratorCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiGifGeneratorCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: str = pydantic.Field(
        alias="prompt",
    )
