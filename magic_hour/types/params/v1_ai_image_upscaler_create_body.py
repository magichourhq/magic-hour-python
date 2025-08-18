import pydantic
import typing
import typing_extensions

from .v1_ai_image_upscaler_create_body_assets import (
    V1AiImageUpscalerCreateBodyAssets,
    _SerializerV1AiImageUpscalerCreateBodyAssets,
)
from .v1_ai_image_upscaler_create_body_style import (
    V1AiImageUpscalerCreateBodyStyle,
    _SerializerV1AiImageUpscalerCreateBodyStyle,
)


class V1AiImageUpscalerCreateBody(typing_extensions.TypedDict):
    """
    V1AiImageUpscalerCreateBody
    """

    assets: typing_extensions.Required[V1AiImageUpscalerCreateBodyAssets]
    """
    Provide the assets for upscaling
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image. This value is mainly used for your own identification of the image.
    """

    scale_factor: typing_extensions.Required[float]
    """
    How much to scale the image. Must be either 2 or 4.
                
    Note: 4x upscale is only available on Creator, Pro, or Business tier.
    """

    style: typing_extensions.Required[V1AiImageUpscalerCreateBodyStyle]


class _SerializerV1AiImageUpscalerCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiImageUpscalerCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1AiImageUpscalerCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    scale_factor: float = pydantic.Field(
        alias="scale_factor",
    )
    style: _SerializerV1AiImageUpscalerCreateBodyStyle = pydantic.Field(
        alias="style",
    )
