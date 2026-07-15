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
    End time of your clip in seconds. Must be greater than `start_seconds`. Duration must be between 3 and 10 seconds.
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your video a custom name for easy identification.
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
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    start_seconds: typing.Optional[float] = pydantic.Field(
        alias="start_seconds", default=None
    )
    style: _SerializerV1AiVideoEditorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
