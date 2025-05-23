import pydantic
import typing
import typing_extensions

from .v1_ai_image_generator_create_body_style import (
    V1AiImageGeneratorCreateBodyStyle,
    _SerializerV1AiImageGeneratorCreateBodyStyle,
)


class V1AiImageGeneratorCreateBody(typing_extensions.TypedDict):
    """
    V1AiImageGeneratorCreateBody
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

    style: typing_extensions.Required[V1AiImageGeneratorCreateBodyStyle]


class _SerializerV1AiImageGeneratorCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiImageGeneratorCreateBody handling case conversions
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
    style: _SerializerV1AiImageGeneratorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
