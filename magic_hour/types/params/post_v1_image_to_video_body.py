"""
Generated by Sideko (sideko.dev)
"""

import typing
import typing_extensions
import pydantic

from .post_v1_image_to_video_body_assets import (
    PostV1ImageToVideoBodyAssets,
    _SerializerPostV1ImageToVideoBodyAssets,
)
from .post_v1_image_to_video_body_style import (
    PostV1ImageToVideoBodyStyle,
    _SerializerPostV1ImageToVideoBodyStyle,
)


class PostV1ImageToVideoBody(typing_extensions.TypedDict):
    """ """

    assets: typing_extensions.Required[PostV1ImageToVideoBodyAssets]
    end_seconds: typing_extensions.Required[float]
    height: typing_extensions.Required[float]
    name: typing.Optional[str]
    style: typing_extensions.Required[PostV1ImageToVideoBodyStyle]
    width: typing_extensions.Required[float]


class _SerializerPostV1ImageToVideoBody(pydantic.BaseModel):
    """
    Serializer for PostV1ImageToVideoBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerPostV1ImageToVideoBodyAssets = pydantic.Field(alias="assets")
    end_seconds: float = pydantic.Field(alias="end_seconds")
    height: float = pydantic.Field(alias="height")
    name: typing.Optional[str] = pydantic.Field(alias="name")
    style: _SerializerPostV1ImageToVideoBodyStyle = pydantic.Field(alias="style")
    width: float = pydantic.Field(alias="width")
