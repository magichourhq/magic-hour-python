
### AI Face Editor <a name="create"></a>

Edit facial features of an image using AI. Each edit costs 1 frame. The height/width of the output image depends on your subscription. Please refer to our [pricing](/pricing) page for more details

**API Endpoint**: `POST /v1/ai-face-editor`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for face editor | `{"image_file_path": "api-assets/id/1234.png"}` |
| `style` | ✓ | Face editing parameters | `{"enhance_face": False, "eye_gaze_horizontal": 0.0, "eye_gaze_vertical": 0.0, "eye_open_ratio": 0.0, "eyebrow_direction": 0.0, "head_pitch": 0.0, "head_roll": 0.0, "head_yaw": 0.0, "lip_open_ratio": 0.0, "mouth_grim": 0.0, "mouth_position_horizontal": 0.0, "mouth_position_vertical": 0.0, "mouth_pout": 0.0, "mouth_purse": 0.0, "mouth_smile": 0.0}` |
| `name` | ✗ | The name of image | `"Face Editor image"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_face_editor.create(
    assets={"image_file_path": "api-assets/id/1234.png"},
    style={
        "enhance_face": False,
        "eye_gaze_horizontal": 0.0,
        "eye_gaze_vertical": 0.0,
        "eye_open_ratio": 0.0,
        "eyebrow_direction": 0.0,
        "head_pitch": 0.0,
        "head_roll": 0.0,
        "head_yaw": 0.0,
        "lip_open_ratio": 0.0,
        "mouth_grim": 0.0,
        "mouth_position_horizontal": 0.0,
        "mouth_position_vertical": 0.0,
        "mouth_pout": 0.0,
        "mouth_purse": 0.0,
        "mouth_smile": 0.0,
    },
    name="Face Editor image",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_face_editor.create(
    assets={"image_file_path": "api-assets/id/1234.png"},
    style={
        "enhance_face": False,
        "eye_gaze_horizontal": 0.0,
        "eye_gaze_vertical": 0.0,
        "eye_open_ratio": 0.0,
        "eyebrow_direction": 0.0,
        "head_pitch": 0.0,
        "head_roll": 0.0,
        "head_yaw": 0.0,
        "lip_open_ratio": 0.0,
        "mouth_grim": 0.0,
        "mouth_position_horizontal": 0.0,
        "mouth_position_vertical": 0.0,
        "mouth_pout": 0.0,
        "mouth_purse": 0.0,
        "mouth_smile": 0.0,
    },
    name="Face Editor image",
)

```

#### Response

##### Type
[V1AiFaceEditorCreateResponse](/magic_hour/types/models/v1_ai_face_editor_create_response.py)

##### Example
`{"credits_charged": 1, "frame_cost": 1, "id": "clx7uu86w0a5qp55yxz315r6r"}`
