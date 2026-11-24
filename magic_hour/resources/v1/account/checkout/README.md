# v1.account.checkout

## Module Functions

### Create checkout <a name="create"></a>

Create a Stripe Checkout link for the account that owns the API key. Nothing is charged until the checkout is completed in a browser.

**API Endpoint**: `POST /v1/account/checkout`

#### Parameters

| Parameter          | Required | Description                                                                                                                                                 | Example         |
| ------------------ | :------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `type_`            |    ✓     | What to buy. `credit_pack` is a one-time credit purchase.                                                                                                   | `"credit_pack"` |
| `credit_shortfall` |    ✗     | Credits a blocked request is missing, e.g. `credit_shortfall` from a 402 response. The checkout starts with enough packs to cover it. Defaults to one pack. | `150.0`         |
| `pack_count`       |    ✗     | Number of credit packs the checkout starts with. Takes priority over `credit_shortfall`.                                                                    | `3`             |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.account.checkout.create(
    type_="credit_pack", credit_shortfall=150.0, pack_count=3
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.account.checkout.create(
    type_="credit_pack", credit_shortfall=150.0, pack_count=3
)
```

#### Response

##### Type

[V1AccountCheckoutCreateResponse](/magic_hour/types/models/v1_account_checkout_create_response.py)

##### Example

```python
{"checkout_url": "https://pay.magichour.ai/c/pay/cs_live_..."}
```
