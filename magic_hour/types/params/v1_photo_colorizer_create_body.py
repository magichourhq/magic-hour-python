import pydantic
import typing
import typing_extensions

from .v1_photo_colorizer_create_body_assets import (
    V1PhotoColorizerCreateBodyAssets,
    _SerializerV1PhotoColorizerCreateBodyAssets,
)


class V1PhotoColorizerCreateBody(typing_extensions.TypedDict):
    """
    V1PhotoColorizerCreateBody
    """

    assets: typing_extensions.Required[V1PhotoColorizerCreateBodyAssets]
    """
    Provide the assets for photo colorization
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image. This value is mainly used for your own identification of the image.
    """


class _SerializerV1PhotoColorizerCreateBody(pydantic.BaseModel):
    """
    Serializer for V1PhotoColorizerCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1PhotoColorizerCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
