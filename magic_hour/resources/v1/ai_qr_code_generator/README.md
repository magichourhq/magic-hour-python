
### create <a name="create"></a>
AI QR Code

Create an AI QR code. Each QR code costs 20 frames.

**API Endpoint**: `POST /v1/ai-qr-code-generator`

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
