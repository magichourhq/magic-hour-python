
### AI Photo Editor <a name="create"></a>

> **NOTE**: this API is still in early development stages, and should be avoided. Please reach out to us if you're interested in this API. 

Edit photo using AI. Each photo costs 10 credits.

**API Endpoint**: `POST /v1/ai-photo-editor`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for photo editor | `{"image_file_path": "api-assets/id/1234.png"}` |
| `resolution` | ✓ | The resolution of the final output image. The allowed value is based on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details | `768` |
| `style` | ✓ |  | `{"image_description": "A photo of a person", "likeness_strength": 5.2, "negative_prompt": "painting, cartoon, sketch", "prompt": "A photo portrait of a person wearing a hat", "prompt_strength": 3.75, "steps": 4, "upscale_factor": 2, "upscale_fidelity": 0.5}` |
| `name` | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Photo Editor image"` |
| `steps` | ✗ | Deprecated: Please use `.style.steps` instead. Number of iterations used to generate the output. Higher values improve quality and increase the strength of the prompt but increase processing time. | `123` |

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
