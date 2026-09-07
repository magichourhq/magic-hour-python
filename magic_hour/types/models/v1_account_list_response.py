import pydantic
import typing
import typing_extensions

from .v1_account_list_response_subscription import V1AccountListResponseSubscription


class V1AccountListResponse(pydantic.BaseModel):
    """
    V1AccountListResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    credits: int = pydantic.Field(
        alias="credits",
    )
    """
    Credits currently available to spend. Includes subscription credits and any purchased credit packs.
    """
    email: typing.Optional[str] = pydantic.Field(
        alias="email",
    )
    """
    Email address of the account.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique ID of the account that owns the API key.
    """
    subscription: typing.Optional[V1AccountListResponseSubscription] = pydantic.Field(
        alias="subscription",
    )
    """
    Details of the account's subscription plan. `null` if the account has no subscription, e.g. a free account, an account that only purchased credit packs, or an account on usage-based API pricing.
    
    Reflects the plan currently configured on the subscription. If a plan change is scheduled, `tier` stays on the current plan until the next payment succeeds, so `tier` and `name` can briefly disagree.
    """
    tier: typing_extensions.Literal["business", "creator", "free", "pro"] = (
        pydantic.Field(
            alias="tier",
        )
    )
    """
    Subscription tier in effect for the account. `free` if there is no active subscription, including while a subscription is `past_due`.
    """
