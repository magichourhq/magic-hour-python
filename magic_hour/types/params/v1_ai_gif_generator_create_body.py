import pydantic
import typing
import typing_extensions

from .v1_ai_gif_generator_create_body_style import (
    V1AiGifGeneratorCreateBodyStyle,
    _SerializerV1AiGifGeneratorCreateBodyStyle,
)


class V1AiGifGeneratorCreateBody(typing_extensions.TypedDict):
    """
    V1AiGifGeneratorCreateBody
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of gif. This value is mainly used for your own identification of the gif.
    """

    output_format: typing_extensions.NotRequired[
        typing_extensions.Literal["gif", "mp4", "webm"]
    ]
    """
    The output file format for the generated animation.
    """

    style: typing_extensions.Required[V1AiGifGeneratorCreateBodyStyle]


class _SerializerV1AiGifGeneratorCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiGifGeneratorCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    output_format: typing.Optional[typing_extensions.Literal["gif", "mp4", "webm"]] = (
        pydantic.Field(alias="output_format", default=None)
    )
    style: _SerializerV1AiGifGeneratorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
