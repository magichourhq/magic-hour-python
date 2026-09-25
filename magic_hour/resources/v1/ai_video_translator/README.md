# v1.ai_video_translator

## Module Functions

### AI Video Translator <a name="create"></a>

**What this API does**

Create the same Video Translator you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

**Good for**

- Automation and batch processing
- Adding video translator into apps, pipelines, or tools

**How it works (3 steps)**

1. Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
2. Send a request to create a video translator job with the basic fields.
3. Check the job status until it's `complete`, then download the result from `downloads`.

**Key options**

- Inputs: usually a file, sometimes a YouTube link, depending on project type
- Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
- Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

**Cost**\
Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

For detailed examples, see the [product page](https://magichour.ai/products/ai-video-translator).

**API Endpoint**: `POST /v1/ai-video-translator`

#### Parameters

| Parameter            | Required | Description                                                                                                                                                                                                                                                                                                                                                                    | Example                                         |
| -------------------- | :------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| `assets`             |    ✓     | Source video for the translation job.                                                                                                                                                                                                                                                                                                                                          | `{"video_file_path": "api-assets/id/1234.mp4"}` |
| `└─ video_file_path` |    ✓     | Source video containing the speech to translate. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details. | `"api-assets/id/1234.mp4"`                      |
| `end_seconds`        |    ✓     | End time of your clip (seconds). Must be greater than start_seconds. The clip must be 1-30 seconds long.                                                                                                                                                                                                                                                                       | `15.0`                                          |
| `target_language`    |    ✓     | Language to translate the video's speech into.                                                                                                                                                                                                                                                                                                                                 | `"Spanish"`                                     |
| `name`               |    ✗     | Give your video a custom name for easy identification.                                                                                                                                                                                                                                                                                                                         | `"My Video Translator video"`                   |
| `resolution`         |    ✗     | Output video resolution. Defaults to 480p. 720p and 1080p require a paid plan.                                                                                                                                                                                                                                                                                                 | `"720p"`                                        |
| `start_seconds`      |    ✗     | Start time of your clip (seconds). Must be ≥ 0.                                                                                                                                                                                                                                                                                                                                | `0.0`                                           |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_video_translator.create(
    assets={"video_file_path": "api-assets/id/1234.mp4"},
    end_seconds=15.0,
    target_language="Spanish",
    name="My Video Translator video",
    resolution="720p",
    start_seconds=0.0,
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_video_translator.create(
    assets={"video_file_path": "api-assets/id/1234.mp4"},
    end_seconds=15.0,
    target_language="Spanish",
    name="My Video Translator video",
    resolution="720p",
    start_seconds=0.0,
)
```

#### Response

##### Type

[V1AiVideoTranslatorCreateResponse](/magic_hour/types/models/v1_ai_video_translator_create_response.py)

##### Example

```python
{"credits_charged": 450, "estimated_frame_cost": 123, "id": "cuid-example"}
```
