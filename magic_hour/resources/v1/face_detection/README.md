
### Get face detection details <a name="get"></a>

Get the details of a face detection task.

**API Endpoint**: `GET /v1/face-detection/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The id of the task | `"string"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.face_detection.get(id="string")

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.face_detection.get(id="string")

```

#### Response

##### Type
[V1FaceDetectionGetResponse](/magic_hour/types/models/v1_face_detection_get_response.py)

##### Example
`{"credits_charged": 123, "faces": [{"path": "api-assets/id/0-0.png", "url": "https://videos.magichour.ai/api-assets/id/0-0.png"}], "id": "string", "status": "complete"}`

### Face Detection <a name="create"></a>

Detect faces in an image or video. 

Note: Face detection is free to use for the near future. Pricing may change in the future.

**API Endpoint**: `POST /v1/face-detection`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for face detection | `{"target_file_path": "api-assets/id/1234.png"}` |
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
`{"credits_charged": 123, "id": "string"}`
