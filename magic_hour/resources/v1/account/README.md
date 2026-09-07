# v1.account

## Module Functions

### Get account details <a name="list"></a>

Get the current credit balance and subscription details of the account that owns the API key.

**API Endpoint**: `GET /v1/account`

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.account.list()
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.account.list()
```

#### Response

##### Type

[V1AccountListResponse](/magic_hour/types/models/v1_account_list_response.py)

##### Example

```python
{"credits": 12500, "email": "user@example.com", "id": "cuid-example", "subscription": {"billing_interval": "month", "cancel_at_period_end": False, "current_period_end": "2026-10-01T00:00:00.000Z", "discount": {"amount_off": 123, "percent_off": 20.0}, "name": "Pro", "price": {"amount": 4900, "currency": "usd"}, "status": "active"}, "tier": "pro"}
```
