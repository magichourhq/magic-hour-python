import pydantic
import typing
import typing_extensions


class PostV1AiHeadshotGeneratorBodyStyle(typing_extensions.TypedDict):
    """
    PostV1AiHeadshotGeneratorBodyStyle
    """

    prompt: typing_extensions.NotRequired[str]
    """
    A prompt to guide the final image.
    """


class _SerializerPostV1AiHeadshotGeneratorBodyStyle(pydantic.BaseModel):
    """
    Serializer for PostV1AiHeadshotGeneratorBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: typing.Optional[str] = pydantic.Field(alias="prompt", default=None)
