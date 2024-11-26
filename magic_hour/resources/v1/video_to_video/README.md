
### create <a name="create"></a>
Create Video-to-Video

Create a Video To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.
  
Get more information about this mode at our [product page](/products/video-to-video).
  

**API Endpoint**: `POST /v1/video-to-video`

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.video_to_video.create(
    data={
        "assets": {
            "video_file_path": "video/id/1234.mp4",
            "video_source": "file",
            "youtube_url": "http://www.example.com",
        },
        "end_seconds": 15,
        "fps_resolution": "HALF",
        "height": 960,
        "name": "Video To Video video",
        "start_seconds": 0,
        "style": {
            "art_style": "3D Render",
            "model": "Absolute Reality",
            "prompt": "string",
            "prompt_type": "append_default",
            "version": "default",
        },
        "width": 512,
    }
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.video_to_video.create(
    data={
        "assets": {
            "video_file_path": "video/id/1234.mp4",
            "video_source": "file",
            "youtube_url": "http://www.example.com",
        },
        "end_seconds": 15,
        "fps_resolution": "HALF",
        "height": 960,
        "name": "Video To Video video",
        "start_seconds": 0,
        "style": {
            "art_style": "3D Render",
            "model": "Absolute Reality",
            "prompt": "string",
            "prompt_type": "append_default",
            "version": "default",
        },
        "width": 512,
    }
)
```

**Upgrade to see all examples**
