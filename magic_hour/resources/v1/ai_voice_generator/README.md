# v1.ai_voice_generator

## Module Functions

### AI Voice Generator <a name="create"></a>

Generate speech from text. Each character costs 0.05 credits. The cost is rounded up to the nearest whole number.

**API Endpoint**: `POST /v1/ai-voice-generator`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `style` | ✓ | The content used to generate speech. | `{"prompt": "Hello, how are you?", "voice_name": "Elon Musk"}` |
| `└─ prompt` | ✓ | Text used to generate speech. Starter tier users can use up to 200 characters, while Creator, Pro, or Business users can use up to 1000. | `"Hello, how are you?"` |
| `└─ voice_name` | ✓ | The voice to use for the speech. Available voices: Elon Musk, Mark Zuckerberg, Joe Rogan, Barack Obama, Morgan Freeman, Kanye West, Donald Trump, Joe Biden, Kim Kardashian, Taylor Swift | `"Elon Musk"` |
| `name` | ✗ | The name of audio. This value is mainly used for your own identification of the audio. | `"Voice Generator audio"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_voice_generator.create(
    style={"prompt": "Hello, how are you?", "voice_name": "Elon Musk"},
    name="Voice Generator audio",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_voice_generator.create(
    style={"prompt": "Hello, how are you?", "voice_name": "Elon Musk"},
    name="Voice Generator audio",
)

```

#### Response

##### Type
[V1AiVoiceGeneratorCreateResponse](/magic_hour/types/models/v1_ai_voice_generator_create_response.py)

##### Example
`{"credits_charged": 1, "id": "cuid-example"}`


