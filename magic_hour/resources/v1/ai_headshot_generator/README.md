
### AI Headshots <a name="create"></a>

Create an AI headshot. Each headshot costs 50 credits.

**API Endpoint**: `POST /v1/ai-headshot-generator`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for headshot photo | `{"image_file_path": "api-assets/id/1234.png"}` |
| `name` | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Ai Headshot image"` |
| `style` | ✗ |  | `{}` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_headshot_generator.create(
    assets={"image_file_path": "api-assets/id/1234.png"}, name="Ai Headshot image"
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_headshot_generator.create(
    assets={"image_file_path": "api-assets/id/1234.png"}, name="Ai Headshot image"
)

```

#### Response

##### Type
[V1AiHeadshotGeneratorCreateResponse](/magic_hour/types/models/v1_ai_headshot_generator_create_response.py)

##### Example
`{"credits_charged": 50, "frame_cost": 50, "id": "cuid-example"}`
