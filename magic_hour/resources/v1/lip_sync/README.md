
### Lip Sync <a name="create"></a>

Create a Lip Sync video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.
  
Get more information about this mode at our [product page](/products/lip-sync).
  

**API Endpoint**: `POST /v1/lip-sync`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for lip-sync. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used | `{"audio_file_path": "api-assets/id/1234.mp3", "video_file_path": "api-assets/id/1234.mp4", "video_source": "file"}` |
| `end_seconds` | ✓ | The end time of the input video in seconds | `15.0` |
| `start_seconds` | ✓ | The start time of the input video in seconds | `0.0` |
| `height` | ✗ | Used to determine the dimensions of the output video.     * If height is provided, width will also be required. The larger value between width and height will be used to determine the maximum output resolution while maintaining the original aspect ratio. * If both height and width are omitted, the video will be resized according to your subscription's maximum resolution, while preserving aspect ratio.  Note: if the video's original resolution is less than the maximum, the video will not be resized.  See our [pricing page](https://magichour.ai/pricing) for more details. | `960` |
| `max_fps_limit` | ✗ | Defines the maximum FPS (frames per second) for the output video. If the input video's FPS is lower than this limit, the output video will retain the input FPS. This is useful for reducing unnecessary frame usage in scenarios where high FPS is not required. | `12.0` |
| `name` | ✗ | The name of video | `"Lip Sync video"` |
| `width` | ✗ | Used to determine the dimensions of the output video.     * If width is provided, height will also be required. The larger value between width and height will be used to determine the maximum output resolution while maintaining the original aspect ratio. * If both height and width are omitted, the video will be resized according to your subscription's maximum resolution, while preserving aspect ratio.  Note: if the video's original resolution is less than the maximum, the video will not be resized.  See our [pricing page](https://magichour.ai/pricing) for more details. | `512` |

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
    start_seconds=0.0,
    height=960,
    max_fps_limit=12.0,
    name="Lip Sync video",
    width=512,
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
    start_seconds=0.0,
    height=960,
    max_fps_limit=12.0,
    name="Lip Sync video",
    width=512,
)

```

#### Response

##### Type
[V1LipSyncCreateResponse](/magic_hour/types/models/v1_lip_sync_create_response.py)

##### Example
`{"credits_charged": 450, "estimated_frame_cost": 450, "id": "clx7uu86w0a5qp55yxz315r6r"}`
