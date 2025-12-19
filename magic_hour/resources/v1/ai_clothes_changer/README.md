# v1.ai_clothes_changer

## Module Functions






<!-- CUSTOM DOCS START -->

### AI Clothes Changer Generate Workflow <a name="generate"></a>

The workflow performs the following action

1. upload local assets to Magic Hour storage. So you can pass in a local path instead of having to upload files yourself
2. trigger a generation
3. poll for a completion status. This is configurable 
4. if success, download the output to local directory

> [!TIP]
> This is the recommended way to use the SDK unless you have specific needs where it is necessary to split up the actions.

#### Parameters

In Additional to the parameters listed in the `.create` section below, `.generate` introduces 3 new parameters:

- `wait_for_completion` (bool, default True): Whether to wait for the project to complete.
- `download_outputs` (bool, default True): Whether to download the generated files
- `download_directory` (str, optional): Directory to save downloaded files (defaults to current directory)

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_clothes_changer.generate(
    assets={
        "garment_file_path": "/path/to/outfit.png",
        "garment_type": "upper_body",
        "person_file_path": "/path/to/model.png",
    },
    name="Clothes Changer image",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_clothes_changer.generate(
    assets={
        "garment_file_path": "/path/to/outfit.png",
        "garment_type": "upper_body",
        "person_file_path": "/path/to/model.png",
    },
    name="Clothes Changer image",
    download_directory="outputs",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs",
)
```

<!-- CUSTOM DOCS END -->
### AI Clothes Changer <a name="create"></a>

Change outfits in photos in seconds with just a photo reference. Each photo costs 25 credits.

**API Endpoint**: `POST /v1/ai-clothes-changer`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for clothes changer | `{"garment_file_path": "api-assets/id/outfit.png", "garment_type": "upper_body", "person_file_path": "api-assets/id/model.png"}` |
| `└─ garment_file_path` | ✓ | The image of the outfit. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/outfit.png"` |
| `└─ garment_type` | ✓ | The type of the outfit. | `"upper_body"` |
| `└─ person_file_path` | ✓ | The image with the person. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/model.png"` |
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

