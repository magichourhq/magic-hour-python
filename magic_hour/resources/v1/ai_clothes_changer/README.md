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
    download_directory=".",
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
    wait_for_completion=True,
    download_outputs=True,
    download_directory=".",
)
```

<!-- CUSTOM DOCS END -->

### AI Clothes Changer <a name="create"></a>

Change outfits in photos in seconds with just a photo reference. Each photo costs 25 credits.

**API Endpoint**: `POST /v1/ai-clothes-changer`

#### Parameters

| Parameter              | Required | Description                                                                                                                                                                                                                                                                                                                                              | Example                                                                                                                          |
| ---------------------- | :------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `assets`               |    ✓     | Provide the assets for clothes changer                                                                                                                                                                                                                                                                                                                   | `{"garment_file_path": "api-assets/id/outfit.png", "garment_type": "upper_body", "person_file_path": "api-assets/id/model.png"}` |
| `└─ garment_file_path` |    ✓     | The image of the outfit. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.   | `"api-assets/id/outfit.png"`                                                                                                     |
| `└─ garment_type`      |    ✗     | Type of garment to swap. If not provided, swaps the entire outfit. _ `upper_body` - for shirts/jackets _ `lower_body` - for pants/skirts _ `dresses` - for entire outfit (deprecated, use `entire_outfit` instead) _ `entire_outfit` - for entire outfit                                                                                                 | `"upper_body"`                                                                                                                   |
| `└─ person_file_path`  |    ✓     | The image with the person. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details. | `"api-assets/id/model.png"`                                                                                                      |
| `name`                 |    ✗     | Give your image a custom name for easy identification.                                                                                                                                                                                                                                                                                                   | `"My Clothes Changer image"`                                                                                                     |

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
    name="My Clothes Changer image",
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
    name="My Clothes Changer image",
)
```

#### Response

##### Type

[V1AiClothesChangerCreateResponse](/magic_hour/types/models/v1_ai_clothes_changer_create_response.py)

##### Example

```python
{"credits_charged": 25, "frame_cost": 25, "id": "cuid-example"}
```
