
### Image Background Remover <a name="create"></a>

Remove background from image. Each image costs 5 credits.

**API Endpoint**: `POST /v1/image-background-remover`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for background removal | `{"background_image_file_path": "api-assets/id/1234.png", "image_file_path": "api-assets/id/1234.png"}` |
| `name` | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Background Remover image"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.image_background_remover.create(
    assets={
        "background_image_file_path": "api-assets/id/1234.png",
        "image_file_path": "api-assets/id/1234.png",
    },
    name="Background Remover image",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.image_background_remover.create(
    assets={
        "background_image_file_path": "api-assets/id/1234.png",
        "image_file_path": "api-assets/id/1234.png",
    },
    name="Background Remover image",
)

```

#### Response

##### Type
[V1ImageBackgroundRemoverCreateResponse](/magic_hour/types/models/v1_image_background_remover_create_response.py)

##### Example
`{"credits_charged": 5, "frame_cost": 5, "id": "cuid-example"}`
