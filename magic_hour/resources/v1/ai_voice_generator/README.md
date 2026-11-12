# v1.ai_voice_generator

## Module Functions

<!-- CUSTOM DOCS START -->

### Ai Voice Generator Generate Workflow <a name="generate"></a>

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
    style={
        "language": "spanish",
        "prompt": "Hello, how are you?",
        "speed": 1.15,
        "voice_name": "Elon Musk",
    },
    name="My Voice Generator audio",
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
res = await client.v1.ai_voice_generator.generate(
    style={
        "language": "spanish",
        "prompt": "Hello, how are you?",
        "speed": 1.15,
        "voice_name": "Elon Musk",
    },
    name="My Voice Generator audio",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="."
)
```

<!-- CUSTOM DOCS END -->

### AI Voice Generator <a name="create"></a>

Generate speech from text. Each character costs 0.1 credits. The cost is rounded up to the nearest whole number.

**API Endpoint**: `POST /v1/ai-voice-generator`

#### Parameters

| Parameter       | Required | Description                                                                                                               | Example                                                                                              |
| --------------- | :------: | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `style`         |    ✓     | The content used to generate speech.                                                                                      | `{"language": "spanish", "prompt": "Hello, how are you?", "speed": 1.15, "voice_name": "Elon Musk"}` |
| `└─ language`   |    ✗     | Spoken language. Use a canonical lowercase language name, or auto to detect the language from the text. Defaults to auto. | `"spanish"`                                                                                          |
| `└─ prompt`     |    ✓     | Text used to generate speech. The character limit is 5000 characters.                                                     | `"Hello, how are you?"`                                                                              |
| `└─ speed`      |    ✗     | Speech speed multiplier, from 0.75 to 1.30 inclusive. Defaults to 1 (normal speed).                                       | `1.15`                                                                                               |
| `└─ voice_name` |    ✓     | The voice to use for the speech. Use the `id` of a voice returned by `GET /v1/voices`.                                    | `"Elon Musk"`                                                                                        |
| `name`          |    ✗     | Give your audio a custom name for easy identification.                                                                    | `"My Voice Generator audio"`                                                                         |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_voice_generator.create(
    style={
        "language": "spanish",
        "prompt": "Hello, how are you?",
        "speed": 1.15,
        "voice_name": "Elon Musk",
    },
    name="My Voice Generator audio",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_voice_generator.create(
    style={
        "language": "spanish",
        "prompt": "Hello, how are you?",
        "speed": 1.15,
        "voice_name": "Elon Musk",
    },
    name="My Voice Generator audio",
)
```

#### Response

##### Type

[V1AiVoiceGeneratorCreateResponse](/magic_hour/types/models/v1_ai_voice_generator_create_response.py)

##### Example

```python
{"credits_charged": 1, "id": "cuid-example"}
```
