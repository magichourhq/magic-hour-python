# v1.ai_image_upscaler

## Module Functions






<!-- CUSTOM DOCS START -->

### Ai Image Upscaler Generate Workflow <a name="generate"></a>

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
res = client.v1.ai_image_upscaler.generate(
    assets={"image_file_path": "/path/to/1234.png"},
    scale_factor=2.0,
    style={"enhancement": "Balanced"},
    name="Image Upscaler image",
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
res = await client.v1.ai_image_upscaler.generate(
    assets={"image_file_path": "/path/to/1234.png"},
    scale_factor=2.0,
    style={"enhancement": "Balanced"},
    name="Image Upscaler image",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### AI Image Upscaler <a name="create"></a>

Upscale your image using AI. Each 2x upscale costs 50 credits, and 4x upscale costs 200 credits.

**API Endpoint**: `POST /v1/ai-image-upscaler`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for upscaling | `{"image_file_path": "api-assets/id/1234.png"}` |
| `└─ image_file_path` | ✓ | The image to upscale. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.png"` |
| `scale_factor` | ✓ | How much to scale the image. Must be either 2 or 4.              Note: 4x upscale is only available on Creator, Pro, or Business tier. | `2.0` |
| `style` | ✓ |  | `{"enhancement": "Balanced"}` |
| `└─ enhancement` | ✓ |  | `"Balanced"` |
| `└─ prompt` | ✗ | A prompt to guide the final image. This value is ignored if `enhancement` is not Creative | `"string"` |
| `name` | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Image Upscaler image"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_image_upscaler.create(
    assets={"image_file_path": "api-assets/id/1234.png"},
    scale_factor=2.0,
    style={"enhancement": "Balanced"},
    name="Image Upscaler image",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_image_upscaler.create(
    assets={"image_file_path": "api-assets/id/1234.png"},
    scale_factor=2.0,
    style={"enhancement": "Balanced"},
    name="Image Upscaler image",
)

```

#### Response

##### Type
[V1AiImageUpscalerCreateResponse](/magic_hour/types/models/v1_ai_image_upscaler_create_response.py)

##### Example
`{"credits_charged": 50, "frame_cost": 50, "id": "cuid-example"}`

