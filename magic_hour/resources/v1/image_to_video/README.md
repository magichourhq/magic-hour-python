# v1.image_to_video

## Module Functions

<!-- CUSTOM DOCS START -->

### Image To Video Generate Workflow <a name="generate"></a>

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
res = client.v1.image_to_video.generate(
    assets={"image_file_path": "/path/to/1234.png"},
    end_seconds=5.0,
    name="Image To Video video",
    resolution="720p",
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
res = await client.v1.image_to_video.generate(
    assets={"image_file_path": "/path/to/1234.png"},
    end_seconds=5.0,
    name="Image To Video video",
    resolution="720p",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="."
)
```

<!-- CUSTOM DOCS END -->

### Image-to-Video <a name="create"></a>

**What this API does**

Create the same Image To Video you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

**Good for**

- Automation and batch processing
- Adding image to video into apps, pipelines, or tools

**How it works (3 steps)**

1. Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
2. Send a request to create a image to video job with the basic fields.
3. Check the job status until it's `complete`, then download the result from `downloads`.

**Key options**

- Inputs: usually a file, sometimes a YouTube link, depending on project type
- Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
- Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

**Cost**\
Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

For detailed examples, see the [product page](https://magichour.ai/products/image-to-video).

**API Endpoint**: `POST /v1/image-to-video`

#### Parameters

| Parameter            | Required | Deprecated | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Example                                         |
| -------------------- | :------: | :--------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| `assets`             |    ✓     |     ✗      | Provide the assets for image-to-video. Sora 2 only supports images with an aspect ratio of `9:16` or `16:9`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `{"image_file_path": "api-assets/id/1234.png"}` |
| `└─ image_file_path` |    ✓     |     —      | The path of the image file. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.                                                                                                                                                                                                                                              | `"api-assets/id/1234.png"`                      |
| `end_seconds`        |    ✓     |     ✗      | The total duration of the output video in seconds. Supported durations depend on the chosen model: _ **Default**: 5-60 seconds (either 5 or 10 for 480p). _ **Seedance**: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 _ **Kling 2.5 Audio**: 5, 10 _ **Sora 2**: 4, 8, 12, 24, 36, 48, 60 _ **Veo 3.1 Audio**: 4, 6, 8, 16, 24, 32, 40, 48, 56 _ **Veo 3.1**: 4, 6, 8, 16, 24, 32, 40, 48, 56 \* **Kling 1.6**: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60                                                                                                                                                   | `5.0`                                           |
| `height`             |    ✗     |     ✓      | `height` is deprecated and no longer influences the output video's resolution. Output resolution is determined by the **minimum** of: - The resolution of the input video - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details. This field is retained only for backward compatibility and will be removed in a future release.                                                                                                                                                                                           | `123`                                           |
| `model`              |    ✗     |     ✗      | The AI model to use for video generation. _ `default`: Our recommended model for general use (Kling 2.5 Audio). Note: For backward compatibility, if you use default and end_seconds > 10, we'll fall back to Kling 1.6. _ `seedance`: Great for fast iteration and start/end frame _ `kling-2.5-audio`: Great for motion, action, and camera control _ `sora-2`: Great for story-telling, dialogue & creativity _ `veo3.1-audio`: Great for dialogue + SFX generated natively _ `veo3.1`: Great for realism, polish, & prompt adherence \* `kling-1.6`: Great for dependable clips with smooth motion | `"kling-2.5-audio"`                             |
| `name`               |    ✗     |     ✗      | Give your video a custom name for easy identification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `"My Image To Video video"`                     |
| `resolution`         |    ✗     |     ✗      | Controls the output video resolution. Defaults to `720p` if not specified. _ **Default**: Supports `480p`, `720p`, and `1080p`. _ **Seedance**: Supports `480p`, `720p`, `1080p`. _ **Kling 2.5 Audio**: Supports `720p`, `1080p`. _ **Sora 2**: Supports `720p`. _ **Veo 3.1 Audio**: Supports `720p`, `1080p`. _ **Veo 3.1**: Supports `720p`, `1080p`. \* **Kling 1.6**: Supports `720p`, `1080p`.                                                                                                                                                                                                  | `"720p"`                                        |
| `style`              |    ✗     |     ✗      | Attributed used to dictate the style of the output                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `{"prompt": "a dog running"}`                   |
| `└─ high_quality`    |    ✗     |     ✓      | Deprecated: Please use `resolution` instead. For backward compatibility, _ `false` maps to 720p resolution _ `true` maps to 1080p resolution This field will be removed in a future version. Use the `resolution` field to directly specify the resolution.                                                                                                                                                                                                                                                                                                                                            | `True`                                          |
| `└─ prompt`          |    ✗     |     —      | The prompt used for the video.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `"a dog running"`                               |
| `└─ quality_mode`    |    ✗     |     ✓      | DEPRECATED: Please use `resolution` field instead. For backward compatibility: _ `quick` maps to 720p resolution _ `studio` maps to 1080p resolution This field will be removed in a future version. Use the `resolution` field to directly to specify the resolution.                                                                                                                                                                                                                                                                                                                                 | `"quick"`                                       |
| `width`              |    ✗     |     ✓      | `width` is deprecated and no longer influences the output video's resolution. Output resolution is determined by the **minimum** of: - The resolution of the input video - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details. This field is retained only for backward compatibility and will be removed in a future release.                                                                                                                                                                                            | `123`                                           |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.image_to_video.create(
    assets={"image_file_path": "api-assets/id/1234.png"},
    end_seconds=5.0,
    model="kling-2.5-audio",
    name="My Image To Video video",
    resolution="720p",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.image_to_video.create(
    assets={"image_file_path": "api-assets/id/1234.png"},
    end_seconds=5.0,
    model="kling-2.5-audio",
    name="My Image To Video video",
    resolution="720p",
)
```

#### Response

##### Type

[V1ImageToVideoCreateResponse](/magic_hour/types/models/v1_image_to_video_create_response.py)

##### Example

```python
{"credits_charged": 450, "estimated_frame_cost": 450, "id": "cuid-example"}
```
