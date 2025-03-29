import pydantic
import typing
import typing_extensions


class V1AiHeadshotGeneratorCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1AiHeadshotGeneratorCreateBodyStyle
    """

    prompt: typing_extensions.NotRequired[str]
    """
    A prompt to guide the final image.
    """


class _SerializerV1AiHeadshotGeneratorCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiHeadshotGeneratorCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: typing.Optional[str] = pydantic.Field(alias="prompt", default=None)
