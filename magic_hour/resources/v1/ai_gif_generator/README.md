# v1.ai_gif_generator

## Module Functions






<!-- CUSTOM DOCS START -->

### Ai Gif Generator Generate Workflow <a name="generate"></a>

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
res = client.v1.ai_gif_generator.generate(
    style={"prompt": "Cute dancing cat, pixel art"},
    name="Ai Gif gif",
    output_format="gif",
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
res = await client.v1.ai_gif_generator.generate(
    style={"prompt": "Cute dancing cat, pixel art"},
    name="Ai Gif gif",
    output_format="gif",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### AI GIF Generator <a name="create"></a>

Create an AI GIF. Each GIF costs 50 credits.

**API Endpoint**: `POST /v1/ai-gif-generator`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `style` | ✓ |  | `{"prompt": "Cute dancing cat, pixel art"}` |
| `└─ prompt` | ✓ | The prompt used for the GIF. | `"Cute dancing cat, pixel art"` |
| `name` | ✗ | The name of gif. This value is mainly used for your own identification of the gif. | `"Ai Gif gif"` |
| `output_format` | ✗ | The output file format for the generated animation. | `"gif"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_gif_generator.create(
    style={"prompt": "Cute dancing cat, pixel art"},
    name="Ai Gif gif",
    output_format="gif",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_gif_generator.create(
    style={"prompt": "Cute dancing cat, pixel art"},
    name="Ai Gif gif",
    output_format="gif",
)

```

#### Response

##### Type
[V1AiGifGeneratorCreateResponse](/magic_hour/types/models/v1_ai_gif_generator_create_response.py)

##### Example
`{"credits_charged": 50, "frame_cost": 50, "id": "cuid-example"}`

