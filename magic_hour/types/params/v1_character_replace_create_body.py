import pydantic
import typing
import typing_extensions

from .v1_character_replace_create_body_assets import (
    V1CharacterReplaceCreateBodyAssets,
    _SerializerV1CharacterReplaceCreateBodyAssets,
)
from .v1_character_replace_create_body_style import (
    V1CharacterReplaceCreateBodyStyle,
    _SerializerV1CharacterReplaceCreateBodyStyle,
)


class V1CharacterReplaceCreateBody(typing_extensions.TypedDict):
    """
    V1CharacterReplaceCreateBody
    """

    assets: typing_extensions.Required[V1CharacterReplaceCreateBodyAssets]
    """
    Source video and reference character image for the job.
    """

    end_seconds: typing_extensions.Required[float]
    """
    End time of your clip (seconds). Must be greater than start_seconds.
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your video a custom name for easy identification.
    """

    resolution: typing_extensions.NotRequired[typing_extensions.Literal["480p", "720p"]]
    """
    Output video resolution. Defaults to 480p, the lowest resolution available on your plan.
    """

    start_seconds: typing_extensions.NotRequired[float]
    """
    Start time of your clip (seconds). Must be ≥ 0.
    """

    style: typing_extensions.NotRequired[V1CharacterReplaceCreateBodyStyle]
    """
    Optional style controls for replace vs animate mode and subject selection.
    """


class _SerializerV1CharacterReplaceCreateBody(pydantic.BaseModel):
    """
    Serializer for V1CharacterReplaceCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1CharacterReplaceCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    resolution: typing.Optional[typing_extensions.Literal["480p", "720p"]] = (
        pydantic.Field(alias="resolution", default=None)
    )
    start_seconds: typing.Optional[float] = pydantic.Field(
        alias="start_seconds", default=None
    )
    style: typing.Optional[_SerializerV1CharacterReplaceCreateBodyStyle] = (
        pydantic.Field(alias="style", default=None)
    )
