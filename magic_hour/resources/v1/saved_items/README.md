# v1.saved_items

## Module Functions

### List saved items <a name="list"></a>

Returns active saved items owned by the authenticated account, newest first. Each item includes every saved asset with a durable file_path for reuse in compatible generation APIs and a temporary signed URL for previewing or downloading. Filter by type to find characters, references, voices, moodboards, or brand kits. To fetch the next page, pass the response's next_cursor as cursor.

**API Endpoint**: `GET /v1/saved-items`

#### Parameters

| Parameter | Required | Description                                                        | Example       |
| --------- | :------: | ------------------------------------------------------------------ | ------------- |
| `cursor`  |    ✗     | Opaque pagination cursor from the previous response's next_cursor. | `"string"`    |
| `limit`   |    ✗     | Maximum number of saved items to return. Defaults to 20.           | `20`          |
| `type_`   |    ✗     | Only return saved items of this type.                              | `"character"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.saved_items.list(limit=20, type_="character")
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.saved_items.list(limit=20, type_="character")
```

#### Response

##### Type

[V1SavedItemsListResponse](/magic_hour/types/models/v1_saved_items_list_response.py)

##### Example

```python
{"items": [{"assets": [{"file_path": "saved-items/user-id/item-id/image.png", "is_primary": True, "media_kind": "IMAGE", "url": "http://www.example.com", "url_expires_at": "2026-09-17T00:00:00.000Z"}], "id": "cuid-example", "name": "Alex", "type_": "character"}], "next_cursor": "string"}
```
