# v1_ai_qr_code_generator

## Module Functions

<!-- CUSTOM DOCS START -->

<!-- CUSTOM DOCS END -->

### AI QR Code <a name="create"></a>

Create an AI QR code. Each QR code costs 20 credits.

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
`{"credits_charged": 20, "frame_cost": 20, "id": "cuid-example"}`

