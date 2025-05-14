
### AI Talking Photo <a name="create"></a>

Create a talking photo from an image and audio or text input.

**API Endpoint**: `POST /v1/ai-talking-photo`

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_talking_photo.create(
    assets={
        "audio_file_path": "api-assets/id/1234.mp3",
        "image_file_path": "api-assets/id/1234.png",
    },
    end_seconds=15.0,
    start_seconds=0.0,
    name="Talking Photo image",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_talking_photo.create(
    assets={
        "audio_file_path": "api-assets/id/1234.mp3",
        "image_file_path": "api-assets/id/1234.png",
    },
    end_seconds=15.0,
    start_seconds=0.0,
    name="Talking Photo image",
)
```
