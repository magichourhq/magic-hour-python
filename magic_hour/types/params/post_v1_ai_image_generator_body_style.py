import pydantic
import typing_extensions


class PostV1AiImageGeneratorBodyStyle(typing_extensions.TypedDict):
    """
    PostV1AiImageGeneratorBodyStyle
    """

    prompt: typing_extensions.Required[str]
    """
    The prompt used for the image.
    """


class _SerializerPostV1AiImageGeneratorBodyStyle(pydantic.BaseModel):
    """
    Serializer for PostV1AiImageGeneratorBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: str = pydantic.Field(
        alias="prompt",
    )
