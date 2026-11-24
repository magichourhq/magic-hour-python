import pydantic


class V1AccountCheckoutCreateResponse(pydantic.BaseModel):
    """
    V1AccountCheckoutCreateResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    checkout_url: str = pydantic.Field(
        alias="checkout_url",
    )
    """
    Open in a browser to complete the purchase.
    """
