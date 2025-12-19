# v1.ai_meme_generator

## Module Functions






<!-- CUSTOM DOCS START -->

### Ai Meme Generator Generate Workflow <a name="generate"></a>

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
res = client.v1.ai_meme_generator.generate(
    style={
        "search_web": False,
        "template": "Drake Hotline Bling",
        "topic": "When the code finally works",
    },
    name="My Funny Meme",
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
res = await client.v1.ai_meme_generator.generate(
    style={
        "search_web": False,
        "template": "Drake Hotline Bling",
        "topic": "When the code finally works",
    },
    name="My Funny Meme",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### AI Meme Generator <a name="create"></a>

Create an AI generated meme. Each meme costs 10 credits.

**API Endpoint**: `POST /v1/ai-meme-generator`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `style` | ✓ |  | `{"search_web": False, "template": "Drake Hotline Bling", "topic": "When the code finally works"}` |
| `└─ search_web` | ✗ | Whether to search the web for meme content. | `False` |
| `└─ template` | ✓ | To use our templates, pass in one of the enum values. | `"Drake Hotline Bling"` |
| `└─ topic` | ✓ | The topic of the meme. | `"When the code finally works"` |
| `name` | ✗ | The name of the meme. | `"My Funny Meme"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_meme_generator.create(
    style={
        "search_web": False,
        "template": "Drake Hotline Bling",
        "topic": "When the code finally works",
    },
    name="My Funny Meme",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_meme_generator.create(
    style={
        "search_web": False,
        "template": "Drake Hotline Bling",
        "topic": "When the code finally works",
    },
    name="My Funny Meme",
)

```

#### Response

##### Type
[V1AiMemeGeneratorCreateResponse](/magic_hour/types/models/v1_ai_meme_generator_create_response.py)

##### Example
`{"credits_charged": 10, "frame_cost": 10, "id": "cuid-example"}`

