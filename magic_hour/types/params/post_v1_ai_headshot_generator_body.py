import pydantic
import typing
import typing_extensions

from .post_v1_ai_headshot_generator_body_assets import (
    PostV1AiHeadshotGeneratorBodyAssets,
    _SerializerPostV1AiHeadshotGeneratorBodyAssets,
)
from .post_v1_ai_headshot_generator_body_style import (
    PostV1AiHeadshotGeneratorBodyStyle,
    _SerializerPostV1AiHeadshotGeneratorBodyStyle,
)


class PostV1AiHeadshotGeneratorBody(typing_extensions.TypedDict):
    """
    PostV1AiHeadshotGeneratorBody
    """

    assets: typing_extensions.Required[PostV1AiHeadshotGeneratorBodyAssets]
    """
    Provide the assets for headshot photo
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image
    """

    style: typing_extensions.NotRequired[PostV1AiHeadshotGeneratorBodyStyle]


class _SerializerPostV1AiHeadshotGeneratorBody(pydantic.BaseModel):
    """
    Serializer for PostV1AiHeadshotGeneratorBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerPostV1AiHeadshotGeneratorBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    style: typing.Optional[_SerializerPostV1AiHeadshotGeneratorBodyStyle] = (
        pydantic.Field(alias="style", default=None)
    )
