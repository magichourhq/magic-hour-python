# v1.ai_voice_generator

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
res = client.v1.ai_voice_generator.generate(
    style={"prompt": "Hello, how are you?", "voice_name": "Elon Musk"},
    name="Voice Generator audio",
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
res = await client.v1.ai_voice_generator.generate(
    style={"prompt": "Hello, how are you?", "voice_name": "Elon Musk"},
    name="Voice Generator audio",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->

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


