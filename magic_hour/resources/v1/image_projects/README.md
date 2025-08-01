
### Delete image <a name="delete"></a>

Permanently delete the rendered image. This action is not reversible, please be sure before deleting.

**API Endpoint**: `DELETE /v1/image-projects/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The id of the image project | `"cm6pvghix03bvyz0zwash6noj"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.image_projects.delete(id="cm6pvghix03bvyz0zwash6noj")

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.image_projects.delete(id="cm6pvghix03bvyz0zwash6noj")

```

### Get image details <a name="get"></a>

Get the details of a image project. The `downloads` field will be empty unless the image was successfully rendered.

The image can be one of the following status
- `draft` - not currently used
- `queued` - the job is queued and waiting for a GPU
- `rendering` - the generation is in progress
- `complete` - the image is successful created
- `error` - an error occurred during rendering
- `canceled` - image render is canceled by the user


**API Endpoint**: `GET /v1/image-projects/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The id of the image project | `"cm6pvghix03bvyz0zwash6noj"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.image_projects.get(id="cm6pvghix03bvyz0zwash6noj")

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.image_projects.get(id="cm6pvghix03bvyz0zwash6noj")

```

#### Response

##### Type
[V1ImageProjectsGetResponse](/magic_hour/types/models/v1_image_projects_get_response.py)

##### Example
`{"created_at": "1970-01-01T00:00:00", "credits_charged": 5, "downloads": [{"expires_at": "2024-10-19T05:16:19.027Z", "url": "https://videos.magichour.ai/id/output.png"}], "enabled": True, "error": {"code": "no_source_face", "message": "Please use an image with a detectable face"}, "id": "clx7uu86w0a5qp55yxz315r6r", "image_count": 1, "name": "Example Name", "status": "complete", "total_frame_cost": 5, "type_": "AI_IMAGE"}`
