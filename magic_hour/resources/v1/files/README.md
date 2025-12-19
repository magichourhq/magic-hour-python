# v1.files






<!-- CUSTOM DOCS START -->

### Upload File <a name="upload-file"></a>

Upload a local file to Magic Hour Storage. The returned value is used for subsequent API calls.

#### Parameters

| Parameter | Required | Description                                                         | Example            |
| --------- | :------: | ------------------------------------------------------------------- | ------------------ |
| `file`    |    ✓     | A local file path, path like object, file URL, or file like object. | `"/tmp/image.png"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
file_path = client.v1.files.upload_file("/path/to/your/image.jpg")
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
file_path = await client.v1.files.upload_file("/path/to/your/image.jpg")
```


<!-- CUSTOM DOCS END -->
## Submodules
- [upload_urls](upload_urls/README.md) - upload_urls

