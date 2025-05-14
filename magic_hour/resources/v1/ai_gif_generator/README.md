
### AI GIFs <a name="create"></a>

Create an AI GIF. Each GIF costs 25 credits.

**API Endpoint**: `POST /v1/ai-gif-generator`

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_gif_generator.create(
    style={"prompt": "Cute dancing cat, pixel art"}, name="Ai Gif gif"
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_gif_generator.create(
    style={"prompt": "Cute dancing cat, pixel art"}, name="Ai Gif gif"
)
```
