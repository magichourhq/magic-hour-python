import pydantic
import typing
import typing_extensions

from .v1_face_swap_create_body_assets import (
    V1FaceSwapCreateBodyAssets,
    _SerializerV1FaceSwapCreateBodyAssets,
)
from .v1_face_swap_create_body_style import (
    V1FaceSwapCreateBodyStyle,
    _SerializerV1FaceSwapCreateBodyStyle,
)


class V1FaceSwapCreateBody(typing_extensions.TypedDict):
    """
    V1FaceSwapCreateBody
    """

    assets: typing_extensions.Required[V1FaceSwapCreateBodyAssets]
    """
    Provide the assets for face swap. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
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

    name: typing_extensions.NotRequired[str]
    """
    The name of video. This value is mainly used for your own identification of the video.
    """

    start_seconds: typing_extensions.Required[float]
    """
    The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
    """

    style: typing_extensions.NotRequired[V1FaceSwapCreateBodyStyle]
    """
    Style of the face swap video.
    """

    width: typing_extensions.NotRequired[typing.Optional[int]]
    """
    `width` is deprecated and no longer influences the output video's resolution.
    
    Output resolution is determined by the **minimum** of:
    - The resolution of the input video
    - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.
    
    This field is retained only for backward compatibility and will be removed in a future release.
    """


class _SerializerV1FaceSwapCreateBody(pydantic.BaseModel):
    """
    Serializer for V1FaceSwapCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1FaceSwapCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    height: typing.Optional[int] = pydantic.Field(alias="height", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    start_seconds: float = pydantic.Field(
        alias="start_seconds",
    )
    style: typing.Optional[_SerializerV1FaceSwapCreateBodyStyle] = pydantic.Field(
        alias="style", default=None
    )
    width: typing.Optional[int] = pydantic.Field(alias="width", default=None)
