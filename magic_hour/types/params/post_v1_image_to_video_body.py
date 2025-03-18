import pydantic
import typing
import typing_extensions

from .post_v1_image_to_video_body_assets import (
    PostV1ImageToVideoBodyAssets,
    _SerializerPostV1ImageToVideoBodyAssets,
)
from .post_v1_image_to_video_body_style import (
    PostV1ImageToVideoBodyStyle,
    _SerializerPostV1ImageToVideoBodyStyle,
)


class PostV1ImageToVideoBody(typing_extensions.TypedDict):
    """
    PostV1ImageToVideoBody
    """

    assets: typing_extensions.Required[PostV1ImageToVideoBodyAssets]
    """
    Provide the assets for image-to-video.
    """

    end_seconds: typing_extensions.Required[float]
    """
    The total duration of the output video in seconds.
    """

    height: typing_extensions.Required[int]
    """
    The height of the input video. This value will help determine the final orientation of the output video. The output video resolution may not match the input.
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of video
    """

    style: typing_extensions.Required[PostV1ImageToVideoBodyStyle]

    width: typing_extensions.Required[int]
    """
    The width of the input video. This value will help determine the final orientation of the output video. The output video resolution may not match the input.
    """


class _SerializerPostV1ImageToVideoBody(pydantic.BaseModel):
    """
    Serializer for PostV1ImageToVideoBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerPostV1ImageToVideoBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    height: int = pydantic.Field(
        alias="height",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    style: _SerializerPostV1ImageToVideoBodyStyle = pydantic.Field(
        alias="style",
    )
    width: int = pydantic.Field(
        alias="width",
    )
