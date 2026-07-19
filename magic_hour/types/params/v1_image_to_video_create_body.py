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
    * **`ltx-2.3`**: Toggle-able: no additional credits for audio
    * **`wan-2.2`**: Not supported
    * **`kling-2.5`**: Toggle-able: no additional credits for audio
    * **`kling-3.0`**: Toggle-able: audio adds extra credits when enabled
    * **`veo3.1-lite`**: Toggle-able: audio adds extra credits when enabled
    * **`veo3.1`**: Toggle-able: audio adds extra credits when enabled
    * **`seedance-1.5`**: Toggle-able: audio adds extra credits when enabled
    * **`seedance-2.0-mini`**: Toggle-able: no additional credits for audio
    * **`seedance-2.0`**: Toggle-able: no additional credits for audio
    * **`sora-2`**: Toggle-able: no additional credits for audio
    
    """

    end_seconds: typing_extensions.Required[float]
    """
    The total duration of the output video in seconds. Supported durations depend on the chosen model:
    
    * **`ltx-2.3`**: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30
    * **`wan-2.2`**: 3, 4, 5, 6, 7, 8, 9, 10, 15
    * **`kling-2.5`**: 5, 10
    * **`kling-3.0`**: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
    * **`veo3.1-lite`**: 4, 6, 8, 16, 24, 32, 40, 48, 56
    * **`veo3.1`**: 4, 6, 8, 16, 24, 32, 40, 48, 56
    * **`seedance-1.5`**: 4, 5, 6, 7, 8, 9, 10, 11, 12
    * **`seedance-2.0-mini`**: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
    * **`seedance-2.0`**: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
    * **`sora-2`**: 4, 8, 12, 24, 36, 48, 60
    
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
            "ltx-2.3",
            "seedance",
            "seedance-1.5",
            "seedance-2.0",
            "seedance-2.0-mini",
            "sora-2",
            "veo3.1",
            "veo3.1-audio",
            "veo3.1-lite",
            "wan-2.2",
        ]
    ]
    """
    The AI model to use for video generation.
    
    * `default`: uses our currently recommended model for general use. For paid tiers, defaults to `kling-3.0`. For free tiers, it defaults to `ltx-2.3`.
    * `ltx-2.3`: Fastest output. Best for rapid iteration.
    * `wan-2.2`: Strong physics, camera moves, and motion.
    * `kling-2.5`: Great for action, motion blur, and camera moves.
    * `kling-3.0`: Best overall quality for cinematic storytelling.
    * `veo3.1-lite`: Veo quality at a more accessible cost.
    * `veo3.1`: Google's model. Highest realism and detail.
    * `seedance-1.5`: Smooth, consistent motion with precision.
    * `seedance-2.0-mini`: Fast, consistent video with strong motion quality
    * `seedance-2.0`: Top quality with reference-to-video control.
    * `sora-2`: Open AI's model. Great for creativity and viral clips.
    
    If you specify the deprecated model value that includes the `-audio` suffix, this will be the same as included `audio` as `true`.
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your video a custom name for easy identification.
    """

    resolution: typing_extensions.NotRequired[
        typing_extensions.Literal["1080p", "480p", "4k", "720p"]
    ]
    """
    Controls the output video resolution. Defaults to `720p` on paid tiers and `480p` on free tiers.
    
    * **`ltx-2.3`**: Supports 480p, 720p, 1080p.
    * **`wan-2.2`**: Supports 480p, 720p, 1080p.
    * **`kling-2.5`**: Supports 720p, 1080p.
    * **`kling-3.0`**: Supports 720p, 1080p, 4k.
    * **`veo3.1-lite`**: Supports 720p, 1080p.
    * **`veo3.1`**: Supports 720p, 1080p.
    * **`seedance-1.5`**: Supports 480p, 720p, 1080p.
    * **`seedance-2.0-mini`**: Supports 480p, 720p.
    * **`seedance-2.0`**: Supports 480p, 720p.
    * **`sora-2`**: Supports 720p.
    
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
            "ltx-2.3",
            "seedance",
            "seedance-1.5",
            "seedance-2.0",
            "seedance-2.0-mini",
            "sora-2",
            "veo3.1",
            "veo3.1-audio",
            "veo3.1-lite",
            "wan-2.2",
        ]
    ] = pydantic.Field(alias="model", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    resolution: typing.Optional[
        typing_extensions.Literal["1080p", "480p", "4k", "720p"]
    ] = pydantic.Field(alias="resolution", default=None)
    style: typing.Optional[_SerializerV1ImageToVideoCreateBodyStyle] = pydantic.Field(
        alias="style", default=None
    )
    width: typing.Optional[int] = pydantic.Field(alias="width", default=None)
