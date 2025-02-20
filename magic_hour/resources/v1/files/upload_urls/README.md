
### create <a name="create"></a>
Generate asset upload urls

Create a list of urls used to upload the assets needed to generate a video. Each video type has their own requirements on what assets are required. Please refer to the specific mode API for more details. The response array will be in the same order as the request body.

Below is the list of valid extensions for each asset type:

- video: mp4, m4v, mov, webm
- audio: mp3, mpeg, wav, aac, aiff, flac
- image: png, jpg, jpeg, webp, avif, jp2, tiff, bmp

Note: `.gif` is supported for face swap API `video_file_path` field.

After receiving the upload url, you can upload the file by sending a PUT request with the header `'Content-Type: application/octet-stream'`.

For example using curl

```
curl -X PUT -H 'Content-Type: application/octet-stream' \
  --data '@/path/to/file/video.mp4' \
  https://videos.magichour.ai/api-assets/id/video.mp4?auth-value=1234567890
```


**API Endpoint**: `POST /v1/files/upload-urls`

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.files.upload_urls.create(
    items=[
        {"extension": "mp4", "type_field": "video"},
        {"extension": "mp3", "type_field": "audio"},
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
        {"extension": "mp4", "type_field": "video"},
        {"extension": "mp3", "type_field": "audio"},
    ]
)
```
