
### AI GIFs <a name="create"></a>

Create an AI GIF. Each GIF costs 50 credits.

**API Endpoint**: `POST /v1/ai-gif-generator`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `style` | ✓ |  | `{"prompt": "Cute dancing cat, pixel art"}` |
| `name` | ✗ | The name of gif. This value is mainly used for your own identification of the gif. | `"Ai Gif gif"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_gif_generator.create(
    style={"prompt": "Cute dancing cat, pixel art"}, name="Ai Gif gif"
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_gif_generator.create(
    style={"prompt": "Cute dancing cat, pixel art"}, name="Ai Gif gif"
)

```

#### Response

##### Type
[V1AiGifGeneratorCreateResponse](/magic_hour/types/models/v1_ai_gif_generator_create_response.py)

##### Example
`{"credits_charged": 50, "frame_cost": 50, "id": "cuid-example"}`
