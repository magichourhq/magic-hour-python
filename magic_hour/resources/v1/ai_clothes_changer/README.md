
### AI Clothes Changer <a name="create"></a>

Change outfits in photos in seconds with just a photo reference. Each photo costs 25 credits.

**API Endpoint**: `POST /v1/ai-clothes-changer`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for clothes changer | `{"garment_file_path": "api-assets/id/outfit.png", "garment_type": "upper_body", "person_file_path": "api-assets/id/model.png"}` |
| `name` | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Clothes Changer image"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_clothes_changer.create(
    assets={
        "garment_file_path": "api-assets/id/outfit.png",
        "garment_type": "upper_body",
        "person_file_path": "api-assets/id/model.png",
    },
    name="Clothes Changer image",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_clothes_changer.create(
    assets={
        "garment_file_path": "api-assets/id/outfit.png",
        "garment_type": "upper_body",
        "person_file_path": "api-assets/id/model.png",
    },
    name="Clothes Changer image",
)

```

#### Response

##### Type
[V1AiClothesChangerCreateResponse](/magic_hour/types/models/v1_ai_clothes_changer_create_response.py)

##### Example
`{"credits_charged": 25, "frame_cost": 25, "id": "cuid-example"}`
