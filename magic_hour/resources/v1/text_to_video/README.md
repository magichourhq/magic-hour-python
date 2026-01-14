# v1.text_to_video

## Module Functions

<!-- CUSTOM DOCS START -->

### Text To Video Generate Workflow <a name="generate"></a>

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
res = client.v1.text_to_video.generate(
    end_seconds=5.0,
    orientation="landscape",
    style={"prompt": "a dog running"},
    name="Text To Video video",
    resolution="720p",
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
res = await client.v1.text_to_video.generate(
    end_seconds=5.0,
    orientation="landscape",
    style={"prompt": "a dog running"},
    name="Text To Video video",
    resolution="720p",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->

### Text-to-Video <a name="create"></a>

**What this API does**

Create the same Text To Video you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

**Good for**

- Automation and batch processing
- Adding text to video into apps, pipelines, or tools

**How it works (3 steps)**

1. Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
2. Send a request to create a text to video job with the basic fields.
3. Check the job status until it's `complete`, then download the result from `downloads`.

**Key options**

- Inputs: usually a file, sometimes a YouTube link, depending on project type
- Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
- Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

**Cost**\
Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

For detailed examples, see the [product page](https://magichour.ai/products/text-to-video).

**API Endpoint**: `POST /v1/text-to-video`

#### Parameters

| Parameter         | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Example                       |
| ----------------- | :------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `end_seconds`     |    ✓     | The total duration of the output video in seconds. The value must be greater than or equal to 5 seconds and less than or equal to 60 seconds. Note: For 480p resolution, the value must be either 5 or 10.                                                                                                                                                                                                                                                                                              | `5.0`                         |
| `orientation`     |    ✓     | Determines the orientation of the output video                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `"landscape"`                 |
| `style`           |    ✓     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `{"prompt": "a dog running"}` |
| `└─ prompt`       |    ✓     | The prompt used for the video.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `"a dog running"`             |
| `└─ quality_mode` |    ✗     | DEPRECATED: Please use `resolution` field instead. For backward compatibility: * `quick` maps to 720p resolution * `studio` maps to 1080p resolution This field will be removed in a future version. Use the `resolution` field to directly to specify the resolution.                                                                                                                                                                                                                                  | `"quick"`                     |
| `name`            |    ✗     | Give your video a custom name for easy identification.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `"My Text To Video video"`    |
| `resolution`      |    ✗     | Controls the output video resolution. Defaults to `720p` if not specified. 480p and 720p are available on Creator, Pro, or Business tiers. However, 1080p require Pro or Business tier. **Options:** - `480p` - Supports only 5 or 10 second videos. Output: 24fps. Cost: 120 credits per 5 seconds. - `720p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 300 credits per 5 seconds. - `1080p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 600 credits per 5 seconds. | `"720p"`                      |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.text_to_video.create(
    end_seconds=5.0,
    orientation="landscape",
    style={"prompt": "a dog running"},
    name="My Text To Video video",
    resolution="720p",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.text_to_video.create(
    end_seconds=5.0,
    orientation="landscape",
    style={"prompt": "a dog running"},
    name="My Text To Video video",
    resolution="720p",
)
```

#### Response

##### Type

[V1TextToVideoCreateResponse](/magic_hour/types/models/v1_text_to_video_create_response.py)

##### Example

```python
{"credits_charged": 450, "estimated_frame_cost": 450, "id": "cuid-example"}
```
