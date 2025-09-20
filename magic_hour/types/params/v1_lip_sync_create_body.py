import pydantic
import typing
import typing_extensions

from .v1_lip_sync_create_body_assets import (
    V1LipSyncCreateBodyAssets,
    _SerializerV1LipSyncCreateBodyAssets,
)
from .v1_lip_sync_create_body_style import (
    V1LipSyncCreateBodyStyle,
    _SerializerV1LipSyncCreateBodyStyle,
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
    The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
    """

    height: typing_extensions.NotRequired[typing.Optional[int]]
    """
    `height` is deprecated and no longer influences the output video's resolution.
    
    Output resolution is determined by the **minimum** of:
    - The resolution of the input video
    - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.
    
    This field is retained only for backward compatibility and will be removed in a future release.
    """

    max_fps_limit: typing_extensions.NotRequired[float]
    """
    Defines the maximum FPS (frames per second) for the output video. If the input video's FPS is lower than this limit, the output video will retain the input FPS. This is useful for reducing unnecessary frame usage in scenarios where high FPS is not required.
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of video. This value is mainly used for your own identification of the video.
    """

    start_seconds: typing_extensions.Required[float]
    """
    The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
    """

    style: typing_extensions.NotRequired[V1LipSyncCreateBodyStyle]
    """
    Attributes used to dictate the style of the output
    """

    width: typing_extensions.NotRequired[typing.Optional[int]]
    """
    `width` is deprecated and no longer influences the output video's resolution.
    
    Output resolution is determined by the **minimum** of:
    - The resolution of the input video
    - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.
    
    This field is retained only for backward compatibility and will be removed in a future release.
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
    style: typing.Optional[_SerializerV1LipSyncCreateBodyStyle] = pydantic.Field(
        alias="style", default=None
    )
    width: typing.Optional[int] = pydantic.Field(alias="width", default=None)
