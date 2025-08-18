import pydantic
import typing
import typing_extensions

from .v1_ai_headshot_generator_create_body_assets import (
    V1AiHeadshotGeneratorCreateBodyAssets,
    _SerializerV1AiHeadshotGeneratorCreateBodyAssets,
)
from .v1_ai_headshot_generator_create_body_style import (
    V1AiHeadshotGeneratorCreateBodyStyle,
    _SerializerV1AiHeadshotGeneratorCreateBodyStyle,
)


class V1AiHeadshotGeneratorCreateBody(typing_extensions.TypedDict):
    """
    V1AiHeadshotGeneratorCreateBody
    """

    assets: typing_extensions.Required[V1AiHeadshotGeneratorCreateBodyAssets]
    """
    Provide the assets for headshot photo
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image. This value is mainly used for your own identification of the image.
    """

    style: typing_extensions.NotRequired[V1AiHeadshotGeneratorCreateBodyStyle]


class _SerializerV1AiHeadshotGeneratorCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiHeadshotGeneratorCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1AiHeadshotGeneratorCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    style: typing.Optional[_SerializerV1AiHeadshotGeneratorCreateBodyStyle] = (
        pydantic.Field(alias="style", default=None)
    )
