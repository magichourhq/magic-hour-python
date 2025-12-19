# v1.ai_photo_editor

## Module Functions






<!-- CUSTOM DOCS START -->

### Ai Photo Editor Generate Workflow <a name="generate"></a>

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
res = client.v1.ai_photo_editor.generate(
    assets={"image_file_path": "/path/to/1234.png"},
    resolution=768,
    style={
        "image_description": "A photo of a person",
        "likeness_strength": 5.2,
        "negative_prompt": "painting, cartoon, sketch",
        "prompt": "A photo portrait of a person wearing a hat",
        "prompt_strength": 3.75,
        "steps": 4,
        "upscale_factor": 2,
        "upscale_fidelity": 0.5,
    },
    name="Photo Editor image",
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
res = await client.v1.ai_photo_editor.generate(
    assets={"image_file_path": "/path/to/1234.png"},
    resolution=768,
    style={
        "image_description": "A photo of a person",
        "likeness_strength": 5.2,
        "negative_prompt": "painting, cartoon, sketch",
        "prompt": "A photo portrait of a person wearing a hat",
        "prompt_strength": 3.75,
        "steps": 4,
        "upscale_factor": 2,
        "upscale_fidelity": 0.5,
    },
    name="Photo Editor image",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### AI Photo Editor <a name="create"></a>

> **NOTE**: this API is still in early development stages, and should be avoided. Please reach out to us if you're interested in this API. 

Edit photo using AI. Each photo costs 10 credits.

**API Endpoint**: `POST /v1/ai-photo-editor`

#### Parameters

| Parameter | Required | Deprecated | Description | Example |
|-----------|:--------:|:----------:|-------------|--------|
| `assets` | ✓ | ✗ | Provide the assets for photo editor | `{"image_file_path": "api-assets/id/1234.png"}` |
| `└─ image_file_path` | ✓ | — | The image used to generate the output. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.png"` |
| `resolution` | ✓ | ✗ | The resolution of the final output image. The allowed value is based on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details | `768` |
| `style` | ✓ | ✗ |  | `{"image_description": "A photo of a person", "likeness_strength": 5.2, "negative_prompt": "painting, cartoon, sketch", "prompt": "A photo portrait of a person wearing a hat", "prompt_strength": 3.75, "steps": 4, "upscale_factor": 2, "upscale_fidelity": 0.5}` |
| `└─ image_description` | ✓ | — | Use this to describe what your input image is. This helps maintain aspects of the image you don't want to change. | `"A photo of a person"` |
| `└─ likeness_strength` | ✓ | — | Determines the input image's influence. Higher values align the output more with the initial image. | `5.2` |
| `└─ negative_prompt` | ✗ | — | What you want to avoid seeing in the final output; has a minor effect. | `"painting, cartoon, sketch"` |
| `└─ prompt` | ✓ | — | What you want your final output to look like. We recommend starting with the image description and making minor edits for best results. | `"A photo portrait of a person wearing a hat"` |
| `└─ prompt_strength` | ✓ | — | Determines the prompt's influence. Higher values align the output more with the prompt. | `3.75` |
| `└─ steps` | ✗ | — | Number of iterations used to generate the output. Higher values improve quality and increase the strength of the prompt but increase processing time. | `4` |
| `└─ upscale_factor` | ✗ | — | The multiplier applied to an image's original dimensions during the upscaling process. For example, a scale of 2 doubles the width and height (e.g., from 512x512 to 1024x1024). | `2` |
| `└─ upscale_fidelity` | ✗ | — | Upscale fidelity refers to the level of quality desired in the generated image. Fidelity value of 1 means more details. | `0.5` |
| `name` | ✗ | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Photo Editor image"` |
| `steps` | ✗ | ✓ | Deprecated: Please use `.style.steps` instead. Number of iterations used to generate the output. Higher values improve quality and increase the strength of the prompt but increase processing time. | `123` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_photo_editor.create(
    assets={"image_file_path": "api-assets/id/1234.png"},
    resolution=768,
    style={
        "image_description": "A photo of a person",
        "likeness_strength": 5.2,
        "negative_prompt": "painting, cartoon, sketch",
        "prompt": "A photo portrait of a person wearing a hat",
        "prompt_strength": 3.75,
        "steps": 4,
        "upscale_factor": 2,
        "upscale_fidelity": 0.5,
    },
    name="Photo Editor image",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_photo_editor.create(
    assets={"image_file_path": "api-assets/id/1234.png"},
    resolution=768,
    style={
        "image_description": "A photo of a person",
        "likeness_strength": 5.2,
        "negative_prompt": "painting, cartoon, sketch",
        "prompt": "A photo portrait of a person wearing a hat",
        "prompt_strength": 3.75,
        "steps": 4,
        "upscale_factor": 2,
        "upscale_fidelity": 0.5,
    },
    name="Photo Editor image",
)

```

#### Response

##### Type
[V1AiPhotoEditorCreateResponse](/magic_hour/types/models/v1_ai_photo_editor_create_response.py)

##### Example
`{"credits_charged": 10, "frame_cost": 10, "id": "cuid-example"}`

