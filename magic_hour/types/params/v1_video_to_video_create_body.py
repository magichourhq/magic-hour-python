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
    End time of your clip (seconds). Must be greater than start_seconds.
    """

    fps_resolution: typing_extensions.NotRequired[
        typing_extensions.Literal["FULL", "HALF"]
    ]
    """
    Determines whether the resulting video will have the same frame per second as the original video, or half.
    * `FULL` - the result video will have the same FPS as the input video
    * `HALF` - the result video will have half the FPS as the input video
    """

    height: typing_extensions.NotRequired[typing.Optional[int]]
    """
    `height` is deprecated and no longer influences the output video's resolution.
    
    This field is retained only for backward compatibility and will be removed in a future release.
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your video a custom name for easy identification.
    """

    start_seconds: typing_extensions.Required[float]
    """
    Start time of your clip (seconds). Must be ≥ 0.
    """

    style: typing_extensions.Required[V1VideoToVideoCreateBodyStyle]

    width: typing_extensions.NotRequired[typing.Optional[int]]
    """
    `width` is deprecated and no longer influences the output video's resolution.
    
    This field is retained only for backward compatibility and will be removed in a future release.
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
