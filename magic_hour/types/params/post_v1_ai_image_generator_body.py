import pydantic
import typing
import typing_extensions

from .post_v1_ai_image_generator_body_style import (
    PostV1AiImageGeneratorBodyStyle,
    _SerializerPostV1AiImageGeneratorBodyStyle,
)


class PostV1AiImageGeneratorBody(typing_extensions.TypedDict):
    """
    PostV1AiImageGeneratorBody
    """

    image_count: typing_extensions.Required[int]
    """
    number to images to generate
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image
    """

    orientation: typing_extensions.Required[
        typing_extensions.Literal["landscape", "portrait", "square"]
    ]

    style: typing_extensions.Required[PostV1AiImageGeneratorBodyStyle]


class _SerializerPostV1AiImageGeneratorBody(pydantic.BaseModel):
    """
    Serializer for PostV1AiImageGeneratorBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    image_count: int = pydantic.Field(
        alias="image_count",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    orientation: typing_extensions.Literal["landscape", "portrait", "square"] = (
        pydantic.Field(
            alias="orientation",
        )
    )
    style: _SerializerPostV1AiImageGeneratorBodyStyle = pydantic.Field(
        alias="style",
    )
