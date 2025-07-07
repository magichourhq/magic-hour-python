
### Animation <a name="create"></a>

Create a Animation video. The estimated frame cost is calculated based on the `fps` and `end_seconds` input.

**API Endpoint**: `POST /v1/animation`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for animation. | `{"audio_file_path": "api-assets/id/1234.mp3", "audio_source": "file", "image_file_path": "api-assets/id/1234.png"}` |
| `end_seconds` | ✓ | The end time of the input video in seconds | `15.0` |
| `fps` | ✓ | The desire output video frame rate | `12.0` |
| `height` | ✓ | The height of the final output video. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details | `960` |
| `style` | ✓ | Defines the style of the output video | `{"art_style": "Painterly Illustration", "camera_effect": "Accelerate", "prompt": "Cyberpunk city", "prompt_type": "ai_choose", "transition_speed": 5}` |
| `width` | ✓ | The width of the final output video. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details | `512` |
| `name` | ✗ | The name of video | `"Animation video"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.animation.create(
    assets={
        "audio_file_path": "api-assets/id/1234.mp3",
        "audio_source": "file",
        "image_file_path": "api-assets/id/1234.png",
    },
    end_seconds=15.0,
    fps=12.0,
    height=960,
    style={
        "art_style": "Painterly Illustration",
        "camera_effect": "Accelerate",
        "prompt": "Cyberpunk city",
        "prompt_type": "ai_choose",
        "transition_speed": 5,
    },
    width=512,
    name="Animation video",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.animation.create(
    assets={
        "audio_file_path": "api-assets/id/1234.mp3",
        "audio_source": "file",
        "image_file_path": "api-assets/id/1234.png",
    },
    end_seconds=15.0,
    fps=12.0,
    height=960,
    style={
        "art_style": "Painterly Illustration",
        "camera_effect": "Accelerate",
        "prompt": "Cyberpunk city",
        "prompt_type": "ai_choose",
        "transition_speed": 5,
    },
    width=512,
    name="Animation video",
)

```

#### Response

##### Type
[V1AnimationCreateResponse](/magic_hour/types/models/v1_animation_create_response.py)

##### Example
`{"credits_charged": 450, "estimated_frame_cost": 450, "id": "clx7uu86w0a5qp55yxz315r6r"}`
