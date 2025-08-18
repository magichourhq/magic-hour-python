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

    end_seconds: typing_extensions.Required[float]
    """
    The total duration of the output video in seconds.
    
    The value must be greater than or equal to 5 seconds and less than or equal to 60 seconds.
    
    Note: For 480p resolution, the value must be either 5 or 10.
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of video. This value is mainly used for your own identification of the video.
    """

    orientation: typing_extensions.Required[
        typing_extensions.Literal["landscape", "portrait", "square"]
    ]
    """
    Determines the orientation of the output video
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

    style: typing_extensions.Required[V1TextToVideoCreateBodyStyle]


class _SerializerV1TextToVideoCreateBody(pydantic.BaseModel):
    """
    Serializer for V1TextToVideoCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    orientation: typing_extensions.Literal["landscape", "portrait", "square"] = (
        pydantic.Field(
            alias="orientation",
        )
    )
    resolution: typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]] = (
        pydantic.Field(alias="resolution", default=None)
    )
    style: _SerializerV1TextToVideoCreateBodyStyle = pydantic.Field(
        alias="style",
    )
