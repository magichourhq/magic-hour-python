# v1.audio_to_video

## Module Functions

<!-- CUSTOM DOCS START -->

### Audio To Video Generate Workflow <a name="generate"></a>

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
res = client.v1.audio_to_video.generate(
    assets={
        "audio_file_path": "/path/to/1234.mp3",
        "image_file_path": "/path/to/1234.png",
    },
    end_seconds=15.0,
    name="My Audio To Video video",
    resolution="720p",
    start_seconds=0.0,
    style={"prompt": "Car driving through a city"},
    wait_for_completion=True,
    download_outputs=True,
    download_directory="."
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.audio_to_video.generate(
    assets={
        "audio_file_path": "/path/to/1234.mp3",
        "image_file_path": "/path/to/1234.png",
    },
    end_seconds=15.0,
    name="My Audio To Video video",
    resolution="720p",
    start_seconds=0.0,
    style={"prompt": "Car driving through a city"},
    wait_for_completion=True,
    download_outputs=True,
    download_directory="."
)
```

<!-- CUSTOM DOCS END -->

### Audio-to-Video <a name="create"></a>

**What this API does**

Create the same Audio To Video you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

**Good for**

- Automation and batch processing
- Adding audio to video into apps, pipelines, or tools

**How it works (3 steps)**

1. Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
2. Send a request to create a audio to video job with the basic fields.
3. Check the job status until it's `complete`, then download the result from `downloads`.

**Key options**

- Inputs: usually a file, sometimes a YouTube link, depending on project type
- Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
- Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

**Cost**\
Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

For detailed examples, see the [product page](https://magichour.ai/products/audio-to-video).

**API Endpoint**: `POST /v1/audio-to-video`

#### Parameters

| Parameter            | Required | Description                                                                                                                                                                                                                                                                                                                                                                       | Example                                                                                      |
| -------------------- | :------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `assets`             |    ✓     | Provide the audio file and an optional reference image.                                                                                                                                                                                                                                                                                                                           | `{"audio_file_path": "api-assets/id/1234.mp3", "image_file_path": "api-assets/id/1234.png"}` |
| `└─ audio_file_path` |    ✓     | The path of the audio file. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.                         | `"api-assets/id/1234.mp3"`                                                                   |
| `└─ image_file_path` |    ✗     | Reference image for the initial frame of the video. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details. | `"api-assets/id/1234.png"`                                                                   |
| `end_seconds`        |    ✓     | End time of your clip (seconds). Must be greater than start_seconds.                                                                                                                                                                                                                                                                                                              | `15.0`                                                                                       |
| `name`               |    ✗     | Give your video a custom name for easy identification.                                                                                                                                                                                                                                                                                                                            | `"My Audio To Video video"`                                                                  |
| `resolution`         |    ✗     | Output video resolution. Defaults to `720p` on paid tiers and `480p` on free tiers.                                                                                                                                                                                                                                                                                               | `"720p"`                                                                                     |
| `start_seconds`      |    ✗     | Start time of your clip (seconds). Must be ≥ 0.                                                                                                                                                                                                                                                                                                                                   | `0.0`                                                                                        |
| `style`              |    ✗     | Attributes used to dictate the style of the output                                                                                                                                                                                                                                                                                                                                | `{"prompt": "Car driving through a city"}`                                                   |
| `└─ prompt`          |    ✗     | Prompt to guide the visual style of the video.                                                                                                                                                                                                                                                                                                                                    | `"Car driving through a city"`                                                               |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.audio_to_video.create(
    assets={
        "audio_file_path": "api-assets/id/1234.mp3",
        "image_file_path": "api-assets/id/1234.png",
    },
    end_seconds=15.0,
    name="My Audio To Video video",
    resolution="720p",
    start_seconds=0.0,
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.audio_to_video.create(
    assets={
        "audio_file_path": "api-assets/id/1234.mp3",
        "image_file_path": "api-assets/id/1234.png",
    },
    end_seconds=15.0,
    name="My Audio To Video video",
    resolution="720p",
    start_seconds=0.0,
)
```

#### Response

##### Type

[V1AudioToVideoCreateResponse](/magic_hour/types/models/v1_audio_to_video_create_response.py)

##### Example

```python
{"credits_charged": 450, "estimated_frame_cost": 123, "id": "cuid-example"}
```
