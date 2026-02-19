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
    Provide the assets for image-to-video. Sora 2 only supports images with an aspect ratio of `9:16` or `16:9`.
    """

    audio: typing_extensions.NotRequired[bool]
    """
    Whether to include audio in the video. Defaults to `false` if not specified.
    
    Audio support varies by model:
    * **`ltx-2`**: Automatically included with no extra credits
    * **`seedance`**: Not supported
    * **`kling-2.5`**: Automatically included with no extra credits
    * **`kling-3.0`**: Toggle-able (can enable/disable)
    * **`sora-2`**: Automatically included with no extra credits
    * **`veo3.1`**: Toggle-able (can enable/disable)
    
    * **`kling-1.6`**: Not supported
    """

    end_seconds: typing_extensions.Required[float]
    """
    The total duration of the output video in seconds. Supported durations depend on the chosen model:
    
    * **`ltx-2`**: 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30
    * **`seedance`**: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    * **`kling-2.5`**: 5, 10
    * **`kling-3.0`**: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
    * **`sora-2`**: 4, 8, 12, 24, 36, 48, 60
    * **`veo3.1`**: 4, 6, 8, 16, 24, 32, 40, 48, 56
    
    Legacy models:
    * **`kling-1.6`**: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60
    """

    height: typing_extensions.NotRequired[typing.Optional[int]]
    """
    `height` is deprecated and no longer influences the output video's resolution.
    
    This field is retained only for backward compatibility and will be removed in a future release.
    """

    model: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "default",
            "kling-1.6",
            "kling-2.5",
            "kling-2.5-audio",
            "kling-3.0",
            "ltx-2",
            "seedance",
            "sora-2",
            "veo3.1",
            "veo3.1-audio",
        ]
    ]
    """
    The AI model to use for video generation.
    
    * `default`: uses our currently recommended model for general use. For paid tiers, defaults to `kling-2.5`. For free tiers, it defaults to `ltx-2`.
    * `ltx-2`: Great for fast iteration with audio, lip-sync, and expressive faces
    * `seedance`: Great for fast iteration and start/end frame
    * `kling-2.5`: Great for motion, action, and camera control
    * `kling-3.0`: Great for cinematic, multi-scene storytelling with control
    * `sora-2`: Great for story-telling, dialogue & creativity
    * `veo3.1`: Great for realism, polish, & prompt adherence
    
    Legacy models:
    * `kling-1.6`: Great for dependable clips with smooth motion
    
    If you specify the deprecated model value that includes the `-audio` suffix, this will be the same as included `audio` as `true`.
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your video a custom name for easy identification.
    """

    resolution: typing_extensions.NotRequired[
        typing_extensions.Literal["1080p", "480p", "720p"]
    ]
    """
    Controls the output video resolution. Defaults to `720p` on paid tiers and `480p` on free tiers.
    
    * **`ltx-2`**: Supports 480p, 720p, 1080p.
    * **`seedance`**: Supports 480p, 720p, 1080p.
    * **`kling-2.5`**: Supports 720p, 1080p.
    * **`kling-3.0`**: Supports 720p, 1080p.
    * **`sora-2`**: Supports 720p.
    * **`veo3.1`**: Supports 720p, 1080p.
    
    * **`kling-1.6`**: Supports 720p, 1080p.
    """

    style: typing_extensions.NotRequired[V1ImageToVideoCreateBodyStyle]
    """
    Attributed used to dictate the style of the output
    """

    width: typing_extensions.NotRequired[typing.Optional[int]]
    """
    `width` is deprecated and no longer influences the output video's resolution.
    
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
    audio: typing.Optional[bool] = pydantic.Field(alias="audio", default=None)
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    height: typing.Optional[int] = pydantic.Field(alias="height", default=None)
    model: typing.Optional[
        typing_extensions.Literal[
            "default",
            "kling-1.6",
            "kling-2.5",
            "kling-2.5-audio",
            "kling-3.0",
            "ltx-2",
            "seedance",
            "sora-2",
            "veo3.1",
            "veo3.1-audio",
        ]
    ] = pydantic.Field(alias="model", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    resolution: typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]] = (
        pydantic.Field(alias="resolution", default=None)
    )
    style: typing.Optional[_SerializerV1ImageToVideoCreateBodyStyle] = pydantic.Field(
        alias="style", default=None
    )
    width: typing.Optional[int] = pydantic.Field(alias="width", default=None)
