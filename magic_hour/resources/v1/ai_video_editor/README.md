# v1.ai_video_editor

## Module Functions

<!-- CUSTOM DOCS START -->

### AI Video Editor Generate Workflow <a name="generate"></a>

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
res = client.v1.ai_video_editor.generate(
    assets={"video_file_path": "/path/to/1234.mp4"},
    end_seconds=5.0,
    style={"prompt": "Change the car color to blue"},
    name="My Video Editor video",
    start_seconds=0.0,
    wait_for_completion=True,
    download_outputs=True,
    download_directory=".",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_video_editor.generate(
    assets={"video_file_path": "/path/to/1234.mp4"},
    end_seconds=5.0,
    style={"prompt": "Change the car color to blue"},
    name="My Video Editor video",
    start_seconds=0.0,
    wait_for_completion=True,
    download_outputs=True,
    download_directory=".",
)
```

<!-- CUSTOM DOCS END -->

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
- Resolution: output size and plan requirements vary by workflow and model. Some workflows derive output size from the input video.
- Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

**Cost**\
Credits are charged when the job is queued (`credits_charged` in the response). Tools billed per frame charge an estimate and settle to the frames that actually render once the job finishes; tools billed per second charge the final amount upfront. Failed jobs are refunded.

For detailed examples, see the [product page](https://magichour.ai/products/ai-video-editor).

**API Endpoint**: `POST /v1/ai-video-editor`

#### Parameters

| Parameter            | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Example                                                     |
| -------------------- | :------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `assets`             |    ✓     | Provide the assets for video editing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `{"video_file_path": "api-assets/id/1234.mp4"}`             |
| `└─ video_file_path` |    ✓     | The video to edit. This value is either - a direct URL to the file. The URL path must end in a supported file extension. - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.                                                                                                                                                   | `"api-assets/id/1234.mp4"`                                  |
| `end_seconds`        |    ✓     | End time of your clip in seconds. Must be greater than `start_seconds`. Allowed duration depends on model: `gemini-omni-1.2`: 3-15s, `wan-3.0`: 2-15s, `ltx-2.5`: 0.5-60s (30s at 1080p), `kling-4.0`: 3-30s.                                                                                                                                                                                                                                                                                                                                      | `5.0`                                                       |
| `style`              |    ✓     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `{"prompt": "Change the car color to blue"}`                |
| `└─ prompt`          |    ✓     | The prompt used to edit the video.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `"Change the car color to blue"`                            |
| `model`              |    ✗     | The AI model to use for video editing. Defaults to `ltx-2.5` on free tiers and `gemini-omni-1.2` on paid tiers. * `gemini-omni-1.2`: Best for precise clips up to 15s, references, and high-resolution output. Requires a paid tier. * `wan-3.0`: High-quality video with native audio, long clips, and end-frame control. Requires a paid tier. * `ltx-2.5`: Fastest for general scenes, long clips, audio, and rapid iteration. * `kling-4.0`: Create cinematic videos with image and video references and optional audio. Requires a paid tier. | `"ltx-2.5"`                                                 |
| `name`               |    ✗     | Give your video a custom name for easy identification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `"My Video Editor video"`                                   |
| `references`         |    ✗     | Name references without @ and refer to them as @name in style.prompt. Names must be unique, ignoring case. Maximum 10 references total. Omit for no references. Reference images for gemini-omni-1.2, wan-3.0, kling-4.0.                                                                                                                                                                                                                                                                                                                          | `[{"file_path": "api-assets/id/1234.png", "name": "hero"}]` |
| `resolution`         |    ✗     | Output resolution. Defaults to `480p` for free tier and `720p` for paid. Supported per model: `gemini-omni-1.2`: 360p, 720p, 1080p, 4k; `wan-3.0`: 480p, 720p, 1080p; `ltx-2.5`: 480p, 720p, 1080p; `kling-4.0`: 720p, 1080p.                                                                                                                                                                                                                                                                                                                      | `"480p"`                                                    |
| `start_seconds`      |    ✗     | Start time of your clip (seconds). Must be ≥ 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `0.0`                                                       |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_video_editor.create(
    assets={"video_file_path": "api-assets/id/1234.mp4"},
    end_seconds=5.0,
    style={"prompt": "Change the car color to blue"},
    model="ltx-2.5",
    name="My Video Editor video",
    resolution="480p",
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
    model="ltx-2.5",
    name="My Video Editor video",
    resolution="480p",
    start_seconds=0.0,
)
```

#### Response

##### Type

[V1AiVideoEditorCreateResponse](/magic_hour/types/models/v1_ai_video_editor_create_response.py)

##### Example

```python
{"credits_charged": 450, "estimated_frame_cost": 123, "id": "cuid-example"}
```
