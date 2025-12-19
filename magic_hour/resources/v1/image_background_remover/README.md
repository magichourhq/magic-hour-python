# v1.image_background_remover

## Module Functions






<!-- CUSTOM DOCS START -->

### Image Background Remover Generate Workflow <a name="generate"></a>

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
res = client.v1.image_background_remover.generate(
    assets={
        "background_image_file_path": "/path/to/1234.png",
        "image_file_path": "/path/to/1234.png",
    },
    name="Background Remover image",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.image_background_remover.generate(
    assets={
        "background_image_file_path": "/path/to/1234.png",
        "image_file_path": "/path/to/1234.png",
    },
    name="Background Remover image",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### Image Background Remover <a name="create"></a>

Remove background from image. Each image costs 5 credits.

**API Endpoint**: `POST /v1/image-background-remover`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for background removal | `{"background_image_file_path": "api-assets/id/1234.png", "image_file_path": "api-assets/id/1234.png"}` |
| `└─ background_image_file_path` | ✗ | The image used as the new background for the image_file_path. This image will be resized to match the image in image_file_path. Please make sure the resolution between the images are similar.  This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.png"` |
| `└─ image_file_path` | ✓ | The image to remove the background. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.png"` |
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

