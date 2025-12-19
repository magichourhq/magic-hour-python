# v1.animation

## Module Functions






<!-- CUSTOM DOCS START -->

### Animation Generate Workflow <a name="generate"></a>

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
res = client.v1.animation.generate(
    assets={
        "audio_file_path": "/path/to/1234.mp3",
        "audio_source": "file",
        "image_file_path": "/path/to/1234.png",
    },
    end_seconds=15.0,
    fps=12.0,
    height=960,
    style={
        "art_style": "Painterly Illustration",
        "camera_effect": "Simple Zoom In",
        "prompt": "Cyberpunk city",
        "prompt_type": "custom",
        "transition_speed": 5,
    },
    width=512,
    name="Animation video",
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
res = await client.v1.animation.generate(
    assets={
        "audio_file_path": "/path/to/1234.mp3",
        "audio_source": "file",
        "image_file_path": "/path/to/1234.png",
    },
    end_seconds=15.0,
    fps=12.0,
    height=960,
    style={
        "art_style": "Painterly Illustration",
        "camera_effect": "Simple Zoom In",
        "prompt": "Cyberpunk city",
        "prompt_type": "custom",
        "transition_speed": 5,
    },
    width=512,
    name="Animation video",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### Animation <a name="create"></a>

Create a Animation video. The estimated frame cost is calculated based on the `fps` and `end_seconds` input.

**API Endpoint**: `POST /v1/animation`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for animation. | `{"audio_file_path": "api-assets/id/1234.mp3", "audio_source": "file", "image_file_path": "api-assets/id/1234.png"}` |
| `└─ audio_file_path` | ✗ | The path of the input audio. This field is required if `audio_source` is `file`. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.mp3"` |
| `└─ audio_source` | ✓ | Optionally add an audio source if you'd like to incorporate audio into your video | `"file"` |
| `└─ image_file_path` | ✗ | An initial image to use a the first frame of the video. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.png"` |
| `└─ youtube_url` | ✗ | Using a youtube video as the input source. This field is required if `audio_source` is `youtube` | `"http://www.example.com"` |
| `end_seconds` | ✓ | This value determines the duration of the output video. | `15.0` |
| `fps` | ✓ | The desire output video frame rate | `12.0` |
| `height` | ✓ | The height of the final output video. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details | `960` |
| `style` | ✓ | Defines the style of the output video | `{"art_style": "Painterly Illustration", "camera_effect": "Simple Zoom In", "prompt": "Cyberpunk city", "prompt_type": "custom", "transition_speed": 5}` |
| `└─ art_style` | ✓ | The art style used to create the output video | `"Painterly Illustration"` |
| `└─ art_style_custom` | ✗ | Describe custom art style. This field is required if `art_style` is `Custom` | `"string"` |
| `└─ camera_effect` | ✓ | The camera effect used to create the output video | `"Simple Zoom In"` |
| `└─ prompt` | ✗ | The prompt used for the video. Prompt is required if `prompt_type` is `custom`. Otherwise this value is ignored | `"Cyberpunk city"` |
| `└─ prompt_type` | ✓ |  * `custom` - Use your own prompt for the video. * `use_lyrics` - Use the lyrics of the audio to create the prompt. If this option is selected, then `assets.audio_source` must be `file` or `youtube`. * `ai_choose` - Let AI write the prompt. If this option is selected, then `assets.audio_source` must be `file` or `youtube`. | `"custom"` |
| `└─ transition_speed` | ✓ | Change determines how quickly the video's content changes across frames.  * Higher = more rapid transitions. * Lower = more stable visual experience. | `5` |
| `width` | ✓ | The width of the final output video. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details | `512` |
| `name` | ✗ | The name of video. This value is mainly used for your own identification of the video. | `"Animation video"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.animation.create(
    assets={
        "audio_file_path": "api-assets/id/1234.mp3",
        "audio_source": "file",
        "image_file_path": "api-assets/id/1234.png",
    },
    end_seconds=15.0,
    fps=12.0,
    height=960,
    style={
        "art_style": "Painterly Illustration",
        "camera_effect": "Simple Zoom In",
        "prompt": "Cyberpunk city",
        "prompt_type": "custom",
        "transition_speed": 5,
    },
    width=512,
    name="Animation video",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.animation.create(
    assets={
        "audio_file_path": "api-assets/id/1234.mp3",
        "audio_source": "file",
        "image_file_path": "api-assets/id/1234.png",
    },
    end_seconds=15.0,
    fps=12.0,
    height=960,
    style={
        "art_style": "Painterly Illustration",
        "camera_effect": "Simple Zoom In",
        "prompt": "Cyberpunk city",
        "prompt_type": "custom",
        "transition_speed": 5,
    },
    width=512,
    name="Animation video",
)

```

#### Response

##### Type
[V1AnimationCreateResponse](/magic_hour/types/models/v1_animation_create_response.py)

##### Example
`{"credits_charged": 450, "estimated_frame_cost": 450, "id": "cuid-example"}`

