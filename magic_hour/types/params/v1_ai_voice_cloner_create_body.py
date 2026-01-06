import pydantic
import typing
import typing_extensions

from .v1_ai_voice_cloner_create_body_assets import (
    V1AiVoiceClonerCreateBodyAssets,
    _SerializerV1AiVoiceClonerCreateBodyAssets,
)
from .v1_ai_voice_cloner_create_body_style import (
    V1AiVoiceClonerCreateBodyStyle,
    _SerializerV1AiVoiceClonerCreateBodyStyle,
)


class V1AiVoiceClonerCreateBody(typing_extensions.TypedDict):
    """
    V1AiVoiceClonerCreateBody
    """

    assets: typing_extensions.Required[V1AiVoiceClonerCreateBodyAssets]
    """
    Provide the assets for voice cloning.
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your audio a custom name for easy identification.
    """

    style: typing_extensions.Required[V1AiVoiceClonerCreateBodyStyle]


class _SerializerV1AiVoiceClonerCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiVoiceClonerCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1AiVoiceClonerCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    style: _SerializerV1AiVoiceClonerCreateBodyStyle = pydantic.Field(
        alias="style",
    )
