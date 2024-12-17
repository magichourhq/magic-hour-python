
### create <a name="create"></a>
Create Animation

Create a Animation video. The estimated frame cost is calculated based on the `fps` and `end_seconds` input.

**API Endpoint**: `POST /v1/animation`

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.animation.create(
    assets={"audio_source": "file"},
    end_seconds=15,
    fps=12,
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
    assets={"audio_source": "file"},
    end_seconds=15,
    fps=12,
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

**Upgrade to see all examples**
