# v1.ai_image_generator

## Module Functions






<!-- CUSTOM DOCS START -->

### Ai Image Generator Generate Workflow <a name="generate"></a>

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
res = client.v1.ai_image_generator.generate(
    image_count=1,
    orientation="landscape",
    style={"prompt": "Cool image", "tool": "ai-anime-generator"},
    name="Ai Image image",
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
res = await client.v1.ai_image_generator.generate(
    image_count=1,
    orientation="landscape",
    style={"prompt": "Cool image", "tool": "ai-anime-generator"},
    name="Ai Image image",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### AI Image Generator <a name="create"></a>

Create an AI image. Each standard image costs 5 credits. Pro quality images cost 30 credits.

**API Endpoint**: `POST /v1/ai-image-generator`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `image_count` | ✓ | Number of images to generate. | `1` |
| `orientation` | ✓ | The orientation of the output image(s). | `"landscape"` |
| `style` | ✓ | The art style to use for image generation. | `{"prompt": "Cool image", "quality_mode": "standard", "tool": "ai-anime-generator"}` |
| `└─ prompt` | ✓ | The prompt used for the image(s). | `"Cool image"` |
| `└─ quality_mode` | ✗ | Controls the quality of the generated image. Defaults to 'standard' if not specified.  **Options:** - `standard` - Standard quality generation. Cost: 5 credits per image. - `pro` - Pro quality generation with enhanced details and quality. Cost: 30 credits per image.  Note: Pro mode is available for users on Creator, Pro, or Business tier. | `"standard"` |
| `└─ tool` | ✗ | The art style to use for image generation. Defaults to 'general' if not provided. | `"ai-anime-generator"` |
| `name` | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Ai Image image"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_image_generator.create(
    image_count=1,
    orientation="landscape",
    style={
        "prompt": "Cool image",
        "quality_mode": "standard",
        "tool": "ai-anime-generator",
    },
    name="Ai Image image",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_image_generator.create(
    image_count=1,
    orientation="landscape",
    style={
        "prompt": "Cool image",
        "quality_mode": "standard",
        "tool": "ai-anime-generator",
    },
    name="Ai Image image",
)

```

#### Response

##### Type
[V1AiImageGeneratorCreateResponse](/magic_hour/types/models/v1_ai_image_generator_create_response.py)

##### Example
`{"credits_charged": 5, "frame_cost": 5, "id": "cuid-example"}`

