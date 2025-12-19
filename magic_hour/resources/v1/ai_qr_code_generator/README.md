# v1.ai_qr_code_generator

## Module Functions






<!-- CUSTOM DOCS START -->

### Ai Qr Code Generator Generate Workflow <a name="generate"></a>

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
res = client.v1.ai_qr_code_generator.generate(
    content="https://magichour.ai",
    style={"art_style": "Watercolor"},
    name="Qr Code image",
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
res = await client.v1.ai_qr_code_generator.generate(
    content="https://magichour.ai",
    style={"art_style": "Watercolor"},
    name="Qr Code image",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### AI QR Code Generator <a name="create"></a>

Create an AI QR code. Each QR code costs 0 credits.

**API Endpoint**: `POST /v1/ai-qr-code-generator`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `content` | ✓ | The content of the QR code. | `"https://magichour.ai"` |
| `style` | ✓ |  | `{"art_style": "Watercolor"}` |
| `└─ art_style` | ✓ | To use our templates, pass in one of Watercolor, Cyberpunk City, Ink Landscape, Interior Painting, Japanese Street, Mech, Minecraft, Picasso Painting, Game Map, Spaceship, Chinese Painting, Winter Village, or pass any custom art style. | `"Watercolor"` |
| `name` | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Qr Code image"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_qr_code_generator.create(
    content="https://magichour.ai",
    style={"art_style": "Watercolor"},
    name="Qr Code image",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_qr_code_generator.create(
    content="https://magichour.ai",
    style={"art_style": "Watercolor"},
    name="Qr Code image",
)

```

#### Response

##### Type
[V1AiQrCodeGeneratorCreateResponse](/magic_hour/types/models/v1_ai_qr_code_generator_create_response.py)

##### Example
`{"credits_charged": 0, "frame_cost": 0, "id": "cuid-example"}`

