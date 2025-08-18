
### AI Image Editor <a name="create"></a>

Edit images with AI. Each edit costs 50 credits.

**API Endpoint**: `POST /v1/ai-image-editor`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for image edit | `{"image_file_path": "api-assets/id/1234.png"}` |
| `style` | ✓ |  | `{"prompt": "Give me sunglasses"}` |
| `name` | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Ai Image Editor image"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_image_editor.create(
    assets={"image_file_path": "api-assets/id/1234.png"},
    style={"prompt": "Give me sunglasses"},
    name="Ai Image Editor image",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_image_editor.create(
    assets={"image_file_path": "api-assets/id/1234.png"},
    style={"prompt": "Give me sunglasses"},
    name="Ai Image Editor image",
)

```

#### Response

##### Type
[V1AiImageEditorCreateResponse](/magic_hour/types/models/v1_ai_image_editor_create_response.py)

##### Example
`{"credits_charged": 50, "frame_cost": 50, "id": "cuid-example"}`
