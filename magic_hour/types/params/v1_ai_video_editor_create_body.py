import pydantic
import typing
import typing_extensions

from .v1_ai_video_editor_create_body_assets import (
    V1AiVideoEditorCreateBodyAssets,
    _SerializerV1AiVideoEditorCreateBodyAssets,
)
from .v1_ai_video_editor_create_body_references_item import (
    V1AiVideoEditorCreateBodyReferencesItem,
    _SerializerV1AiVideoEditorCreateBodyReferencesItem,
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
    End time of your clip in seconds. Must be greater than `start_seconds`. Allowed duration depends on model: `gemini-omni-1.2`: 3-15s, `wan-3.0`: 2-15s, `ltx-2.5`: 0.5-60s (30s at 1080p), `kling-4.0`: 3-30s.
    """

    model: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "gemini-omni",
            "gemini-omni-1.1",
            "gemini-omni-1.2",
            "kling-4.0",
            "ltx-2.3",
            "ltx-2.5",
            "wan-3.0",
        ]
    ]
    """
    The AI model to use for video editing. Defaults to `ltx-2.5` on free tiers and `gemini-omni-1.2` on paid tiers.
    
    * `gemini-omni-1.2`: Best for precise clips up to 15s, references, and high-resolution output. Requires a paid tier.
    * `wan-3.0`: High-quality video with native audio, long clips, and end-frame control. Requires a paid tier.
    * `ltx-2.5`: Fastest for general scenes, long clips, audio, and rapid iteration.
    * `kling-4.0`: Create cinematic videos with image and video references and optional audio. Requires a paid tier.
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your video a custom name for easy identification.
    """

    references: typing_extensions.NotRequired[
        typing.List[V1AiVideoEditorCreateBodyReferencesItem]
    ]
    """
    Name references without @ and refer to them as @name in style.prompt. Names must be unique, ignoring case. Maximum 10 references total. Omit for no references.
    
    Reference images for gemini-omni-1.2, wan-3.0, kling-4.0.
    """

    resolution: typing_extensions.NotRequired[
        typing_extensions.Literal["1080p", "360p", "480p", "4k", "720p"]
    ]
    """
    Output resolution. Defaults to `480p` for free tier and `720p` for paid. Supported per model: `gemini-omni-1.2`: 360p, 720p, 1080p, 4k; `wan-3.0`: 480p, 720p, 1080p; `ltx-2.5`: 480p, 720p, 1080p; `kling-4.0`: 720p, 1080p.
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
        typing_extensions.Literal[
            "gemini-omni",
            "gemini-omni-1.1",
            "gemini-omni-1.2",
            "kling-4.0",
            "ltx-2.3",
            "ltx-2.5",
            "wan-3.0",
        ]
    ] = pydantic.Field(alias="model", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    references: typing.Optional[
        typing.List[_SerializerV1AiVideoEditorCreateBodyReferencesItem]
    ] = pydantic.Field(alias="references", default=None)
    resolution: typing.Optional[
        typing_extensions.Literal["1080p", "360p", "480p", "4k", "720p"]
    ] = pydantic.Field(alias="resolution", default=None)
    start_seconds: typing.Optional[float] = pydantic.Field(
        alias="start_seconds", default=None
    )
    style: _SerializerV1AiVideoEditorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
