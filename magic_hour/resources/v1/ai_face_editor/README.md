# v1.ai_face_editor

## Module Functions






<!-- CUSTOM DOCS START -->

### Ai Face Editor Generate Workflow <a name="generate"></a>

The workflow performs the following action

1. upload local assets to Magic Hour storage. So you can pass in a local path instead of having to upload files yourself
2. trigger a generation
3. poll for a completion status. This is configurable
4. if success, download the output to local directory

> [!TIP]
> This is the recommended way to use the SDK unless you have specific needs where it is necessary to split up the actions.

#### Parameters

In Additional to the parameters listed in the `.create` section below, `.generate` introduces 3 new parameters:

- `wait_for_completion` (bool, default True): Whether to wait for the project to complete.
- `download_outputs` (bool, default True): Whether to download the generated files
- `download_directory` (str, optional): Directory to save downloaded files (defaults to current directory)

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_face_editor.generate(
    assets={"image_file_path": "/path/to/1234.png"},
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
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_face_editor.generate(
    assets={"image_file_path": "/path/to/1234.png"},
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
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### AI Face Editor <a name="create"></a>

Edit facial features of an image using AI. Each edit costs 1 frame. The height/width of the output image depends on your subscription. Please refer to our [pricing](/pricing) page for more details

**API Endpoint**: `POST /v1/ai-face-editor`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for face editor | `{"image_file_path": "api-assets/id/1234.png"}` |
| `└─ image_file_path` | ✓ | This is the image whose face will be edited. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.png"` |
| `style` | ✓ | Face editing parameters | `{"enhance_face": False, "eye_gaze_horizontal": 0.0, "eye_gaze_vertical": 0.0, "eye_open_ratio": 0.0, "eyebrow_direction": 0.0, "head_pitch": 0.0, "head_roll": 0.0, "head_yaw": 0.0, "lip_open_ratio": 0.0, "mouth_grim": 0.0, "mouth_position_horizontal": 0.0, "mouth_position_vertical": 0.0, "mouth_pout": 0.0, "mouth_purse": 0.0, "mouth_smile": 0.0}` |
| `└─ enhance_face` | ✗ | Enhance face features | `False` |
| `└─ eye_gaze_horizontal` | ✗ | Horizontal eye gaze (-100 to 100), in increments of 5 | `0.0` |
| `└─ eye_gaze_vertical` | ✗ | Vertical eye gaze (-100 to 100), in increments of 5 | `0.0` |
| `└─ eye_open_ratio` | ✗ | Eye open ratio (-100 to 100), in increments of 5 | `0.0` |
| `└─ eyebrow_direction` | ✗ | Eyebrow direction (-100 to 100), in increments of 5 | `0.0` |
| `└─ head_pitch` | ✗ | Head pitch (-100 to 100), in increments of 5 | `0.0` |
| `└─ head_roll` | ✗ | Head roll (-100 to 100), in increments of 5 | `0.0` |
| `└─ head_yaw` | ✗ | Head yaw (-100 to 100), in increments of 5 | `0.0` |
| `└─ lip_open_ratio` | ✗ | Lip open ratio (-100 to 100), in increments of 5 | `0.0` |
| `└─ mouth_grim` | ✗ | Mouth grim (-100 to 100), in increments of 5 | `0.0` |
| `└─ mouth_position_horizontal` | ✗ | Horizontal mouth position (-100 to 100), in increments of 5 | `0.0` |
| `└─ mouth_position_vertical` | ✗ | Vertical mouth position (-100 to 100), in increments of 5 | `0.0` |
| `└─ mouth_pout` | ✗ | Mouth pout (-100 to 100), in increments of 5 | `0.0` |
| `└─ mouth_purse` | ✗ | Mouth purse (-100 to 100), in increments of 5 | `0.0` |
| `└─ mouth_smile` | ✗ | Mouth smile (-100 to 100), in increments of 5 | `0.0` |
| `name` | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Face Editor image"` |

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
`{"credits_charged": 1, "frame_cost": 1, "id": "cuid-example"}`

