
### AI Talking Photo <a name="create"></a>

Create a talking photo from an image and audio or text input.

**API Endpoint**: `POST /v1/ai-talking-photo`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for creating a talking photo | `{"audio_file_path": "api-assets/id/1234.mp3", "image_file_path": "api-assets/id/1234.png"}` |
| `end_seconds` | ✓ | The end time of the input audio in seconds. The maximum duration allowed is 60 seconds. | `15.0` |
| `start_seconds` | ✓ | The start time of the input audio in seconds. The maximum duration allowed is 60 seconds. | `0.0` |
| `name` | ✗ | The name of image | `"Talking Photo image"` |
| `style` | ✗ | Attributes used to dictate the style of the output | `{"generation_mode": "expressive", "intensity": 1.5}` |

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

#### Response

##### Type
[V1AiTalkingPhotoCreateResponse](/magic_hour/types/models/v1_ai_talking_photo_create_response.py)

##### Example
`{"credits_charged": 450, "estimated_frame_cost": 450, "id": "clx7uu86w0a5qp55yxz315r6r"}`
