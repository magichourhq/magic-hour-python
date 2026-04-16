import pydantic
import typing
import typing_extensions

from .v1_body_swap_create_body_assets import (
    V1BodySwapCreateBodyAssets,
    _SerializerV1BodySwapCreateBodyAssets,
)


class V1BodySwapCreateBody(typing_extensions.TypedDict):
    """
    V1BodySwapCreateBody
    """

    assets: typing_extensions.Required[V1BodySwapCreateBodyAssets]
    """
    Person image and scene image for body swap
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your image a custom name for easy identification.
    """

    resolution: typing_extensions.Required[
        typing_extensions.Literal["1k", "2k", "4k", "640px"]
    ]
    """
    Output resolution. Determines credits charged for the run.
    """


class _SerializerV1BodySwapCreateBody(pydantic.BaseModel):
    """
    Serializer for V1BodySwapCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1BodySwapCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    resolution: typing_extensions.Literal["1k", "2k", "4k", "640px"] = pydantic.Field(
        alias="resolution",
    )
