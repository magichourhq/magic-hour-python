import pydantic
import typing
import typing_extensions

from .post_v1_image_background_remover_body_assets import (
    PostV1ImageBackgroundRemoverBodyAssets,
    _SerializerPostV1ImageBackgroundRemoverBodyAssets,
)


class PostV1ImageBackgroundRemoverBody(typing_extensions.TypedDict):
    """
    PostV1ImageBackgroundRemoverBody
    """

    assets: typing_extensions.Required[PostV1ImageBackgroundRemoverBodyAssets]
    """
    Provide the assets for background removal
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image
    """


class _SerializerPostV1ImageBackgroundRemoverBody(pydantic.BaseModel):
    """
    Serializer for PostV1ImageBackgroundRemoverBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerPostV1ImageBackgroundRemoverBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
