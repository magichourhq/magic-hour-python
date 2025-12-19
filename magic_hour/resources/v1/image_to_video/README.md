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
    download_directory="outputs"
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
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### Image-to-Video <a name="create"></a>

Create a Image To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.
  
Get more information about this mode at our [product page](https://magichour.ai/products/image-to-video).
  

**API Endpoint**: `POST /v1/image-to-video`

#### Parameters

| Parameter | Required | Deprecated | Description | Example |
|-----------|:--------:|:----------:|-------------|--------|
| `assets` | ✓ | ✗ | Provide the assets for image-to-video. | `{"image_file_path": "api-assets/id/1234.png"}` |
| `└─ image_file_path` | ✓ | — | The path of the image file. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.png"` |
| `end_seconds` | ✓ | ✗ | The total duration of the output video in seconds. | `5.0` |
| `height` | ✗ | ✓ | `height` is deprecated and no longer influences the output video's resolution.  Output resolution is determined by the **minimum** of: - The resolution of the input video - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.  This field is retained only for backward compatibility and will be removed in a future release. | `123` |
| `name` | ✗ | ✗ | The name of video. This value is mainly used for your own identification of the video. | `"Image To Video video"` |
| `resolution` | ✗ | ✗ | Controls the output video resolution. Defaults to `720p` if not specified.  480p and 720p are available on Creator, Pro, or Business tiers. However, 1080p require Pro or Business tier.  **Options:** - `480p` - Supports only 5 or 10 second videos. Output: 24fps. Cost: 120 credits per 5 seconds. - `720p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 300 credits per 5 seconds. - `1080p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 600 credits per 5 seconds. | `"720p"` |
| `style` | ✗ | ✗ | Attributed used to dictate the style of the output | `{"prompt": "a dog running"}` |
| `└─ high_quality` | ✗ | ✓ | Deprecated: Please use `resolution` instead. For backward compatibility,  * `false` maps to 720p resolution * `true` maps to 1080p resolution  This field will be removed in a future version. Use the `resolution` field to directly specify the resolution. | `True` |
| `└─ prompt` | ✗ | — | The prompt used for the video. | `"a dog running"` |
| `└─ quality_mode` | ✗ | ✓ | DEPRECATED: Please use `resolution` field instead. For backward compatibility: * `quick` maps to 720p resolution * `studio` maps to 1080p resolution  This field will be removed in a future version. Use the `resolution` field to directly to specify the resolution. | `"quick"` |
| `width` | ✗ | ✓ | `width` is deprecated and no longer influences the output video's resolution.  Output resolution is determined by the **minimum** of: - The resolution of the input video - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.  This field is retained only for backward compatibility and will be removed in a future release. | `123` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.image_to_video.create(
    assets={"image_file_path": "api-assets/id/1234.png"},
    end_seconds=5.0,
    name="Image To Video video",
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
    name="Image To Video video",
    resolution="720p",
)

```

#### Response

##### Type
[V1ImageToVideoCreateResponse](/magic_hour/types/models/v1_image_to_video_create_response.py)

##### Example
`{"credits_charged": 450, "estimated_frame_cost": 450, "id": "cuid-example"}`

