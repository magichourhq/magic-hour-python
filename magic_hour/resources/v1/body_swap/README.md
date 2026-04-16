# v1.body_swap

## Module Functions

<!-- CUSTOM DOCS START -->

### Body Swap Generate Workflow <a name="generate"></a>

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
res = client.v1.body_swap.generate(
    assets={
        "person_file_path": "/path/to/person.png",
        "scene_file_path": "/path/to/scene.png",
    },
    resolution="1k",
    name="My Body Swap image",
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
res = await client.v1.body_swap.generate(
    assets={
        "person_file_path": "/path/to/person.png",
        "scene_file_path": "/path/to/scene.png",
    },
    resolution="1k",
    name="My Body Swap image",
    wait_for_completion=True,
    download_outputs=True,
    download_directory=".",
)
```

<!-- CUSTOM DOCS END -->

### Body Swap <a name="create"></a>

Swap a person into a scene image using Nano Banana 2. Credits depend on `resolution` (from 100 credits at 640px upward).

**API Endpoint**: `POST /v1/body-swap`

#### Parameters

| Parameter             | Required | Description                                                                                                                                                                                                                                                                                                                                                                | Example                                                                                       |
| --------------------- | :------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `assets`              |    ✓     | Person image and scene image for body swap                                                                                                                                                                                                                                                                                                                                 | `{"person_file_path": "api-assets/id/1234.png", "scene_file_path": "api-assets/id/5678.png"}` |
| `└─ person_file_path` |    ✓     | Image of the person to place into the scene. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details. | `"api-assets/id/1234.png"`                                                                    |
| `└─ scene_file_path`  |    ✓     | Target scene image (background). This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.             | `"api-assets/id/5678.png"`                                                                    |
| `resolution`          |    ✓     | Output resolution. Determines credits charged for the run.                                                                                                                                                                                                                                                                                                                 | `"1k"`                                                                                        |
| `name`                |    ✗     | Give your image a custom name for easy identification.                                                                                                                                                                                                                                                                                                                     | `"My Body Swap image"`                                                                        |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.body_swap.create(
    assets={
        "person_file_path": "api-assets/id/1234.png",
        "scene_file_path": "api-assets/id/5678.png",
    },
    resolution="1k",
    name="My Body Swap image",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.body_swap.create(
    assets={
        "person_file_path": "api-assets/id/1234.png",
        "scene_file_path": "api-assets/id/5678.png",
    },
    resolution="1k",
    name="My Body Swap image",
)
```

#### Response

##### Type

[V1BodySwapCreateResponse](/magic_hour/types/models/v1_body_swap_create_response.py)

##### Example

```python
{"credits_charged": 100, "frame_cost": 100, "id": "cuid-example"}
```
