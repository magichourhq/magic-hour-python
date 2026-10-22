# v1.ai_music_generator

## generate

Creates the project, waits for completion, and downloads outputs by default.

```python
result = client.v1.ai_music_generator.generate(
    duration=120,
    style={"prompt": "Dreamy synthwave with warm bass"},
)
```

Set `wait_for_completion=False` to return the current project status, or `download_outputs=False` to skip downloads. Use `download_directory` to choose the output folder. `AsyncClient` supports the same method with `await`.

## Module Functions

### AI Music Generator <a name="create"></a>

Generate music from a description, with optional custom lyrics or instrumental-only output. Costs 1 credits per requested second. Returns a project ID; poll GET /v1/audio-projects/{id} for status and downloads.

**API Endpoint**: `POST /v1/ai-music-generator`

#### Parameters

| Parameter               | Required | Description                                                                            | Example                                                                                                                       |
| ----------------------- | :------: | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `duration`              |    ✓     | Requested track duration in seconds, from 15 to 300. Determines credits charged.       | `120`                                                                                                                         |
| `style`                 |    ✓     |                                                                                        | `{"instrumental": False, "lyrics": "City lights are fading...", "prompt": "Dreamy synthwave with warm bass and soft vocals"}` |
| `└─ instrumental`       |    ✗     | Generate music without vocals. When true, lyrics is ignored.                           | `False`                                                                                                                       |
| `└─ lyrics`             |    ✗     | Custom lyrics. Omit or leave blank for AI-generated lyrics when instrumental is false. | `"City lights are fading..."`                                                                                                 |
| `└─ prompt`             |    ✓     | Describe the song, including genre, mood, and instruments.                             | `"Dreamy synthwave with warm bass and soft vocals"`                                                                           |
| `additional_properties` |    ✗     |                                                                                        | `{}`                                                                                                                          |
| `name`                  |    ✗     | Give your audio a custom name for easy identification.                                 | `"My Music Generator audio"`                                                                                                  |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_music_generator.create(
    duration=120,
    style={
        "instrumental": False,
        "lyrics": "City lights are fading...",
        "prompt": "Dreamy synthwave with warm bass and soft vocals",
    },
    name="My Music Generator audio",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_music_generator.create(
    duration=120,
    style={
        "instrumental": False,
        "lyrics": "City lights are fading...",
        "prompt": "Dreamy synthwave with warm bass and soft vocals",
    },
    name="My Music Generator audio",
)
```

#### Response

##### Type

[V1AiMusicGeneratorCreateResponse](/magic_hour/types/models/v1_ai_music_generator_create_response.py)

##### Example

```python
{"credits_charged": 120, "id": "cuid-example"}
```
