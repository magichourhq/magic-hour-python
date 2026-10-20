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
    download_directory="."
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
    download_directory="."
)
```

<!-- CUSTOM DOCS END -->

### AI Talking Photo <a name="create"></a>

Create a talking photo video from an image and an audio file.

**API Endpoint**: `POST /v1/ai-talking-photo`

#### Parameters

| Parameter            | Required | Deprecated | Description                                                                                                                                                                                                                                                                                                                                                                                                    | Example                                                                                               |
| -------------------- | :------: | :--------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `assets`             |    ✓     |     ✗      | Provide the assets for creating a talking photo                                                                                                                                                                                                                                                                                                                                                                | `{"audio_file_path": "api-assets/id/1234.mp3", "image_file_path": "api-assets/id/1234.png"}`          |
| `└─ audio_file_path` |    ✓     |     —      | The audio file to sync with the image. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.                                           | `"api-assets/id/1234.mp3"`                                                                            |
| `└─ image_file_path` |    ✓     |     —      | The source image to animate. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.                                                     | `"api-assets/id/1234.png"`                                                                            |
| `end_seconds`        |    ✓     |     ✗      | The end time of the input audio in seconds. Maximum clip length depends on style.generation_mode: realistic 300s, prompted 45s.                                                                                                                                                                                                                                                                                | `5.0`                                                                                                 |
| `start_seconds`      |    ✓     |     ✗      | The start time of the input audio in seconds. Maximum clip length depends on style.generation_mode: realistic 300s, prompted 45s.                                                                                                                                                                                                                                                                              | `0.0`                                                                                                 |
| `max_resolution`     |    ✗     |     ✓      | Deprecated: use `resolution`. Still accepted as a larger-dimension cap, limited by your plan. Ignored when `resolution` is provided. After plan capping: * Below 1280 maps to `480p` (intermediate values round down). * 1280 or above maps to `720p`.                                                                                                                                                         | `123`                                                                                                 |
| `name`               |    ✗     |     ✗      | Give your video a custom name for easy identification.                                                                                                                                                                                                                                                                                                                                                         | `"My Talking Photo video"`                                                                            |
| `resolution`         |    ✗     |     ✗      | Output preset. Overrides `max_resolution`. Defaults to 480p in prompted mode; realistic mode uses the mapped plan maximum.                                                                                                                                                                                                                                                                                     | `"480p"`                                                                                              |
| `style`              |    ✗     |     ✗      | Attributes used to dictate the style of the output                                                                                                                                                                                                                                                                                                                                                             | `{"generation_mode": "realistic", "prompt": "A person smiling and speaking naturally to the camera"}` |
| `└─ generation_mode` |    ✗     |     —      | Controls overall motion style. * `realistic` - Maintains likeness well, high quality, and reliable. * `prompted` - Slightly lower likeness; allows option to prompt scene. **Deprecated values (maintained for backward compatibility):** * `pro` - Deprecated: use `realistic` * `standard` - Deprecated: use `prompted` * `stable` - Deprecated: use `realistic` * `expressive` - Deprecated: use `prompted` | `"realistic"`                                                                                         |
| `└─ intensity`       |    ✗     |     ✓      | Note: this value is only applicable when generation_mode is `expressive`. The value can include up to 2 decimal places. * Lower values yield more stability but can suppress mouth movement. * Higher values increase motion and expressiveness, with a higher risk of distortion.                                                                                                                             | `123.0`                                                                                               |
| `└─ prompt`          |    ✗     |     —      | A text prompt to guide the generation. Only applicable when generation_mode is `prompted`. This field is ignored for other modes.                                                                                                                                                                                                                                                                              | `"A person smiling and speaking naturally to the camera"`                                             |

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
    end_seconds=5.0,
    start_seconds=0.0,
    name="My Talking Photo video",
    resolution="480p",
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
    end_seconds=5.0,
    start_seconds=0.0,
    name="My Talking Photo video",
    resolution="480p",
)
```

#### Response

##### Type

[V1AiTalkingPhotoCreateResponse](/magic_hour/types/models/v1_ai_talking_photo_create_response.py)

##### Example

```python
{"credits_charged": 450, "estimated_frame_cost": 123, "id": "cuid-example"}
```
