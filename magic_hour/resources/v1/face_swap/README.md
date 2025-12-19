# v1.face_swap

## Module Functions






<!-- CUSTOM DOCS START -->

### Face Swap Generate Workflow <a name="generate"></a>

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
res = client.v1.face_swap.generate(
    assets={
        "face_mappings": [
            {
                "new_face": "/path/to/1234.png",
                "original_face": "api-assets/id/0-0.png",
            }
        ],
        "face_swap_mode": "all-faces",
        "image_file_path": "image/id/1234.png",
        "video_file_path": "/path/to/1234.mp4",
        "video_source": "file",
    },
    end_seconds=15.0,
    start_seconds=0.0,
    name="Face Swap video",
    style={"version": "default"},
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
res = await client.v1.face_swap.generate(
    assets={
        "face_mappings": [
            {
                "new_face": "/path/to/1234.png",
                "original_face": "api-assets/id/0-0.png",
            }
        ],
        "face_swap_mode": "all-faces",
        "image_file_path": "image/id/1234.png",
        "video_file_path": "/path/to/1234.mp4",
        "video_source": "file",
    },
    end_seconds=15.0,
    start_seconds=0.0,
    name="Face Swap video",
    style={"version": "default"},
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### Face Swap Video <a name="create"></a>

Create a Face Swap video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.
  
Get more information about this mode at our [product page](https://magichour.ai/products/face-swap).
  

**API Endpoint**: `POST /v1/face-swap`

#### Parameters

| Parameter | Required | Deprecated | Description | Example |
|-----------|:--------:|:----------:|-------------|--------|
| `assets` | ✓ | ✗ | Provide the assets for face swap. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used | `{"face_mappings": [{"new_face": "api-assets/id/1234.png", "original_face": "api-assets/id/0-0.png"}], "face_swap_mode": "all-faces", "image_file_path": "image/id/1234.png", "video_file_path": "api-assets/id/1234.mp4", "video_source": "file"}` |
| `└─ face_mappings` | ✗ | — | This is the array of face mappings used for multiple face swap. The value is required if `face_swap_mode` is `individual-faces`. | `[{"new_face": "api-assets/id/1234.png", "original_face": "api-assets/id/0-0.png"}]` |
| `└─ face_swap_mode` | ✗ | — | The mode of face swap. * `all-faces` - Swap all faces in the target image or video. `source_file_path` is required. * `individual-faces` - Swap individual faces in the target image or video. `source_faces` is required. | `"all-faces"` |
| `└─ image_file_path` | ✗ | — | The path of the input image with the face to be swapped.  The value is required if `face_swap_mode` is `all-faces`.  This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"image/id/1234.png"` |
| `└─ video_file_path` | ✗ | — | Required if `video_source` is `file`. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.mp4"` |
| `└─ video_source` | ✓ | — |  | `"file"` |
| `└─ youtube_url` | ✗ | — | Using a youtube video as the input source. This field is required if `video_source` is `youtube` | `"http://www.example.com"` |
| `end_seconds` | ✓ | ✗ | The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds. | `15.0` |
| `start_seconds` | ✓ | ✗ | The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0. | `0.0` |
| `height` | ✗ | ✓ | `height` is deprecated and no longer influences the output video's resolution.  Output resolution is determined by the **minimum** of: - The resolution of the input video - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.  This field is retained only for backward compatibility and will be removed in a future release. | `123` |
| `name` | ✗ | ✗ | The name of video. This value is mainly used for your own identification of the video. | `"Face Swap video"` |
| `style` | ✗ | ✗ | Style of the face swap video. | `{"version": "default"}` |
| `└─ version` | ✗ | — | * `v1` - May preserve skin detail and texture better, but weaker identity preservation. * `v2` - Faster, sharper, better handling of hair and glasses. stronger identity preservation. * `default` - Use the version we recommend, which will change over time. This is recommended unless you need a specific earlier version. This is the default behavior. | `"default"` |
| `width` | ✗ | ✓ | `width` is deprecated and no longer influences the output video's resolution.  Output resolution is determined by the **minimum** of: - The resolution of the input video - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.  This field is retained only for backward compatibility and will be removed in a future release. | `123` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.face_swap.create(
    assets={
        "face_mappings": [
            {
                "new_face": "api-assets/id/1234.png",
                "original_face": "api-assets/id/0-0.png",
            }
        ],
        "face_swap_mode": "all-faces",
        "image_file_path": "image/id/1234.png",
        "video_file_path": "api-assets/id/1234.mp4",
        "video_source": "file",
    },
    end_seconds=15.0,
    start_seconds=0.0,
    name="Face Swap video",
    style={"version": "default"},
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.face_swap.create(
    assets={
        "face_mappings": [
            {
                "new_face": "api-assets/id/1234.png",
                "original_face": "api-assets/id/0-0.png",
            }
        ],
        "face_swap_mode": "all-faces",
        "image_file_path": "image/id/1234.png",
        "video_file_path": "api-assets/id/1234.mp4",
        "video_source": "file",
    },
    end_seconds=15.0,
    start_seconds=0.0,
    name="Face Swap video",
    style={"version": "default"},
)

```

#### Response

##### Type
[V1FaceSwapCreateResponse](/magic_hour/types/models/v1_face_swap_create_response.py)

##### Example
`{"credits_charged": 450, "estimated_frame_cost": 450, "id": "cuid-example"}`

