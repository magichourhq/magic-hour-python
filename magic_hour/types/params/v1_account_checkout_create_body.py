import pydantic
import typing
import typing_extensions


class V1AccountCheckoutCreateBody(typing_extensions.TypedDict):
    """
    V1AccountCheckoutCreateBody
    """

    credit_shortfall: typing_extensions.NotRequired[float]
    """
    Credits a blocked request is missing, e.g. `credit_shortfall` from a 402 response. The checkout starts with enough packs to cover it. Defaults to one pack.
    """

    pack_count: typing_extensions.NotRequired[int]
    """
    Number of credit packs the checkout starts with. Takes priority over `credit_shortfall`.
    """

    type_: typing_extensions.Required[typing_extensions.Literal["credit_pack"]]
    """
    What to buy. `credit_pack` is a one-time credit purchase.
    """


class _SerializerV1AccountCheckoutCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AccountCheckoutCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    credit_shortfall: typing.Optional[float] = pydantic.Field(
        alias="credit_shortfall", default=None
    )
    pack_count: typing.Optional[int] = pydantic.Field(alias="pack_count", default=None)
    type_: typing_extensions.Literal["credit_pack"] = pydantic.Field(
        alias="type",
    )
