# v1.files.upload_urls

## Module Functions

### Generate asset upload urls <a name="create"></a>

Generates a list of pre-signed upload URLs for the assets required. This API is only necessary if you want to upload to Magic Hour's storage. Refer to the [Input Files Guide](/integration/input-files) for more details.

The response array will match the order of items in the request body.

**Valid file extensions per asset type**:
- video: mp4, m4v, mov, webm
- audio: mp3, wav, aac, flac, webm
- image: png, jpg, jpeg, heic, webp, avif, jp2, tiff, bmp
- gif: gif, webp, webm

> Note: `gif` is only supported for face swap API `video_file_path` field.

Once you receive an upload URL, send a `PUT` request to upload the file directly.

Example:

```
curl -X PUT --data '@/path/to/file/video.mp4' \
  https://videos.magichour.ai/api-assets/id/video.mp4?<auth params from the API response>
```

**API Endpoint**: `POST /v1/files/upload-urls`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `items` | ✓ | The list of assets to upload. The response array will match the order of items in the request body. | `[{"extension": "mp4", "type_": "video"}, {"extension": "mp3", "type_": "audio"}]` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.files.upload_urls.create(
    items=[
        {"extension": "mp4", "type_": "video"},
        {"extension": "mp3", "type_": "audio"},
    ]
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.files.upload_urls.create(
    items=[
        {"extension": "mp4", "type_": "video"},
        {"extension": "mp3", "type_": "audio"},
    ]
)

```

#### Response

##### Type
[V1FilesUploadUrlsCreateResponse](/magic_hour/types/models/v1_files_upload_urls_create_response.py)

##### Example
`{"items": [{"expires_at": "2024-07-25T16:56:21.932Z", "file_path": "api-assets/id/video.mp4", "upload_url": "https://videos.magichour.ai/api-assets/id/video.mp4?auth-value=1234567890"}, {"expires_at": "2024-07-25T16:56:21.932Z", "file_path": "api-assets/id/audio.mp3", "upload_url": "https://videos.magichour.ai/api-assets/id/audio.mp3?auth-value=1234567890"}]}`

