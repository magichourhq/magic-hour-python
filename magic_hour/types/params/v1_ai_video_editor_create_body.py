import pydantic
import typing
import typing_extensions

from .v1_ai_video_editor_create_body_assets import (
    V1AiVideoEditorCreateBodyAssets,
    _SerializerV1AiVideoEditorCreateBodyAssets,
)
from .v1_ai_video_editor_create_body_style import (
    V1AiVideoEditorCreateBodyStyle,
    _SerializerV1AiVideoEditorCreateBodyStyle,
)


class V1AiVideoEditorCreateBody(typing_extensions.TypedDict):
    """
    V1AiVideoEditorCreateBody
    """

    assets: typing_extensions.Required[V1AiVideoEditorCreateBodyAssets]
    """
    Provide the assets for video editing.
    """

    end_seconds: typing_extensions.Required[float]
    """
    End time of your clip in seconds. Must be greater than `start_seconds`. Minimum duration depends on model: `gemini-omni-1.1`: 3s, `ltx-2.3`: 0.5s. Maximum duration depends on model: `gemini-omni-1.1`: 10s, `ltx-2.3`: 45s.
    """

    model: typing_extensions.NotRequired[
        typing_extensions.Literal["gemini-omni", "gemini-omni-1.1", "ltx-2.3"]
    ]
    """
    Editing model. Defaults to `ltx-2.3` for free tier and `gemini-omni-1.1` for paid. `gemini-omni` is deprecated; use `gemini-omni-1.1` instead.
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your video a custom name for easy identification.
    """

    resolution: typing_extensions.NotRequired[
        typing_extensions.Literal["1080p", "480p", "720p"]
    ]
    """
    Output resolution. Defaults to `480p` for free tier and `720p` for paid. `gemini-omni-1.1` and deprecated `gemini-omni` support 720p and 1080p; LTX-2.3 supports 480p, 720p, and 1080p.
    """

    start_seconds: typing_extensions.NotRequired[float]
    """
    Start time of your clip (seconds). Must be ≥ 0.
    """

    style: typing_extensions.Required[V1AiVideoEditorCreateBodyStyle]


class _SerializerV1AiVideoEditorCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiVideoEditorCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1AiVideoEditorCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    model: typing.Optional[
        typing_extensions.Literal["gemini-omni", "gemini-omni-1.1", "ltx-2.3"]
    ] = pydantic.Field(alias="model", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    resolution: typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]] = (
        pydantic.Field(alias="resolution", default=None)
    )
    start_seconds: typing.Optional[float] = pydantic.Field(
        alias="start_seconds", default=None
    )
    style: _SerializerV1AiVideoEditorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
