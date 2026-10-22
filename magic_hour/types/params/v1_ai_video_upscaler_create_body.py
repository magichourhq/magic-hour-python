import pydantic
import typing
import typing_extensions

from .v1_ai_video_upscaler_create_body_assets import (
    V1AiVideoUpscalerCreateBodyAssets,
    _SerializerV1AiVideoUpscalerCreateBodyAssets,
)


class V1AiVideoUpscalerCreateBody(typing_extensions.TypedDict):
    """
    V1AiVideoUpscalerCreateBody
    """

    assets: typing_extensions.Required[V1AiVideoUpscalerCreateBodyAssets]
    """
    Source video for the upscale job.
    """

    end_seconds: typing_extensions.Required[float]
    """
    End time of your clip (seconds). Must be greater than start_seconds.
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your video a custom name for easy identification.
    """

    resolution: typing_extensions.Required[
        typing_extensions.Literal["1080p", "2k", "4k", "720p"]
    ]
    """
    Output resolution. `720p` and `1080p` set the output's short side, `2k` and `4k` its long side; the aspect ratio is kept. Requires a paid plan.
    """

    start_seconds: typing_extensions.NotRequired[float]
    """
    Start time of your clip (seconds). Must be ≥ 0.
    """


class _SerializerV1AiVideoUpscalerCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiVideoUpscalerCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1AiVideoUpscalerCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    resolution: typing_extensions.Literal["1080p", "2k", "4k", "720p"] = pydantic.Field(
        alias="resolution",
    )
    start_seconds: typing.Optional[float] = pydantic.Field(
        alias="start_seconds", default=None
    )
