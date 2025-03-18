import pydantic
import typing
import typing_extensions

from .post_v1_ai_image_upscaler_body_assets import (
    PostV1AiImageUpscalerBodyAssets,
    _SerializerPostV1AiImageUpscalerBodyAssets,
)
from .post_v1_ai_image_upscaler_body_style import (
    PostV1AiImageUpscalerBodyStyle,
    _SerializerPostV1AiImageUpscalerBodyStyle,
)


class PostV1AiImageUpscalerBody(typing_extensions.TypedDict):
    """
    PostV1AiImageUpscalerBody
    """

    assets: typing_extensions.Required[PostV1AiImageUpscalerBodyAssets]
    """
    Provide the assets for upscaling
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image
    """

    scale_factor: typing_extensions.Required[float]
    """
    How much to scale the image. Must be either 2 or 4
    """

    style: typing_extensions.Required[PostV1AiImageUpscalerBodyStyle]


class _SerializerPostV1AiImageUpscalerBody(pydantic.BaseModel):
    """
    Serializer for PostV1AiImageUpscalerBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerPostV1AiImageUpscalerBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    scale_factor: float = pydantic.Field(
        alias="scale_factor",
    )
    style: _SerializerPostV1AiImageUpscalerBodyStyle = pydantic.Field(
        alias="style",
    )
