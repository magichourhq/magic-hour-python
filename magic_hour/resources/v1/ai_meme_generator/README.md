
### AI Meme Generator <a name="create"></a>

Create an AI generated meme. Each meme costs 10 credits.

**API Endpoint**: `POST /v1/ai-meme-generator`

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
