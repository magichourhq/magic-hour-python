
### AI Clothes Changer

Change outfits in photos in seconds with just a photo reference. Each photo costs 25 credits.

**API Endpoint**: `POST /v1/ai-clothes-changer`

### Generate Function <a name="generate"></a>

Generate clothes changed image with automatic file upload and optional download functionality.

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for clothes changer | `{"garment_file_path": "path/to/outfit.png", "garment_type": "upper_body", "person_file_path": "path/to/model.png"}` |
| `name` | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Clothes Changer image"` |
| `wait_for_completion` | ✗ | Whether to wait for the image project to complete before returning | `True` |
| `download_outputs` | ✗ | Whether to download the outputs when complete | `True` |
| `download_directory` | ✗ | The directory to download the outputs to. If not provided, outputs will be downloaded to the current working directory | `"outputs/"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_clothes_changer.generate(
    assets={
        "garment_file_path": "path/to/outfit.png",
        "garment_type": "upper_body",
        "person_file_path": "path/to/model.png",
    },
    name="Clothes Changer image",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs/",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_clothes_changer.generate(
    assets={
        "garment_file_path": "path/to/outfit.png",
        "garment_type": "upper_body",
        "person_file_path": "path/to/model.png",
    },
    name="Clothes Changer image",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs/",
)
```

### Create Function <a name="create"></a>

Basic clothes changer function for direct API calls.

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

#### Create Function Response

##### Type
[V1AiClothesChangerCreateResponse](/magic_hour/types/models/v1_ai_clothes_changer_create_response.py)

##### Example
`{"credits_charged": 25, "frame_cost": 25, "id": "cuid-example"}`

#### Generate Function Response

##### Type
[V1ImageProjectsGetResponseWithDownloads](/magic_hour/types/models/v1_image_projects_get_response.py)

##### Example
`{"status": "COMPLETE", "downloads": [{"download_url": "https://api.example.com/download/image.jpg", "local_path": "outputs/image.jpg"}]}`
