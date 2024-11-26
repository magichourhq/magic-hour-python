
### create <a name="create"></a>
Create Image-to-Video

Create a Image To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.
  
Get more information about this mode at our [product page](/products/image-to-video).
  

**API Endpoint**: `POST /v1/image-to-video`

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.image_to_video.create(
    data={
        "assets": {"image_file_path": "image/id/1234.png"},
        "end_seconds": 5,
        "height": 960,
        "name": "Image To Video video",
        "style": {"prompt": "string"},
        "width": 512,
    }
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.image_to_video.create(
    data={
        "assets": {"image_file_path": "image/id/1234.png"},
        "end_seconds": 5,
        "height": 960,
        "name": "Image To Video video",
        "style": {"prompt": "string"},
        "width": 512,
    }
)
```

**Upgrade to see all examples**