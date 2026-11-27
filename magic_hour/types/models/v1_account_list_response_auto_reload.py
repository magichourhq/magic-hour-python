import pydantic
import typing_extensions


class V1AccountListResponseAutoReload(pydantic.BaseModel):
    """
    V1AccountListResponseAutoReload
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    status: typing_extensions.Literal[
        "active",
        "auto_reload_pending",
        "disabled",
        "payment_failed",
        "spending_limit_reached",
    ] = pydantic.Field(
        alias="status",
    )
    """
    State of Auto Reload on the account.
    - `disabled`: off or never set up.
    - `active`: on, with no refill processing or blocked.
    - `auto_reload_pending`: a refill is processing. Check again shortly.
    - `payment_failed`: the last refill payment failed and paused Auto Reload until the payment method is updated.
    - `spending_limit_reached`: the monthly limit blocked the last refill.
    
    After an `insufficient_credits` rejection, resubmit the same request once `credits` reaches that rejection's `credits_required`.
    """
