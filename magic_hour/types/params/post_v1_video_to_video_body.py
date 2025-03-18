import pydantic
import typing
import typing_extensions

from .post_v1_video_to_video_body_assets import (
    PostV1VideoToVideoBodyAssets,
    _SerializerPostV1VideoToVideoBodyAssets,
)
from .post_v1_video_to_video_body_style import (
    PostV1VideoToVideoBodyStyle,
    _SerializerPostV1VideoToVideoBodyStyle,
)


class PostV1VideoToVideoBody(typing_extensions.TypedDict):
    """
    PostV1VideoToVideoBody
    """

    assets: typing_extensions.Required[PostV1VideoToVideoBodyAssets]
    """
    Provide the assets for video-to-video. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
    """

    end_seconds: typing_extensions.Required[float]
    """
    The end time of the input video in seconds
    """

    fps_resolution: typing_extensions.NotRequired[
        typing_extensions.Literal["FULL", "HALF"]
    ]
    """
    Determines whether the resulting video will have the same frame per second as the original video, or half. 
    * `FULL` - the result video will have the same FPS as the input video
    * `HALF` - the result video will have half the FPS as the input video
    """

    height: typing_extensions.Required[int]
    """
    The height of the final output video. Must be divisible by 64. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of video
    """

    start_seconds: typing_extensions.Required[float]
    """
    The start time of the input video in seconds
    """

    style: typing_extensions.Required[PostV1VideoToVideoBodyStyle]

    width: typing_extensions.Required[int]
    """
    The width of the final output video. Must be divisible by 64. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
    """


class _SerializerPostV1VideoToVideoBody(pydantic.BaseModel):
    """
    Serializer for PostV1VideoToVideoBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerPostV1VideoToVideoBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    fps_resolution: typing.Optional[typing_extensions.Literal["FULL", "HALF"]] = (
        pydantic.Field(alias="fps_resolution", default=None)
    )
    height: int = pydantic.Field(
        alias="height",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    start_seconds: float = pydantic.Field(
        alias="start_seconds",
    )
    style: _SerializerPostV1VideoToVideoBodyStyle = pydantic.Field(
        alias="style",
    )
    width: int = pydantic.Field(
        alias="width",
    )
