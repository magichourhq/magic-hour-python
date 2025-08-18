### File Uploading

The client provides a easy way to upload media files to Magic Hour's cloud storage. Once uploaded, files receive a unique path that can be referenced across other Magic Hour API endpoints.

#### Synchronous Client

Upload using File Path, Path Object, or File-like Object

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("MAGIC_HOUR_API_TOKEN"))

# Using file path
uploaded_path = client.v1.files.upload_file("/path/to/image.jpg")

# Upload path object
file_path = Path("./assets/photo.png")
uploaded_path = client.v1.files.upload_file(file_path)

with open("/path/to/image.jpg", "rb") as file:
    uploaded_path = client.v1.files.upload_file(image_file)
```

#### Asynchronous Client

Upload using File Path, Path Object, or File-like Object

```python
import asyncio
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("MAGIC_HOUR_API_TOKEN"))

# Using file path
uploaded_path = await client.v1.files.upload_file("/path/to/image.jpg")

# Upload path object
file_path = Path("./assets/photo.png")
uploaded_path = await client.v1.files.upload_file(file_path)

with open("/path/to/image.jpg", "rb") as file:
    uploaded_path = await client.v1.files.upload_file(file)
```
