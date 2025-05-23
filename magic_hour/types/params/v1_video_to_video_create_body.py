import pydantic
import typing
import typing_extensions

from .v1_video_to_video_create_body_assets import (
    V1VideoToVideoCreateBodyAssets,
    _SerializerV1VideoToVideoCreateBodyAssets,
)
from .v1_video_to_video_create_body_style import (
    V1VideoToVideoCreateBodyStyle,
    _SerializerV1VideoToVideoCreateBodyStyle,
)


class V1VideoToVideoCreateBody(typing_extensions.TypedDict):
    """
    V1VideoToVideoCreateBody
    """

    assets: typing_extensions.Required[V1VideoToVideoCreateBodyAssets]
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

    height: typing_extensions.NotRequired[int]
    """
    Used to determine the dimensions of the output video. 
      
    * If height is provided, width will also be required. The larger value between width and height will be used to determine the maximum output resolution while maintaining the original aspect ratio.
    * If both height and width are omitted, the video will be resized according to your subscription's maximum resolution, while preserving aspect ratio.
    
    Note: if the video's original resolution is less than the maximum, the video will not be resized.
    
    See our [pricing page](https://magichour.ai/pricing) for more details.
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of video
    """

    start_seconds: typing_extensions.Required[float]
    """
    The start time of the input video in seconds
    """

    style: typing_extensions.Required[V1VideoToVideoCreateBodyStyle]

    width: typing_extensions.NotRequired[int]
    """
    Used to determine the dimensions of the output video. 
      
    * If width is provided, height will also be required. The larger value between width and height will be used to determine the maximum output resolution while maintaining the original aspect ratio.
    * If both height and width are omitted, the video will be resized according to your subscription's maximum resolution, while preserving aspect ratio.
    
    Note: if the video's original resolution is less than the maximum, the video will not be resized.
    
    See our [pricing page](https://magichour.ai/pricing) for more details.
    """


class _SerializerV1VideoToVideoCreateBody(pydantic.BaseModel):
    """
    Serializer for V1VideoToVideoCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1VideoToVideoCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    fps_resolution: typing.Optional[typing_extensions.Literal["FULL", "HALF"]] = (
        pydantic.Field(alias="fps_resolution", default=None)
    )
    height: typing.Optional[int] = pydantic.Field(alias="height", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    start_seconds: float = pydantic.Field(
        alias="start_seconds",
    )
    style: _SerializerV1VideoToVideoCreateBodyStyle = pydantic.Field(
        alias="style",
    )
    width: typing.Optional[int] = pydantic.Field(alias="width", default=None)
