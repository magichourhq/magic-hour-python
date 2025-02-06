
### create <a name="create"></a>
Image Background Remover

Remove background from image. Each image costs 5 frames.

**API Endpoint**: `POST /v1/image-background-remover`

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.image_background_remover.create(
    assets={"image_file_path": "api-assets/id/1234.png"},
    name="Background Remover image",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.image_background_remover.create(
    assets={"image_file_path": "api-assets/id/1234.png"},
    name="Background Remover image",
)
```
