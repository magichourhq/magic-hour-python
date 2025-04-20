import pydantic
import typing
import typing_extensions

from .v1_lip_sync_create_body_assets import (
    V1LipSyncCreateBodyAssets,
    _SerializerV1LipSyncCreateBodyAssets,
)


class V1LipSyncCreateBody(typing_extensions.TypedDict):
    """
    V1LipSyncCreateBody
    """

    assets: typing_extensions.Required[V1LipSyncCreateBodyAssets]
    """
    Provide the assets for lip-sync. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
    """

    end_seconds: typing_extensions.Required[float]
    """
    The end time of the input video in seconds
    """

    height: typing_extensions.NotRequired[int]
    """
    Used to determine the dimensions of the output video. 
      
    * If height is provided, width will also be required. The larger value between width and height will be used to determine the maximum output resolution while maintaining the original aspect ratio.
    * If both height and width are omitted, the video will be resized according to your subscription's maximum resolution, while preserving aspect ratio.
    
    Note: if the video's original resolution is less than the maximum, the video will not be resized.
    
    See our [pricing page](https://magichour.ai/pricing) for more details.
    """

    max_fps_limit: typing_extensions.NotRequired[float]
    """
    Defines the maximum FPS (frames per second) for the output video. If the input video's FPS is lower than this limit, the output video will retain the input FPS. This is useful for reducing unnecessary frame usage in scenarios where high FPS is not required.
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of video
    """

    start_seconds: typing_extensions.Required[float]
    """
    The start time of the input video in seconds
    """

    width: typing_extensions.NotRequired[int]
    """
    Used to determine the dimensions of the output video. 
      
    * If width is provided, height will also be required. The larger value between width and height will be used to determine the maximum output resolution while maintaining the original aspect ratio.
    * If both height and width are omitted, the video will be resized according to your subscription's maximum resolution, while preserving aspect ratio.
    
    Note: if the video's original resolution is less than the maximum, the video will not be resized.
    
    See our [pricing page](https://magichour.ai/pricing) for more details.
    """


class _SerializerV1LipSyncCreateBody(pydantic.BaseModel):
    """
    Serializer for V1LipSyncCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1LipSyncCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    height: typing.Optional[int] = pydantic.Field(alias="height", default=None)
    max_fps_limit: typing.Optional[float] = pydantic.Field(
        alias="max_fps_limit", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    start_seconds: float = pydantic.Field(
        alias="start_seconds",
    )
    width: typing.Optional[int] = pydantic.Field(alias="width", default=None)
