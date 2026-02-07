# v1.photo_colorizer

## Module Functions

<!-- CUSTOM DOCS START -->

### Photo Colorizer Generate Workflow <a name="generate"></a>

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
res = client.v1.photo_colorizer.generate(
    assets={"image_file_path": "/path/to/1234.png"}, name="Photo Colorizer image"
    wait_for_completion=True,
    download_outputs=True,
    download_directory="."
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.photo_colorizer.generate(
    assets={"image_file_path": "/path/to/1234.png"}, name="Photo Colorizer image"
    wait_for_completion=True,
    download_outputs=True,
    download_directory="."
)
```

<!-- CUSTOM DOCS END -->

### Photo Colorizer <a name="create"></a>

Colorize image. Each image costs 10 credits.

**API Endpoint**: `POST /v1/photo-colorizer`

#### Parameters

| Parameter            | Required | Description                                                                                                                                                                                                                                                                                                                                                                   | Example                                         |
| -------------------- | :------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| `assets`             |    ✓     | Provide the assets for photo colorization                                                                                                                                                                                                                                                                                                                                     | `{"image_file_path": "api-assets/id/1234.png"}` |
| `└─ image_file_path` |    ✓     | The image used to generate the colorized image. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls). See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details. | `"api-assets/id/1234.png"`                      |
| `name`               |    ✗     | Give your image a custom name for easy identification.                                                                                                                                                                                                                                                                                                                        | `"My Photo Colorizer image"`                    |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.photo_colorizer.create(
    assets={"image_file_path": "api-assets/id/1234.png"},
    name="My Photo Colorizer image",
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.photo_colorizer.create(
    assets={"image_file_path": "api-assets/id/1234.png"},
    name="My Photo Colorizer image",
)
```

#### Response

##### Type

[V1PhotoColorizerCreateResponse](/magic_hour/types/models/v1_photo_colorizer_create_response.py)

##### Example

```python
{"credits_charged": 10, "frame_cost": 10, "id": "cuid-example"}
```
