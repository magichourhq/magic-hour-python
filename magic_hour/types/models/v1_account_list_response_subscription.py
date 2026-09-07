import pydantic
import typing
import typing_extensions

from .v1_account_list_response_subscription_discount import (
    V1AccountListResponseSubscriptionDiscount,
)
from .v1_account_list_response_subscription_price import (
    V1AccountListResponseSubscriptionPrice,
)


class V1AccountListResponseSubscription(pydantic.BaseModel):
    """
    Details of the account's subscription plan. `null` if the account has no subscription, e.g. a free account, an account that only purchased credit packs, or an account on usage-based API pricing.

    Reflects the plan currently configured on the subscription. If a plan change is scheduled, `tier` stays on the current plan until the next payment succeeds, so `tier` and `name` can briefly disagree.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    billing_interval: typing.Optional[typing_extensions.Literal["month", "year"]] = (
        pydantic.Field(
            alias="billing_interval",
        )
    )
    """
    How often the subscription is billed. `null` if unknown.
    """
    cancel_at_period_end: bool = pydantic.Field(
        alias="cancel_at_period_end",
    )
    """
    Whether the subscription is scheduled to end at `current_period_end` instead of renewing. The subscription stays usable until then.
    """
    current_period_end: typing.Optional[str] = pydantic.Field(
        alias="current_period_end",
    )
    """
    End of the current billing period, in ISO 8601 format. The subscription renews at this time, or ends if `cancel_at_period_end` is `true`.
    """
    discount: typing.Optional[V1AccountListResponseSubscriptionDiscount] = (
        pydantic.Field(
            alias="discount",
        )
    )
    """
    Discount applied to the subscription. `null` if no discount is applied.
    """
    name: typing.Optional[str] = pydantic.Field(
        alias="name",
    )
    """
    Name of the current subscription plan, e.g. `Creator`, `Pro`, `Pro Plus`, `Business`. `null` if the plan cannot be determined. Use `tier` for a machine-readable value.
    """
    price: V1AccountListResponseSubscriptionPrice = pydantic.Field(
        alias="price",
    )
    status: typing_extensions.Literal["active", "past_due"] = pydantic.Field(
        alias="status",
    )
    """
    Status of the subscription.
    - `active`: payments are up to date.
    - `past_due`: the latest payment failed. `tier` is `free` until payment succeeds. The subscription is canceled if payment keeps failing.
    """
