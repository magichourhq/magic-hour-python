import pydantic
import typing
import typing_extensions

from .v1_head_swap_create_body_assets import (
    V1HeadSwapCreateBodyAssets,
    _SerializerV1HeadSwapCreateBodyAssets,
)


class V1HeadSwapCreateBody(typing_extensions.TypedDict):
    """
    V1HeadSwapCreateBody
    """

    assets: typing_extensions.Required[V1HeadSwapCreateBodyAssets]
    """
    Provide the body and head images for head swap
    """

    max_resolution: typing_extensions.NotRequired[int]
    """
    Constrains the larger dimension (height or width) of the output. Omit to use the maximum allowed for your plan (capped at 2048px). Values above your plan maximum are clamped down to your plan's maximum.
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your image a custom name for easy identification.
    """


class _SerializerV1HeadSwapCreateBody(pydantic.BaseModel):
    """
    Serializer for V1HeadSwapCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1HeadSwapCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    max_resolution: typing.Optional[int] = pydantic.Field(
        alias="max_resolution", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
