# v1.head_swap

## Module Functions

### Head Swap <a name="create"></a>

Swap a head onto a body image. Each image costs 10 credits. Output resolution depends on your subscription; you may set `max_resolution` lower than your plan maximum if desired.

**API Endpoint**: `POST /v1/head-swap`

#### Parameters

| Parameter           | Required | Description                                                                                                                                                                                                                                                                                                                                                           | Example                                                                                    |
| ------------------- | :------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `assets`            |    ✓     | Provide the body and head images for head swap                                                                                                                                                                                                                                                                                                                        | `{"body_file_path": "api-assets/id/1234.png", "head_file_path": "api-assets/id/5678.png"}` |
| `└─ body_file_path` |    ✓     | Image that receives the swapped head. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.   | `"api-assets/id/1234.png"`                                                                 |
| `└─ head_file_path` |    ✓     | Image of the head to place on the body. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details. | `"api-assets/id/5678.png"`                                                                 |
| `max_resolution`    |    ✗     | Constrains the larger dimension (height or width) of the output. Omit to use the maximum allowed for your plan (capped at 2048px). Values above your plan maximum are clamped down to your plan's maximum.                                                                                                                                                            | `1024`                                                                                     |
| `name`              |    ✗     | Give your image a custom name for easy identification.                                                                                                                                                                                                                                                                                                                | `"My Head Swap image"`                                                                     |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.head_swap.create(
    assets={
        "body_file_path": "api-assets/id/1234.png",
        "head_file_path": "api-assets/id/5678.png",
    },
    max_resolution=1024,
    name="My Head Swap image",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.head_swap.create(
    assets={
        "body_file_path": "api-assets/id/1234.png",
        "head_file_path": "api-assets/id/5678.png",
    },
    max_resolution=1024,
    name="My Head Swap image",
)
```

#### Response

##### Type

[V1HeadSwapCreateResponse](/magic_hour/types/models/v1_head_swap_create_response.py)

##### Example

```python
{"credits_charged": 10, "frame_cost": 10, "id": "cuid-example"}
```
