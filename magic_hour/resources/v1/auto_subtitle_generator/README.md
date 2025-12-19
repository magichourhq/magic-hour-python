# v1.auto_subtitle_generator

## Module Functions






<!-- CUSTOM DOCS START -->

### Auto Subtitle Generator Generate Workflow <a name="generate"></a>

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
res = client.v1.auto_subtitle_generator.generate(
    assets={"video_file_path": "/path/to/1234.mp4"},
    end_seconds=15.0,
    start_seconds=0.0,
    style={},
    name="Auto Subtitle video",
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
res = await client.v1.auto_subtitle_generator.generate(
    assets={"video_file_path": "/path/to/1234.mp4"},
    end_seconds=15.0,
    start_seconds=0.0,
    style={},
    name="Auto Subtitle video",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### Auto Subtitle Generator <a name="create"></a>

Automatically generate subtitles for your video in multiple languages.

**API Endpoint**: `POST /v1/auto-subtitle-generator`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for auto subtitle generator | `{"video_file_path": "api-assets/id/1234.mp4"}` |
| `└─ video_file_path` | ✓ | This is the video used to add subtitles. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.mp4"` |
| `end_seconds` | ✓ | The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds. | `15.0` |
| `start_seconds` | ✓ | The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0. | `0.0` |
| `style` | ✓ | Style of the subtitle. At least one of `.style.template` or `.style.custom_config` must be provided.  * If only `.style.template` is provided, default values for the template will be used. * If both are provided, the fields in `.style.custom_config` will be used to overwrite the fields in `.style.template`. * If only `.style.custom_config` is provided, then all fields in `.style.custom_config` will be used.  To use custom config only, the following `custom_config` params are required: * `.style.custom_config.font` * `.style.custom_config.text_color` * `.style.custom_config.vertical_position` * `.style.custom_config.horizontal_position`  | `{}` |
| `└─ custom_config` | ✗ | Custom subtitle configuration. | `{"font": "Noto Sans", "font_size": 24.0, "font_style": "normal", "highlighted_text_color": "#FFD700", "horizontal_position": "center", "stroke_color": "#000000", "stroke_width": 1.0, "text_color": "#FFFFFF", "vertical_position": "bottom"}` |
| `└─ template` | ✗ | Preset subtitle templates. Please visit https://magichour.ai/create/auto-subtitle-generator to see the style of the existing templates. | `"cinematic"` |
| `name` | ✗ | The name of video. This value is mainly used for your own identification of the video. | `"Auto Subtitle video"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.auto_subtitle_generator.create(
    assets={"video_file_path": "api-assets/id/1234.mp4"},
    end_seconds=15.0,
    start_seconds=0.0,
    style={},
    name="Auto Subtitle video",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.auto_subtitle_generator.create(
    assets={"video_file_path": "api-assets/id/1234.mp4"},
    end_seconds=15.0,
    start_seconds=0.0,
    style={},
    name="Auto Subtitle video",
)

```

#### Response

##### Type
[V1AutoSubtitleGeneratorCreateResponse](/magic_hour/types/models/v1_auto_subtitle_generator_create_response.py)

##### Example
`{"credits_charged": 450, "estimated_frame_cost": 450, "id": "cuid-example"}`

