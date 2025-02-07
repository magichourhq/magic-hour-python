
### create <a name="create"></a>
Lip Sync

Create a Lip Sync video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.
  
Get more information about this mode at our [product page](/products/lip-sync).
  

**API Endpoint**: `POST /v1/lip-sync`

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.lip_sync.create(
    assets={
        "audio_file_path": "api-assets/id/1234.mp3",
        "video_file_path": "api-assets/id/1234.mp4",
        "video_source": "file",
    },
    end_seconds=15.0,
    height=960,
    start_seconds=0.0,
    width=512,
    max_fps_limit=12.0,
    name="Lip Sync video",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.lip_sync.create(
    assets={
        "audio_file_path": "api-assets/id/1234.mp3",
        "video_file_path": "api-assets/id/1234.mp4",
        "video_source": "file",
    },
    end_seconds=15.0,
    height=960,
    start_seconds=0.0,
    width=512,
    max_fps_limit=12.0,
    name="Lip Sync video",
)
```
