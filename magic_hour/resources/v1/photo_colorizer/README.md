# v1_photo_colorizer

## Module Functions

<!-- CUSTOM DOCS START -->

<!-- CUSTOM DOCS END -->

### Photo Colorizer <a name="create"></a>

Colorize image. Each image costs 5 credits.

**API Endpoint**: `POST /v1/photo-colorizer`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for photo colorization | `{"image_file_path": "api-assets/id/1234.png"}` |
| `└─ image_file_path` | ✓ | The image used to generate the colorized image. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.png"` |
| `name` | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Photo Colorizer image"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.photo_colorizer.create(
    assets={"image_file_path": "api-assets/id/1234.png"}, name="Photo Colorizer image"
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.photo_colorizer.create(
    assets={"image_file_path": "api-assets/id/1234.png"}, name="Photo Colorizer image"
)

```

#### Response

##### Type
[V1PhotoColorizerCreateResponse](/magic_hour/types/models/v1_photo_colorizer_create_response.py)

##### Example
`{"credits_charged": 5, "frame_cost": 5, "id": "cuid-example"}`

