# v1.ai_image_editor

## Module Functions






<!-- CUSTOM DOCS START -->

### Ai Image Editor Generate Workflow <a name="generate"></a>

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
res = client.v1.ai_image_editor.generate(
    assets={"image_file_path": "/path/to/1234.png"},
    style={"prompt": "Give me sunglasses"},
    name="Ai Image Editor image",
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
res = await client.v1.ai_image_editor.generate(
    assets={"image_file_path": "/path/to/1234.png"},
    style={"prompt": "Give me sunglasses"},
    name="Ai Image Editor image",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### AI Image Editor <a name="create"></a>

Edit images with AI. Each edit costs 50 credits.

**API Endpoint**: `POST /v1/ai-image-editor`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for image edit | `{"image_file_path": "api-assets/id/1234.png", "image_file_paths": ["api-assets/id/1234.png", "api-assets/id/1235.png"]}` |
| `└─ image_file_path` | ✗ | Deprecated: Please use `image_file_paths` instead as edits with multiple images are now supported. The image used in the edit. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.png"` |
| `└─ image_file_paths` | ✗ | The image(s) used in the edit, maximum of 10 images. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `["api-assets/id/1234.png", "api-assets/id/1235.png"]` |
| `style` | ✓ |  | `{"model": "Nano Banana", "prompt": "Give me sunglasses"}` |
| `└─ model` | ✗ | The AI model to use for image editing. * `Nano Banana` - Precise, realistic edits with consistent results * `Seedream` - Creative, imaginative images with artistic freedom * `default` - Use the model we recommend, which will change over time. This is recommended unless you need a specific model. This is the default behavior. | `"Nano Banana"` |
| `└─ prompt` | ✓ | The prompt used to edit the image. | `"Give me sunglasses"` |
| `name` | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Ai Image Editor image"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_image_editor.create(
    assets={
        "image_file_path": "api-assets/id/1234.png",
        "image_file_paths": ["api-assets/id/1234.png", "api-assets/id/1235.png"],
    },
    style={"model": "Nano Banana", "prompt": "Give me sunglasses"},
    name="Ai Image Editor image",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_image_editor.create(
    assets={
        "image_file_path": "api-assets/id/1234.png",
        "image_file_paths": ["api-assets/id/1234.png", "api-assets/id/1235.png"],
    },
    style={"model": "Nano Banana", "prompt": "Give me sunglasses"},
    name="Ai Image Editor image",
)

```

#### Response

##### Type
[V1AiImageEditorCreateResponse](/magic_hour/types/models/v1_ai_image_editor_create_response.py)

##### Example
`{"credits_charged": 50, "frame_cost": 50, "id": "cuid-example"}`

