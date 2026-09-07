import pydantic


class V1AccountListResponseSubscriptionPrice(pydantic.BaseModel):
    """
    V1AccountListResponseSubscriptionPrice
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Price charged per billing interval, in the smallest unit of the currency (e.g. 4900 is $49.00 for `usd`). Discounts are not applied.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter ISO 4217 currency code, lowercase.
    """
