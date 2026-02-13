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
    * **seedance**: Not supported
    * **kling-2.5**: Always included (cannot be disabled)
    * **kling-3.0**: Toggle-able (can enable/disable)
    * **sora-2**: Always included (cannot be disabled)
    * **veo3.1**: Toggle-able (can enable/disable)
    * **kling-1.6**: Not supported
    """

    end_seconds: typing_extensions.Required[float]
    """
    The total duration of the output video in seconds.
    
    Supported durations depend on the chosen model:
    * **Default**: 5-60 seconds (2-12 seconds for 480p).
    * **seedance**: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    * **kling-2.5**: 5, 10
    * **kling-3.0**: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
    * **sora-2**: 4, 8, 12, 24, 36, 48, 60
    * **veo3.1**: 4, 6, 8, 16, 24, 32, 40, 48, 56
    * **kling-1.6**: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60
    """

    height: typing_extensions.NotRequired[typing.Optional[int]]
    """
    `height` is deprecated and no longer influences the output video's resolution.
    
    Output resolution is determined by the **minimum** of:
    - The resolution of the input video
    - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.
    
    This field is retained only for backward compatibility and will be removed in a future release.
    """

    model: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "default",
            "kling-1.6",
            "kling-2.5",
            "kling-2.5-audio",
            "kling-3.0",
            "seedance",
            "sora-2",
            "veo3.1",
            "veo3.1-audio",
        ]
    ]
    """
    The AI model to use for video generation.
    * `default`: Our recommended model for general use (Kling 2.5 Audio). Note: For backward compatibility, if you use default and end_seconds > 10, we'll fall back to Kling 1.6.
    * `seedance`: Great for fast iteration and start/end frame
    * `kling-2.5`: Great for motion, action, and camera control
    * `kling-3.0`: Great for cinematic, multi-scene storytelling with control
    * `sora-2`: Great for story-telling, dialogue & creativity
    * `veo3.1`: Great for realism, polish, & prompt adherence
    * `kling-1.6`: Great for dependable clips with smooth motion
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your video a custom name for easy identification.
    """

    resolution: typing_extensions.NotRequired[
        typing_extensions.Literal["1080p", "480p", "720p"]
    ]
    """
    Controls the output video resolution. Defaults to `720p` if not specified.
    
    * **Default**: Supports `480p`, `720p`, and `1080p`.
    * **seedance**: Supports `480p`, `720p`, `1080p`.
    * **kling-2.5**: Supports `720p`, `1080p`.
    * **kling-3.0**: Supports `720p`, `1080p`.
    * **sora-2**: Supports `720p`.
    * **veo3.1**: Supports `720p`, `1080p`.
    * **kling-1.6**: Supports `720p`, `1080p`.
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
