# v1.ai_voice_cloner

## Module Functions

### AI Voice Cloner <a name="create"></a>

Clone a voice from an audio sample and generate speech.

- Each character costs 0.05 credits.
- The cost is rounded up to the nearest whole number

**API Endpoint**: `POST /v1/ai-voice-cloner`

#### Parameters

| Parameter            | Required | Description                                                                                                                                                                                                                                                                                                                                                                           | Example                                         |
| -------------------- | :------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| `assets`             |    ✓     | Provide the assets for voice cloning.                                                                                                                                                                                                                                                                                                                                                 | `{"audio_file_path": "api-assets/id/1234.mp3"}` |
| `└─ audio_file_path` |    ✓     | The audio used to clone the voice. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more. | `"api-assets/id/1234.mp3"`                      |
| `style`              |    ✓     |                                                                                                                                                                                                                                                                                                                                                                                       | `{"prompt": "Hello, this is my cloned voice."}` |
| `└─ prompt`          |    ✓     | Text used to generate speech from the cloned voice. The character limit is 1000 characters.                                                                                                                                                                                                                                                                                           | `"Hello, this is my cloned voice."`             |
| `name`               |    ✗     | The name of audio. This value is mainly used for your own identification of the audio.                                                                                                                                                                                                                                                                                                | `"Voice Cloner audio"`                          |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_voice_cloner.create(
    assets={"audio_file_path": "api-assets/id/1234.mp3"},
    style={"prompt": "Hello, this is my cloned voice."},
    name="Voice Cloner audio",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_voice_cloner.create(
    assets={"audio_file_path": "api-assets/id/1234.mp3"},
    style={"prompt": "Hello, this is my cloned voice."},
    name="Voice Cloner audio",
)
```

#### Response

##### Type

[V1AiVoiceClonerCreateResponse](/magic_hour/types/models/v1_ai_voice_cloner_create_response.py)

##### Example

```python
{"credits_charged": 1, "id": "cuid-example"}
```
