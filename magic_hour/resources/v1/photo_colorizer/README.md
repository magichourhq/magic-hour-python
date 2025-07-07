
### Photo Colorizer <a name="create"></a>

Colorize image. Each image costs 5 credits.

**API Endpoint**: `POST /v1/photo-colorizer`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for photo colorization | `{"image_file_path": "api-assets/id/1234.png"}` |
| `name` | ✗ | The name of image | `"Photo Colorizer image"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.photo_colorizer.create(
    assets={"image_file_path": "api-assets/id/1234.png"}, name="Photo Colorizer image"
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.photo_colorizer.create(
    assets={"image_file_path": "api-assets/id/1234.png"}, name="Photo Colorizer image"
)

```

#### Response

##### Type
[V1PhotoColorizerCreateResponse](/magic_hour/types/models/v1_photo_colorizer_create_response.py)

##### Example
`{"credits_charged": 5, "frame_cost": 5, "id": "clx7uu86w0a5qp55yxz315r6r"}`
