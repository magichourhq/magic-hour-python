# v1.video_to_video

## Module Functions






<!-- CUSTOM DOCS START -->

### Video To Video Generate Workflow <a name="generate"></a>

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
res = client.v1.video_to_video.generate(
    assets={"video_file_path": "/path/to/1234.mp4", "video_source": "file"},
    end_seconds=15.0,
    start_seconds=0.0,
    style={
        "art_style": "3D Render",
        "model": "default",
        "prompt": "string",
        "prompt_type": "default",
        "version": "default",
    },
    fps_resolution="HALF",
    name="Video To Video video",
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
res = await client.v1.video_to_video.generate(
    assets={"video_file_path": "/path/to/1234.mp4", "video_source": "file"},
    end_seconds=15.0,
    start_seconds=0.0,
    style={
        "art_style": "3D Render",
        "model": "default",
        "prompt": "string",
        "prompt_type": "default",
        "version": "default",
    },
    fps_resolution="HALF",
    name="Video To Video video",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### Video-to-Video <a name="create"></a>

Create a Video To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.
  
Get more information about this mode at our [product page](https://magichour.ai/products/video-to-video).
  

**API Endpoint**: `POST /v1/video-to-video`

#### Parameters

| Parameter | Required | Deprecated | Description | Example |
|-----------|:--------:|:----------:|-------------|--------|
| `assets` | ✓ | ✗ | Provide the assets for video-to-video. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used | `{"video_file_path": "api-assets/id/1234.mp4", "video_source": "file"}` |
| `└─ video_file_path` | ✗ | — | Required if `video_source` is `file`. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.mp4"` |
| `└─ video_source` | ✓ | — |  | `"file"` |
| `└─ youtube_url` | ✗ | — | Using a youtube video as the input source. This field is required if `video_source` is `youtube` | `"http://www.example.com"` |
| `end_seconds` | ✓ | ✗ | The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds. | `15.0` |
| `start_seconds` | ✓ | ✗ | The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0. | `0.0` |
| `style` | ✓ | ✗ |  | `{"art_style": "3D Render", "model": "default", "prompt_type": "default", "version": "default"}` |
| `└─ art_style` | ✓ | — |  | `"3D Render"` |
| `└─ model` | ✗ | — | * `Dreamshaper` - a good all-around model that works for both animations as well as realism. * `Absolute Reality` - better at realism, but you'll often get similar results with Dreamshaper as well. * `Flat 2D Anime` - best for a flat illustration style that's common in most anime. * `default` - use the default recommended model for the selected art style. | `"default"` |
| `└─ prompt` | ✗ | — | The prompt used for the video. Prompt is required if `prompt_type` is `custom` or `append_default`. If `prompt_type` is `default`, then the `prompt` value passed will be ignored. | `"string"` |
| `└─ prompt_type` | ✗ | — | * `default` - Use the default recommended prompt for the art style. * `custom` - Only use the prompt passed in the API. Note: for v1, lora prompt will still be auto added to apply the art style properly. * `append_default` - Add the default recommended prompt to the end of the prompt passed in the API. | `"default"` |
| `└─ version` | ✗ | — | * `v1` - more detail, closer prompt adherence, and frame-by-frame previews. * `v2` - faster, more consistent, and less noisy. * `default` - use the default version for the selected art style. | `"default"` |
| `fps_resolution` | ✗ | ✗ | Determines whether the resulting video will have the same frame per second as the original video, or half. * `FULL` - the result video will have the same FPS as the input video * `HALF` - the result video will have half the FPS as the input video | `"HALF"` |
| `height` | ✗ | ✓ | `height` is deprecated and no longer influences the output video's resolution.  Output resolution is determined by the **minimum** of: - The resolution of the input video - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.  This field is retained only for backward compatibility and will be removed in a future release. | `123` |
| `name` | ✗ | ✗ | The name of video. This value is mainly used for your own identification of the video. | `"Video To Video video"` |
| `width` | ✗ | ✓ | `width` is deprecated and no longer influences the output video's resolution.  Output resolution is determined by the **minimum** of: - The resolution of the input video - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.  This field is retained only for backward compatibility and will be removed in a future release. | `123` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.video_to_video.create(
    assets={"video_file_path": "api-assets/id/1234.mp4", "video_source": "file"},
    end_seconds=15.0,
    start_seconds=0.0,
    style={
        "art_style": "3D Render",
        "model": "default",
        "prompt_type": "default",
        "version": "default",
    },
    fps_resolution="HALF",
    name="Video To Video video",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.video_to_video.create(
    assets={"video_file_path": "api-assets/id/1234.mp4", "video_source": "file"},
    end_seconds=15.0,
    start_seconds=0.0,
    style={
        "art_style": "3D Render",
        "model": "default",
        "prompt_type": "default",
        "version": "default",
    },
    fps_resolution="HALF",
    name="Video To Video video",
)

```

#### Response

##### Type
[V1VideoToVideoCreateResponse](/magic_hour/types/models/v1_video_to_video_create_response.py)

##### Example
`{"credits_charged": 450, "estimated_frame_cost": 450, "id": "cuid-example"}`

