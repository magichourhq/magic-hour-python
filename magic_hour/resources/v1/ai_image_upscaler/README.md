
### create <a name="create"></a>
Create Upscaled Image

Upscale your image using AI. Each 2x upscale costs 50 frames, and 4x upscale costs 200 frames.

**API Endpoint**: `POST /v1/ai-image-upscaler`

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_image_upscaler.create(
    assets={"image_file_path": "image/id/1234.png"},
    scale_factor=123.45,
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
    assets={"image_file_path": "image/id/1234.png"},
    scale_factor=123.45,
    style={"enhancement": "Balanced"},
    name="Image Upscaler image",
)
```

**Upgrade to see all examples**
