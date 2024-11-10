# SDK Usage Examples

## Module v1.video_projects

### Get video project details

Get the details of a video project. The `download` field will be `null` unless the video was successfully rendered.

The video can be one of the following status

- `draft` - not currently used
- `queued` - the job is queued and waiting for a GPU
- `rendering` - the generation is in progress
- `complete` - the video is successful created
- `error` - an error occurred during rendering
- `canceled` - video render is canceled by the user

**API Endpoint**: `GET /v1/video-projects/{id}`

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.video_projects.get(id="string")
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.video_projects.get(id="string")
```

**Upgrade to see all examples**
