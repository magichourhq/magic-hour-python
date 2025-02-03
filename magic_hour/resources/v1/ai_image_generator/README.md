
### create <a name="create"></a>
AI Images

Create an AI image. Each image costs 5 frames.

**API Endpoint**: `POST /v1/ai-image-generator`

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_image_generator.create(
    image_count=1,
    orientation="landscape",
    style={"prompt": "Cool image"},
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
    style={"prompt": "Cool image"},
    name="Ai Image image",
)
```
