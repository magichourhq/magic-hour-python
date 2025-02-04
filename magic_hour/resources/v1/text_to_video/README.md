
### create <a name="create"></a>
Text-to-Video

Create a Text To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.
  
Get more information about this mode at our [product page](/products/text-to-video).
  

**API Endpoint**: `POST /v1/text-to-video`

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.text_to_video.create(
    end_seconds=5.0,
    orientation="landscape",
    style={"prompt": "string"},
    name="Text To Video video",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.text_to_video.create(
    end_seconds=5.0,
    orientation="landscape",
    style={"prompt": "string"},
    name="Text To Video video",
)
```
