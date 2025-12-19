# v1.face_detection

## Module Functions






<!-- CUSTOM DOCS START -->

### Face Detection Generate Workflow <a name="generate"></a>

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
res = client.v1.face_detection.generate(
    assets={"target_file_path": "/path/to/1234.png"}, confidence_score=0.5
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.face_detection.generate(
    assets={"target_file_path": "/path/to/1234.png"}, confidence_score=0.5
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### Get face detection details <a name="get"></a>

Get the details of a face detection task. 

Use this API to get the list of faces detected in the image or video to use in the [face swap photo](/api-reference/face-swap-photo/face-swap-photo) or [face swap video](/api-reference/face-swap/face-swap-video) API calls for multi-face swaps.

**API Endpoint**: `GET /v1/face-detection/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The id of the task. This value is returned by the [face detection API](/api-reference/files/face-detection#response-id). | `"uuid-example"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.face_detection.get(id="uuid-example")

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.face_detection.get(id="uuid-example")

```

#### Response

##### Type
[V1FaceDetectionGetResponse](/magic_hour/types/models/v1_face_detection_get_response.py)

##### Example
`{"credits_charged": 0, "faces": [{"path": "api-assets/id/0-0.png", "url": "https://videos.magichour.ai/api-assets/id/0-0.png"}], "id": "uuid-example", "status": "complete"}`

### Face Detection <a name="create"></a>

Detect faces in an image or video. 
      
Use this API to get the list of faces detected in the image or video to use in the [face swap photo](/api-reference/face-swap-photo/face-swap-photo) or [face swap video](/api-reference/face-swap/face-swap-video) API calls for multi-face swaps.

Note: Face detection is free to use for the near future. Pricing may change in the future.

**API Endpoint**: `POST /v1/face-detection`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for face detection | `{"target_file_path": "api-assets/id/1234.png"}` |
| `└─ target_file_path` | ✓ | This is the image or video where the face will be detected. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.png"` |
| `confidence_score` | ✗ | Confidence threshold for filtering detected faces.  * Higher values (e.g., 0.9) include only faces detected with high certainty, reducing false positives.  * Lower values (e.g., 0.3) include more faces, but may increase the chance of incorrect detections. | `0.5` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.face_detection.create(
    assets={"target_file_path": "api-assets/id/1234.png"}, confidence_score=0.5
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.face_detection.create(
    assets={"target_file_path": "api-assets/id/1234.png"}, confidence_score=0.5
)

```

#### Response

##### Type
[V1FaceDetectionCreateResponse](/magic_hour/types/models/v1_face_detection_create_response.py)

##### Example
`{"credits_charged": 123, "id": "uuid-example"}`

