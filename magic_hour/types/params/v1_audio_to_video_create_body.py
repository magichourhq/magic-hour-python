import pydantic
import typing
import typing_extensions

from .v1_audio_to_video_create_body_assets import (
    V1AudioToVideoCreateBodyAssets,
    _SerializerV1AudioToVideoCreateBodyAssets,
)
from .v1_audio_to_video_create_body_style import (
    V1AudioToVideoCreateBodyStyle,
    _SerializerV1AudioToVideoCreateBodyStyle,
)


class V1AudioToVideoCreateBody(typing_extensions.TypedDict):
    """
    V1AudioToVideoCreateBody
    """

    assets: typing_extensions.Required[V1AudioToVideoCreateBodyAssets]
    """
    Provide the audio file and an optional reference image.
    """

    end_seconds: typing_extensions.Required[float]
    """
    End time of your clip (seconds). Must be greater than start_seconds.
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your video a custom name for easy identification.
    """

    resolution: typing_extensions.NotRequired[
        typing_extensions.Literal["1080p", "480p", "720p"]
    ]
    """
    Output video resolution. Defaults to `720p` on paid tiers and `480p` on free tiers.
    """

    start_seconds: typing_extensions.NotRequired[float]
    """
    Start time of your clip (seconds). Must be ≥ 0.
    """

    style: typing_extensions.NotRequired[V1AudioToVideoCreateBodyStyle]
    """
    Attributes used to dictate the style of the output
    """


class _SerializerV1AudioToVideoCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AudioToVideoCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1AudioToVideoCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    resolution: typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]] = (
        pydantic.Field(alias="resolution", default=None)
    )
    start_seconds: typing.Optional[float] = pydantic.Field(
        alias="start_seconds", default=None
    )
    style: typing.Optional[_SerializerV1AudioToVideoCreateBodyStyle] = pydantic.Field(
        alias="style", default=None
    )
