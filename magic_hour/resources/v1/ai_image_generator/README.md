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
    style={
        "prompt": "Cool image",
        "tool": "ai-anime-generator",
    },
    aspect_ratio="1:1",
    model="default",
    name="My Ai Image image",
    resolution="auto",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="."
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
    download_directory="."
)
```

<!-- CUSTOM DOCS END -->

### AI Image Generator <a name="create"></a>

Create an AI image with advanced model selection and quality controls.

**API Endpoint**: `POST /v1/ai-image-generator`

#### Parameters

| Parameter         | Required | Deprecated | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Example                                                  |
| ----------------- | :------: | :--------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| `image_count`     |    ✓     |     ✗      | Number of images to generate. Maximum varies by model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `1`                                                      |
| `style`           |    ✓     |     ✗      | The art style to use for image generation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `{"prompt": "Cool image", "tool": "ai-anime-generator"}` |
| `└─ prompt`       |    ✓     |     —      | The prompt used for the image(s).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `"Cool image"`                                           |
| `└─ quality_mode` |    ✗     |     ✓      | DEPRECATED: Use `model` field instead for explicit model selection. Legacy quality mode mapping: - `standard` → `z-image-turbo` model - `pro` → `seedream-v4` model If model is specified, it will take precedence over the legacy quality_mode field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `"pro"`                                                  |
| `└─ tool`         |    ✗     |     —      | The art style to use for image generation. Defaults to 'general' if not provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `"ai-anime-generator"`                                   |
| `aspect_ratio`    |    ✗     |     ✗      | The aspect ratio of the output image(s). If not specified, defaults to `1:1` (square).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `"1:1"`                                                  |
| `model`           |    ✗     |     ✗      | The AI model to use for image generation. Each model has different capabilities and costs. **Models:** - `default` - Use the model we recommend, which will change over time. This is recommended unless you need a specific model. This is the default behavior. - `flux-schnell` - from 5 credits/image - Supported resolutions: 640px, 1k, 2k - Available for tiers: free, creator, pro, business - Image count allowed: 1, 2, 3, 4 - `z-image-turbo` - from 5 credits/image - Supported resolutions: 640px, 1k, 2k - Available for tiers: free, creator, pro, business - Image count allowed: 1, 2, 3, 4 - `seedream-v4` - from 40 credits/image - Supported resolutions: 640px, 1k, 2k, 4k - Available for tiers: free, creator, pro, business - Image count allowed: 1, 2, 3, 4 - `nano-banana` - from 50 credits/image - Supported resolutions: 640px, 1k - Available for tiers: free, creator, pro, business - Image count allowed: 1, 2, 3, 4 - `nano-banana-2` - from 100 credits/image - Supported resolutions: 640px, 1k, 2k, 4k - Available for tiers: free, creator, pro, business - Image count allowed: 1, 4, 9, 16 - `nano-banana-pro` - from 150 credits/image - Supported resolutions: 1k, 2k, 4k - Available for tiers: creator, pro, business - Image count allowed: 1, 4, 9, 16 **Deprecated Enum Values:** - `seedream` - Use `seedream-v4` instead. | `"default"`                                              |
| `name`            |    ✗     |     ✗      | Give your image a custom name for easy identification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `"My Ai Image image"`                                    |
| `orientation`     |    ✗     |     ✓      | DEPRECATED: Use `aspect_ratio` instead. The orientation of the output image(s). `aspect_ratio` takes precedence when `orientation` if both are provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `"landscape"`                                            |
| `resolution`      |    ✗     |     ✗      | Maximum resolution (longest edge) for the output image. **Options:** - `640px` — up to 640px - `1k` — up to 1024px - `2k` — up to 2048px - `4k` — up to 4096px - `auto` — **Deprecated.** Mapped server-side from your subscription tier to the best matching resolution the model supports **Per-model support:** - `flux-schnell` - 640px, 1k, 2k - `z-image-turbo` - 640px, 1k, 2k - `seedream-v4` - 640px, 1k, 2k, 4k - `nano-banana` - 640px, 1k - `nano-banana-2` - 640px, 1k, 2k, 4k - `nano-banana-pro` - 1k, 2k, 4k Note: Resolution availability depends on the model and your subscription tier.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `"auto"`                                                 |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_image_generator.create(
    image_count=1,
    style={"prompt": "Cool image", "tool": "ai-anime-generator"},
    aspect_ratio="1:1",
    model="default",
    name="My Ai Image image",
    resolution="auto",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_image_generator.create(
    image_count=1,
    style={"prompt": "Cool image", "tool": "ai-anime-generator"},
    aspect_ratio="1:1",
    model="default",
    name="My Ai Image image",
    resolution="auto",
)
```

#### Response

##### Type

[V1AiImageGeneratorCreateResponse](/magic_hour/types/models/v1_ai_image_generator_create_response.py)

##### Example

```python
{"credits_charged": 5, "frame_cost": 5, "id": "cuid-example"}
```
