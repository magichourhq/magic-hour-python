import pydantic
import typing
import typing_extensions

from .v1_text_to_video_create_body_style import (
    V1TextToVideoCreateBodyStyle,
    _SerializerV1TextToVideoCreateBodyStyle,
)


class V1TextToVideoCreateBody(typing_extensions.TypedDict):
    """
    V1TextToVideoCreateBody
    """

    aspect_ratio: typing_extensions.NotRequired[
        typing_extensions.Literal["16:9", "1:1", "9:16"]
    ]
    """
    Determines the aspect ratio of the output video.
    
    * **`gemini-omni-1.1`**: Supports 16:9, 9:16.
    * **`kling-2.6`**: Supports 9:16, 16:9, 1:1.
    * **`kling-3.0`**: Supports 9:16, 16:9, 1:1.
    * **`ltx-2.3`**: Supports 9:16, 16:9, 1:1.
    * **`ltx-2.5`**: Supports 9:16, 16:9, 1:1.
    * **`minimax-h3`**: Supports 16:9, 9:16, 1:1.
    * **`seedance-1.5`**: Supports 9:16, 16:9, 1:1.
    * **`seedance-2.0`**: Supports 9:16, 16:9, 1:1.
    * **`seedance-2.0-mini`**: Supports 9:16, 16:9, 1:1.
    * **`seedance-2.5`**: Supports 9:16, 16:9, 1:1.
    * **`sora-2`**: Supports 9:16, 16:9.
    * **`veo3.1`**: Supports 9:16, 16:9.
    * **`veo3.1-lite`**: Supports 9:16, 16:9.
    * **`wan-2.2`**: Supports 9:16, 16:9, 1:1.
    
    """

    audio: typing_extensions.NotRequired[bool]
    """
    Whether to include audio in the video. Defaults to `false` if not specified.
    
    Audio support varies by model:
    * **`gemini-omni-1.1`**: Not supported
    * **`kling-2.6`**: Not supported
    * **`kling-3.0`**: Toggle-able: audio adds extra credits when enabled
    * **`ltx-2.3`**: Toggle-able: no additional credits for audio
    * **`ltx-2.5`**: Toggle-able: no additional credits for audio
    * **`minimax-h3`**: Toggle-able: no additional credits for audio
    * **`seedance-1.5`**: Toggle-able: audio adds extra credits when enabled
    * **`seedance-2.0`**: Toggle-able: no additional credits for audio
    * **`seedance-2.0-mini`**: Toggle-able: no additional credits for audio
    * **`seedance-2.5`**: Toggle-able: no additional credits for audio
    * **`sora-2`**: Toggle-able: no additional credits for audio
    * **`veo3.1`**: Toggle-able: audio adds extra credits when enabled
    * **`veo3.1-lite`**: Toggle-able: audio adds extra credits when enabled
    * **`wan-2.2`**: Not supported
    
    """

    end_seconds: typing_extensions.Required[float]
    """
    The total duration of the output video in seconds. Supported durations depend on the chosen model:
    
    * **`gemini-omni-1.1`**: 3, 4, 5, 6, 7, 8, 9, 10
    * **`kling-2.6`**: 5, 10
    * **`kling-3.0`**: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
    * **`ltx-2.3`**: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30
    * **`ltx-2.5`**: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60
    * **`minimax-h3`**: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30
    * **`seedance-1.5`**: 4, 5, 6, 7, 8, 9, 10, 11, 12
    * **`seedance-2.0`**: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
    * **`seedance-2.0-mini`**: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
    * **`seedance-2.5`**: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
    * **`sora-2`**: 4, 8, 12, 24, 36, 48, 60
    * **`veo3.1`**: 4, 6, 8, 16, 24, 32, 40, 48, 56
    * **`veo3.1-lite`**: 4, 6, 8, 16, 24, 32, 40, 48, 56
    * **`wan-2.2`**: 3, 4, 5, 6, 7, 8, 9, 10, 15
    
    """

    model: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "default",
            "gemini-omni-1.1",
            "kling-1.6",
            "kling-2.5",
            "kling-2.5-audio",
            "kling-2.6",
            "kling-3.0",
            "ltx-2",
            "ltx-2.3",
            "ltx-2.5",
            "minimax-h3",
            "seedance",
            "seedance-1.5",
            "seedance-2.0",
            "seedance-2.0-mini",
            "seedance-2.5",
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
    * `gemini-omni-1.1`: Best for precise short clips, first/last frames, and high-resolution output.
    * `kling-2.6`: Best for action, motion blur, and controlled camera moves.
    * `kling-3.0`: Best for cinematic stories, references, and optional audio.
    * `ltx-2.3`: Fastest for general scenes, long clips, audio, and rapid iteration.
    * `ltx-2.5`: Fastest for general scenes, long clips, audio, and rapid iteration.
    * `minimax-h3`: Great for reference-driven clips with native audio and longer durations.
    * `seedance-1.5`: Best for smooth, consistent motion with an end frame.
    * `seedance-2.0`: Best for reference-led clips with precise subject control.
    * `seedance-2.0-mini`: Faster reference-led clips with consistent motion and audio.
    * `seedance-2.5`: Best for premium realism, detail, and natural motion.
    * `sora-2`: Best for creative concepts and longer clips with audio.
    * `veo3.1`: Best for romantic interactions and expressive action, with realistic detail.
    * `veo3.1-lite`: Balanced realism and audio at a lower cost than Veo 3.1.
    * `wan-2.2`: Best for physical motion, action, and camera movement.
    
    If you specify the deprecated model value that includes the `-audio` suffix, this will be the same as included `audio` as `true`.
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your video a custom name for easy identification.
    """

    orientation: typing_extensions.NotRequired[
        typing_extensions.Literal["landscape", "portrait", "square"]
    ]
    """
    Deprecated. Use `aspect_ratio` instead.
    """

    resolution: typing_extensions.NotRequired[
        typing_extensions.Literal["1080p", "480p", "4k", "720p"]
    ]
    """
    Controls the output video resolution. Defaults to `720p` on paid tiers and `480p` on free tiers.
    
    * **`gemini-omni-1.1`**: Supports 360p, 720p, 1080p, 4k.
    * **`kling-2.6`**: Supports 720p, 1080p.
    * **`kling-3.0`**: Supports 720p, 1080p, 4k.
    * **`ltx-2.3`**: Supports 480p, 720p, 1080p.
    * **`ltx-2.5`**: Supports 480p, 720p, 1080p.
    * **`minimax-h3`**: Supports 480p, 720p, 1080p.
    * **`seedance-1.5`**: Supports 480p, 720p, 1080p.
    * **`seedance-2.0`**: Supports 480p, 720p.
    * **`seedance-2.0-mini`**: Supports 480p, 720p.
    * **`seedance-2.5`**: Supports 480p, 720p.
    * **`sora-2`**: Supports 720p.
    * **`veo3.1`**: Supports 720p, 1080p.
    * **`veo3.1-lite`**: Supports 720p, 1080p.
    * **`wan-2.2`**: Supports 480p, 720p, 1080p.
    
    """

    style: typing_extensions.Required[V1TextToVideoCreateBodyStyle]


class _SerializerV1TextToVideoCreateBody(pydantic.BaseModel):
    """
    Serializer for V1TextToVideoCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    aspect_ratio: typing.Optional[typing_extensions.Literal["16:9", "1:1", "9:16"]] = (
        pydantic.Field(alias="aspect_ratio", default=None)
    )
    audio: typing.Optional[bool] = pydantic.Field(alias="audio", default=None)
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    model: typing.Optional[
        typing_extensions.Literal[
            "default",
            "gemini-omni-1.1",
            "kling-1.6",
            "kling-2.5",
            "kling-2.5-audio",
            "kling-2.6",
            "kling-3.0",
            "ltx-2",
            "ltx-2.3",
            "ltx-2.5",
            "minimax-h3",
            "seedance",
            "seedance-1.5",
            "seedance-2.0",
            "seedance-2.0-mini",
            "seedance-2.5",
            "sora-2",
            "veo3.1",
            "veo3.1-audio",
            "veo3.1-lite",
            "wan-2.2",
        ]
    ] = pydantic.Field(alias="model", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    orientation: typing.Optional[
        typing_extensions.Literal["landscape", "portrait", "square"]
    ] = pydantic.Field(alias="orientation", default=None)
    resolution: typing.Optional[
        typing_extensions.Literal["1080p", "480p", "4k", "720p"]
    ] = pydantic.Field(alias="resolution", default=None)
    style: _SerializerV1TextToVideoCreateBodyStyle = pydantic.Field(
        alias="style",
    )
