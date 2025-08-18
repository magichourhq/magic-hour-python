import pydantic
import typing
import typing_extensions

from .v1_image_background_remover_create_body_assets import (
    V1ImageBackgroundRemoverCreateBodyAssets,
    _SerializerV1ImageBackgroundRemoverCreateBodyAssets,
)


class V1ImageBackgroundRemoverCreateBody(typing_extensions.TypedDict):
    """
    V1ImageBackgroundRemoverCreateBody
    """

    assets: typing_extensions.Required[V1ImageBackgroundRemoverCreateBodyAssets]
    """
    Provide the assets for background removal
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image. This value is mainly used for your own identification of the image.
    """


class _SerializerV1ImageBackgroundRemoverCreateBody(pydantic.BaseModel):
    """
    Serializer for V1ImageBackgroundRemoverCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1ImageBackgroundRemoverCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
