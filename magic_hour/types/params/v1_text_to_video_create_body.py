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
    * **Seedance**: Supports `9:16`, `16:9`, `1:1`.
    * **Kling 2.5 Audio**: Supports `9:16`, `16:9`, `1:1`.
    * **Sora 2**: Supports `9:16`, `16:9`.
    * **Veo 3.1 Audio**: Supports `9:16`, `16:9`.
    * **Veo 3.1**: Supports `9:16`, `16:9`.
    * **Kling 1.6**: Supports `9:16`, `16:9`, `1:1`.
    """

    end_seconds: typing_extensions.Required[float]
    """
    The total duration of the output video in seconds.
    
    Supported durations depend on the chosen model:
    * **Default**: 5-60 seconds (2-12 seconds for 480p).
    * **Seedance**: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    * **Kling 2.5 Audio**: 5, 10
    * **Sora 2**: 4, 8, 12, 24, 36, 48, 60
    * **Veo 3.1 Audio**: 4, 6, 8, 16, 24, 32, 40, 48, 56
    * **Veo 3.1**: 4, 6, 8, 16, 24, 32, 40, 48, 56
    * **Kling 1.6**: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60
    """

    model: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "default",
            "kling-1.6",
            "kling-2.5-audio",
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
    * `kling-2.5-audio`: Great for motion, action, and camera control
    * `sora-2`: Great for story-telling, dialogue & creativity
    * `veo3.1-audio`: Great for dialogue + SFX generated natively
    * `veo3.1`: Great for realism, polish, & prompt adherence
    * `kling-1.6`: Great for dependable clips with smooth motion
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
        typing_extensions.Literal["1080p", "480p", "720p"]
    ]
    """
    Controls the output video resolution. Defaults to `720p` if not specified.
    
    * **Default**: Supports `480p`, `720p`, and `1080p`.
    * **Seedance**: Supports `480p`, `720p`, `1080p`.
    * **Kling 2.5 Audio**: Supports `720p`, `1080p`.
    * **Sora 2**: Supports `720p`.
    * **Veo 3.1 Audio**: Supports `720p`, `1080p`.
    * **Veo 3.1**: Supports `720p`, `1080p`.
    * **Kling 1.6**: Supports `720p`, `1080p`.
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
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    model: typing.Optional[
        typing_extensions.Literal[
            "default",
            "kling-1.6",
            "kling-2.5-audio",
            "seedance",
            "sora-2",
            "veo3.1",
            "veo3.1-audio",
        ]
    ] = pydantic.Field(alias="model", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    orientation: typing.Optional[
        typing_extensions.Literal["landscape", "portrait", "square"]
    ] = pydantic.Field(alias="orientation", default=None)
    resolution: typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]] = (
        pydantic.Field(alias="resolution", default=None)
    )
    style: _SerializerV1TextToVideoCreateBodyStyle = pydantic.Field(
        alias="style",
    )
