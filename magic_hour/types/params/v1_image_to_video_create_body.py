import pydantic
import typing
import typing_extensions

from .v1_image_to_video_create_body_assets import (
    V1ImageToVideoCreateBodyAssets,
    _SerializerV1ImageToVideoCreateBodyAssets,
)
from .v1_image_to_video_create_body_style import (
    V1ImageToVideoCreateBodyStyle,
    _SerializerV1ImageToVideoCreateBodyStyle,
)


class V1ImageToVideoCreateBody(typing_extensions.TypedDict):
    """
    V1ImageToVideoCreateBody
    """

    assets: typing_extensions.Required[V1ImageToVideoCreateBodyAssets]
    """
    Provide the assets for image-to-video.
    """

    end_seconds: typing_extensions.Required[float]
    """
    The total duration of the output video in seconds.
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

    resolution: typing_extensions.NotRequired[
        typing_extensions.Literal["1080p", "480p", "720p"]
    ]
    """
    Controls the output video resolution. Defaults to `720p` if not specified.
    
    480p and 720p are available on Creator, Pro, or Business tiers. However, 1080p require Pro or Business tier.
    
    **Options:**
    - `480p` - Supports only 5 or 10 second videos. Output: 24fps. Cost: 120 credits per 5 seconds.
    - `720p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 300 credits per 5 seconds.
    - `1080p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 600 credits per 5 seconds.
    """

    style: typing_extensions.NotRequired[V1ImageToVideoCreateBodyStyle]
    """
    Attributed used to dictate the style of the output
    """

    width: typing_extensions.NotRequired[typing.Optional[int]]
    """
    `width` is deprecated and no longer influences the output video's resolution.
    
    Output resolution is determined by the **minimum** of:
    - The resolution of the input video
    - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.
    
    This field is retained only for backward compatibility and will be removed in a future release.
    """


class _SerializerV1ImageToVideoCreateBody(pydantic.BaseModel):
    """
    Serializer for V1ImageToVideoCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1ImageToVideoCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    height: typing.Optional[int] = pydantic.Field(alias="height", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    resolution: typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]] = (
        pydantic.Field(alias="resolution", default=None)
    )
    style: typing.Optional[_SerializerV1ImageToVideoCreateBodyStyle] = pydantic.Field(
        alias="style", default=None
    )
    width: typing.Optional[int] = pydantic.Field(alias="width", default=None)
