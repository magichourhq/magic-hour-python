
### Text-to-Video <a name="create"></a>

Create a Text To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.
  
Get more information about this mode at our [product page](/products/text-to-video).
  

**API Endpoint**: `POST /v1/text-to-video`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `end_seconds` | ✓ | The total duration of the output video in seconds. | `5.0` |
| `orientation` | ✓ | Determines the orientation of the output video | `"landscape"` |
| `style` | ✓ |  | `{"prompt": "a dog running"}` |
| `name` | ✗ | The name of video | `"Text To Video video"` |
| `resolution` | ✗ | Controls the output video resolution. Defaults to `720p` if not specified.  **Options:** - `480p` - Supports only 5 or 10 second videos. Output: 24fps. Cost: 120 credits per 5 seconds. - `720p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 300 credits per 5 seconds. - `1080p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 600 credits per 5 seconds. **Requires** `pro` or `business` tier. | `"1080p"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.text_to_video.create(
    end_seconds=5.0,
    orientation="landscape",
    style={"prompt": "a dog running"},
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
    style={"prompt": "a dog running"},
    name="Text To Video video",
)

```

#### Response

##### Type
[V1TextToVideoCreateResponse](/magic_hour/types/models/v1_text_to_video_create_response.py)

##### Example
`{"credits_charged": 450, "estimated_frame_cost": 450, "id": "clx7uu86w0a5qp55yxz315r6r"}`
