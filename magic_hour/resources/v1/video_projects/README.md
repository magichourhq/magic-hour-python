# v1.video_projects

## Module Functions






<!-- CUSTOM DOCS START -->

### Check results <a name="check-result"></a>

Poll the details API to check on the status of the rendering. Optionally can also download the output

#### Parameters

| Parameter             | Required | Description                                                                                          | Example          |
| --------------------- | :------: | ---------------------------------------------------------------------------------------------------- | ---------------- |
| `id`                  |    ✓     | Unique ID of the video project. This value is returned by all of the POST APIs that create an video. | `"cuid-example"` |
| `wait_for_completion` |    ✗     | Whether to wait for the project to complete.                                                         | `True`           |
| `download_outputs`    |    ✗     | Whether to download the generated files                                                              | `True`           |
| `download_directory`  |    ✗     | Directory to save downloaded files (defaults to current directory)                                   | `"./outputs"`    |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.video_projects.check_result(
  id="cuid-example",
  wait_for_completion=True,
  download_outputs=True,
  download_directory="outputs",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.video_projects.check_result(
  id="cuid-example",
  wait_for_completion=True,
  download_outputs=True,
  download_directory="outputs",
)
```

<!-- CUSTOM DOCS END -->
### Delete video <a name="delete"></a>

Permanently delete the rendered video. This action is not reversible, please be sure before deleting.

**API Endpoint**: `DELETE /v1/video-projects/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | Unique ID of the video project. This value is returned by all of the POST APIs that create a video. | `"cuid-example"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.video_projects.delete(id="cuid-example")

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.video_projects.delete(id="cuid-example")

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
| `id` | ✓ | Unique ID of the video project. This value is returned by all of the POST APIs that create a video. | `"cuid-example"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.video_projects.get(id="cuid-example")

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.video_projects.get(id="cuid-example")

```

#### Response

##### Type
[V1VideoProjectsGetResponse](/magic_hour/types/models/v1_video_projects_get_response.py)

##### Example
`{"created_at": "1970-01-01T00:00:00", "credits_charged": 450, "download": {"expires_at": "2024-10-19T05:16:19.027Z", "url": "https://videos.magichour.ai/id/output.mp4"}, "downloads": [{"expires_at": "2024-10-19T05:16:19.027Z", "url": "https://videos.magichour.ai/id/output.mp4"}], "enabled": True, "end_seconds": 15.0, "error": {"code": "no_source_face", "message": "Please use an image with a detectable face"}, "fps": 30.0, "height": 960, "id": "cuid-example", "name": "Example Name", "start_seconds": 0.0, "status": "complete", "total_frame_cost": 450, "type_": "FACE_SWAP", "width": 512}`

