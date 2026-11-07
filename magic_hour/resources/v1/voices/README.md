# v1.voices

## Module Functions

### List voices <a name="list"></a>

List the voices available for text-to-speech. Use a voice's `id` as `style.voice_name` in the AI Voice Generator API. To fetch the next page, pass the response's next_cursor as cursor.

**API Endpoint**: `GET /v1/voices`

#### Parameters

| Parameter | Required | Description                                                        | Example    |
| --------- | :------: | ------------------------------------------------------------------ | ---------- |
| `cursor`  |    ✗     | Opaque pagination cursor from the previous response's next_cursor. | `"string"` |
| `limit`   |    ✗     | Maximum number of voices to return. Defaults to 20.                | `20`       |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.voices.list(limit=20)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.voices.list(limit=20)
```

#### Response

##### Type

[V1VoicesListResponse](/magic_hour/types/models/v1_voices_list_response.py)

##### Example

```python
{"next_cursor": "string", "voices": [{"avatar_url": "https://d28dkohlqf5vwj.cloudfront.net/models/nano-banana/female-portrait-turtleneck.webp", "id": "cv-0001", "name": "Ashley", "preview_url": "https://videos.magichour.ai/presets/voices/v2/cv-0001-ashley.mp3"}]}
```
