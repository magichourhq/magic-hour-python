
### Auto Subtitle Generator <a name="create"></a>

Automatically generate subtitles for your video in multiple languages.

**API Endpoint**: `POST /v1/auto-subtitle-generator`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for auto subtitle generator | `{"video_file_path": "api-assets/id/1234.mp4"}` |
| `end_seconds` | ✓ | The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds. | `15.0` |
| `start_seconds` | ✓ | The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0. | `0.0` |
| `style` | ✓ | Style of the subtitle. At least one of `.style.template` or `.style.custom_config` must be provided.  * If only `.style.template` is provided, default values for the template will be used. * If both are provided, the fields in `.style.custom_config` will be used to overwrite the fields in `.style.template`. * If only `.style.custom_config` is provided, then all fields in `.style.custom_config` will be used.  To use custom config only, the following `custom_config` params are required: * `.style.custom_config.font` * `.style.custom_config.text_color` * `.style.custom_config.vertical_position` * `.style.custom_config.horizontal_position`  | `{}` |
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
