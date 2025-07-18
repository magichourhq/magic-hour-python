
### Delete video <a name="delete"></a>

Permanently delete the rendered video. This action is not reversible, please be sure before deleting.

**API Endpoint**: `DELETE /v1/video-projects/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The id of the video project | `"cm6pvghix03bvyz0zwash6noj"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.video_projects.delete(id="cm6pvghix03bvyz0zwash6noj")

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.video_projects.delete(id="cm6pvghix03bvyz0zwash6noj")

```

### Get video details <a name="get"></a>

Get the details of a video project. The `downloads` field will be empty unless the video was successfully rendered.

The video can be one of the following status
- `draft` - not currently used
- `queued` - the job is queued and waiting for a GPU
- `rendering` - the generation is in progress
- `complete` - the video is successful created
- `error` - an error occurred during rendering
- `canceled` - video render is canceled by the user


**API Endpoint**: `GET /v1/video-projects/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The id of the video | `"cm6pvghix03bvyz0zwash6noj"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.video_projects.get(id="cm6pvghix03bvyz0zwash6noj")

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.video_projects.get(id="cm6pvghix03bvyz0zwash6noj")

```

#### Response

##### Type
[V1VideoProjectsGetResponse](/magic_hour/types/models/v1_video_projects_get_response.py)

##### Example
`{"created_at": "1970-01-01T00:00:00", "credits_charged": 450, "download": {"expires_at": "2024-10-19T05:16:19.027Z", "url": "https://videos.magichour.ai/id/output.mp4"}, "downloads": [{"expires_at": "2024-10-19T05:16:19.027Z", "url": "https://videos.magichour.ai/id/output.mp4"}], "enabled": True, "end_seconds": 15.0, "error": {"code": "no_source_face", "message": "Please use an image with a detectable face"}, "fps": 30.0, "height": 960, "id": "clx7uu86w0a5qp55yxz315r6r", "name": "Example Name", "start_seconds": 0.0, "status": "complete", "total_frame_cost": 450, "type_": "FACE_SWAP", "width": 512}`
