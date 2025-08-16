
### AI Images <a name="create"></a>

Create an AI image. Each image costs 5 credits.

**API Endpoint**: `POST /v1/ai-image-generator`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `image_count` | ✓ | Number of images to generate. | `1` |
| `orientation` | ✓ | The orientation of the output image(s). | `"landscape"` |
| `style` | ✓ | The art style to use for image generation. | `{"prompt": "Cool image", "tool": "ai-anime-generator"}` |
| `name` | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Ai Image image"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_image_generator.create(
    image_count=1,
    orientation="landscape",
    style={"prompt": "Cool image", "tool": "ai-anime-generator"},
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
    style={"prompt": "Cool image", "tool": "ai-anime-generator"},
    name="Ai Image image",
)

```

#### Response

##### Type
[V1AiImageGeneratorCreateResponse](/magic_hour/types/models/v1_ai_image_generator_create_response.py)

##### Example
`{"credits_charged": 5, "frame_cost": 5, "id": "cuid-example"}`
