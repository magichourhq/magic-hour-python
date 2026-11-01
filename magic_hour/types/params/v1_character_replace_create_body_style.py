import pydantic
import typing
import typing_extensions

from .v1_character_replace_create_body_style_points_item import (
    V1CharacterReplaceCreateBodyStylePointsItem,
    _SerializerV1CharacterReplaceCreateBodyStylePointsItem,
)


class V1CharacterReplaceCreateBodyStyle(typing_extensions.TypedDict):
    """
    Optional style controls for replace vs animate mode and subject selection.
    """

    mode: typing_extensions.NotRequired[typing_extensions.Literal["animate", "replace"]]
    """
    Processing mode. `replace` swaps the detected subject with your reference character. `animate` transfers motion from the video onto your character image.
    """

    points: typing_extensions.NotRequired[
        typing.List[V1CharacterReplaceCreateBodyStylePointsItem]
    ]
    """
    On-frame markers for manual subject selection. Required when `selection_mode` is `point`. Ignored when `selection_mode` is `auto` or omitted. Rejected for models without subject selection (supported by `wan-animate`, `minimax-h3`). `minimax-h3` subject `points` are `replace`-only; `animate` with `selection_mode` `point` returns 422, and with `auto` or no `selection_mode` the points are ignored.
    """

    prompt: typing_extensions.NotRequired[str]
    """
    Optional direction. Supported by kling-3.0, minimax-h3.
    """

    selection_mode: typing_extensions.NotRequired[
        typing_extensions.Literal["auto", "point"]
    ]
    """
    How to locate the subject in the source video. `auto` detects a person automatically. `point` uses your `points` to mark the subject and is supported by `wan-animate`, `minimax-h3`. `minimax-h3` subject `points` are `replace`-only; `animate` with `selection_mode` `point` returns 422, and with `auto` or no `selection_mode` the points are ignored. Defaults to `auto`.
    """


class _SerializerV1CharacterReplaceCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1CharacterReplaceCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mode: typing.Optional[typing_extensions.Literal["animate", "replace"]] = (
        pydantic.Field(alias="mode", default=None)
    )
    points: typing.Optional[
        typing.List[_SerializerV1CharacterReplaceCreateBodyStylePointsItem]
    ] = pydantic.Field(alias="points", default=None)
    prompt: typing.Optional[str] = pydantic.Field(alias="prompt", default=None)
    selection_mode: typing.Optional[typing_extensions.Literal["auto", "point"]] = (
        pydantic.Field(alias="selection_mode", default=None)
    )
