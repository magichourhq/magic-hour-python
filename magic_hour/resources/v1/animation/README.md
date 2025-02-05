
### create <a name="create"></a>
Animation

Create a Animation video. The estimated frame cost is calculated based on the `fps` and `end_seconds` input.

**API Endpoint**: `POST /v1/animation`

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
