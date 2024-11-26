
### create <a name="create"></a>
Create AI Headshots

Create an AI headshot. Each headshot costs 50 frames.

**API Endpoint**: `POST /v1/ai-headshot-generator`

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_headshot_generator.create(
    data={
        "assets": {"image_file_path": "image/id/1234.png"},
        "name": "Ai Headshot image",
    }
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_headshot_generator.create(
    data={
        "assets": {"image_file_path": "image/id/1234.png"},
        "name": "Ai Headshot image",
    }
)
```

**Upgrade to see all examples**