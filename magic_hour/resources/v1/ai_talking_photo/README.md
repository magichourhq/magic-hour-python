# v1.ai_talking_photo

## Module Functions






<!-- CUSTOM DOCS START -->

### Ai Talking Photo Generate Workflow <a name="generate"></a>

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
res = client.v1.ai_talking_photo.generate(
    assets={
        "audio_file_path": "/path/to/1234.mp3",
        "image_file_path": "/path/to/1234.png",
    },
    end_seconds=15.0,
    start_seconds=0.0,
    name="Talking Photo image",
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
res = await client.v1.ai_talking_photo.generate(
    assets={
        "audio_file_path": "/path/to/1234.mp3",
        "image_file_path": "/path/to/1234.png",
    },
    end_seconds=15.0,
    start_seconds=0.0,
    name="Talking Photo image",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### AI Talking Photo <a name="create"></a>

Create a talking photo from an image and audio or text input.

**API Endpoint**: `POST /v1/ai-talking-photo`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for creating a talking photo | `{"audio_file_path": "api-assets/id/1234.mp3", "image_file_path": "api-assets/id/1234.png"}` |
| `└─ audio_file_path` | ✓ | The audio file to sync with the image. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.mp3"` |
| `└─ image_file_path` | ✓ | The source image to animate. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.png"` |
| `end_seconds` | ✓ | The end time of the input audio in seconds. The maximum duration allowed is 60 seconds. | `15.0` |
| `start_seconds` | ✓ | The start time of the input audio in seconds. The maximum duration allowed is 60 seconds. | `0.0` |
| `name` | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Talking Photo image"` |
| `style` | ✗ | Attributes used to dictate the style of the output | `{"generation_mode": "pro", "intensity": 1.5}` |
| `└─ generation_mode` | ✗ | Controls overall motion style. * `pro` -  Higher fidelity, realistic detail, accurate lip sync, and faster generation. * `standard` -  More expressive motion, but lower visual fidelity.  * `expressive` - More motion and facial expressiveness; may introduce visual artifacts. (Deprecated: passing this value will be treated as `standard`) * `stable` -  Reduced motion for cleaner output; may result in minimal animation. (Deprecated: passing this value will be treated as `pro`) | `"pro"` |
| `└─ intensity` | ✗ | Note: this value is only applicable when generation_mode is `expressive`. The value can include up to 2 decimal places. * Lower values yield more stability but can suppress mouth movement. * Higher values increase motion and expressiveness, with a higher risk of distortion. | `1.5` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_talking_photo.create(
    assets={
        "audio_file_path": "api-assets/id/1234.mp3",
        "image_file_path": "api-assets/id/1234.png",
    },
    end_seconds=15.0,
    start_seconds=0.0,
    name="Talking Photo image",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_talking_photo.create(
    assets={
        "audio_file_path": "api-assets/id/1234.mp3",
        "image_file_path": "api-assets/id/1234.png",
    },
    end_seconds=15.0,
    start_seconds=0.0,
    name="Talking Photo image",
)

```

#### Response

##### Type
[V1AiTalkingPhotoCreateResponse](/magic_hour/types/models/v1_ai_talking_photo_create_response.py)

##### Example
`{"credits_charged": 450, "estimated_frame_cost": 450, "id": "cuid-example"}`

