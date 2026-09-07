import pydantic
import typing


class V1AccountListResponseSubscriptionDiscount(pydantic.BaseModel):
    """
    Discount applied to the subscription. `null` if no discount is applied.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_off: typing.Optional[int] = pydantic.Field(
        alias="amount_off",
    )
    """
    Fixed amount taken off `price.amount` each billing interval, in the smallest unit of the currency. `null` if the discount is a percentage.
    """
    percent_off: typing.Optional[float] = pydantic.Field(
        alias="percent_off",
    )
    """
    Percentage taken off `price.amount` each billing interval. `null` if the discount is a fixed amount.
    """
