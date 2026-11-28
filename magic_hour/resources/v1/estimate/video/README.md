# v1.estimate.video

## Module Functions

### Estimate video credits <a name="list"></a>

Get the credits a video create request charges when it is submitted. Pass `tool`, then the fields below that the tool's create request uses, with the same values. Tools billed per frame charge an estimate at submission, assuming 30 fps for an uploaded video, and settle to the frames that render. Does not create a project or spend credits. It prices the fields passed here. It does not check your plan, your balance or the rest of the create request.

**API Endpoint**: `GET /v1/estimate/video`

#### Parameters

| Parameter             | Required | Description                                                                                                                                                                                                                                     | Example            |
| --------------------- | :------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `end_seconds`         |    ✓     | The `end_seconds` of the create request. Used by every tool.                                                                                                                                                                                    | `5.0`              |
| `tool`                |    ✓     | The create endpoint to price, named by its path. For example `image-to-video` for `POST /v1/image-to-video`.                                                                                                                                    | `"image-to-video"` |
| `audio`               |    ✗     | The `audio` of the create request. Used by `image-to-video`, `text-to-video`. Defaults to `false`.                                                                                                                                              | `True`             |
| `has_video_reference` |    ✗     | Whether any of the create request's `references` is a video. Used by `text-to-video`. Defaults to `false`.                                                                                                                                      | `True`             |
| `model`               |    ✗     | The `model` of the create request. Used by `image-to-video`, `text-to-video`, `ai-ugc-ad`, `ai-video-editor`, `character-replace`.                                                                                                              | `"kling-3.0"`      |
| `resolution`          |    ✗     | The `resolution` of the create request. Used by `image-to-video`, `text-to-video`, `ai-ugc-ad`, `ai-video-editor`, `character-replace`, `audio-to-video`, `ai-video-translator`, `ai-video-upscaler`. `ai-video-translator` defaults to `480p`. | `"720p"`           |
| `start_seconds`       |    ✗     | The `start_seconds` of the create request, for tools whose create request has it. Defaults to 0.                                                                                                                                                | `123.0`            |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.estimate.video.list(
    end_seconds=5.0, tool="image-to-video", model="kling-3.0", resolution="720p"
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.estimate.video.list(
    end_seconds=5.0, tool="image-to-video", model="kling-3.0", resolution="720p"
)
```

#### Response

##### Type

[V1EstimateVideoListResponse](/magic_hour/types/models/v1_estimate_video_list_response.py)

##### Example

```python
{"estimated_credits": 150}
```
