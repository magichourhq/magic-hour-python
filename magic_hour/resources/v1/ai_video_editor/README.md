# v1.ai_video_editor

## Module Functions

### AI Video Editor <a name="create"></a>

**What this API does**

Create the same Video Editor you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

**Good for**

- Automation and batch processing
- Adding video editor into apps, pipelines, or tools

**How it works (3 steps)**

1. Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
2. Send a request to create a video editor job with the basic fields.
3. Check the job status until it's `complete`, then download the result from `downloads`.

**Key options**

- Inputs: usually a file, sometimes a YouTube link, depending on project type
- Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
- Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

**Cost**\
Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

For detailed examples, see the [product page](https://magichour.ai/products/video-editor).

**API Endpoint**: `POST /v1/ai-video-editor`

#### Parameters

| Parameter            | Required | Description                                                                                                                                                                                                                                                                                                                                      | Example                                         |
| -------------------- | :------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| `assets`             |    ✓     | Provide the assets for video editing.                                                                                                                                                                                                                                                                                                            | `{"video_file_path": "api-assets/id/1234.mp4"}` |
| `└─ video_file_path` |    ✓     | The video to edit. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details. | `"api-assets/id/1234.mp4"`                      |
| `end_seconds`        |    ✓     | End time of your clip in seconds. Must be greater than `start_seconds`. Duration must be between 3 and 10 seconds.                                                                                                                                                                                                                               | `5.0`                                           |
| `style`              |    ✓     |                                                                                                                                                                                                                                                                                                                                                  | `{"prompt": "Change the car color to blue"}`    |
| `└─ prompt`          |    ✓     | The prompt used to edit the video.                                                                                                                                                                                                                                                                                                               | `"Change the car color to blue"`                |
| `name`               |    ✗     | Give your video a custom name for easy identification.                                                                                                                                                                                                                                                                                           | `"My Video Editor video"`                       |
| `start_seconds`      |    ✗     | Start time of your clip (seconds). Must be ≥ 0.                                                                                                                                                                                                                                                                                                  | `0.0`                                           |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_video_editor.create(
    assets={"video_file_path": "api-assets/id/1234.mp4"},
    end_seconds=5.0,
    style={"prompt": "Change the car color to blue"},
    name="My Video Editor video",
    start_seconds=0.0,
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_video_editor.create(
    assets={"video_file_path": "api-assets/id/1234.mp4"},
    end_seconds=5.0,
    style={"prompt": "Change the car color to blue"},
    name="My Video Editor video",
    start_seconds=0.0,
)
```

#### Response

##### Type

[V1AiVideoEditorCreateResponse](/magic_hour/types/models/v1_ai_video_editor_create_response.py)

##### Example

```python
{"credits_charged": 450, "estimated_frame_cost": 450, "id": "cuid-example"}
```
