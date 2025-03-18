
### delete <a name="delete"></a>
Delete video

Permanently delete the rendered video. This action is not reversible, please be sure before deleting.

**API Endpoint**: `DELETE /v1/video-projects/{id}`

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

### get <a name="get"></a>
Get video details

Get the details of a video project. The `downloads` field will be empty unless the video was successfully rendered.

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
res = client.v1.video_projects.get(id="cm6pvghix03bvyz0zwash6noj")
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.video_projects.get(id="cm6pvghix03bvyz0zwash6noj")
```
