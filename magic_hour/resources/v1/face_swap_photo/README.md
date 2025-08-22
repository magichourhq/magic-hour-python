# v1_face_swap_photo

## Module Functions

<!-- CUSTOM DOCS START -->

<!-- CUSTOM DOCS END -->

### Face Swap Photo <a name="create"></a>

Create a face swap photo. Each photo costs 5 credits. The height/width of the output image depends on your subscription. Please refer to our [pricing](https://magichour.ai/pricing) page for more details

**API Endpoint**: `POST /v1/face-swap-photo`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `assets` | ✓ | Provide the assets for face swap photo | `{"face_mappings": [{"new_face": "api-assets/id/1234.png", "original_face": "api-assets/id/0-0.png"}], "face_swap_mode": "all-faces", "source_file_path": "api-assets/id/1234.png", "target_file_path": "api-assets/id/1234.png"}` |
| `└─ face_mappings` | ✗ | This is the array of face mappings used for multiple face swap. The value is required if `face_swap_mode` is `individual-faces`. | `[{"new_face": "api-assets/id/1234.png", "original_face": "api-assets/id/0-0.png"}]` |
| `└─ face_swap_mode` | ✗ | The mode of face swap. * `all-faces` - Swap all faces in the target image or video. `source_file_path` is required. * `individual-faces` - Swap individual faces in the target image or video. `source_faces` is required. | `"all-faces"` |
| `└─ source_file_path` | ✗ | This is the image from which the face is extracted. The value is required if `face_swap_mode` is `all-faces`.  This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.png"` |
| `└─ target_file_path` | ✓ | This is the image where the face from the source image will be placed. This value is either - a direct URL to the video file - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).  Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.  | `"api-assets/id/1234.png"` |
| `name` | ✗ | The name of image. This value is mainly used for your own identification of the image. | `"Face Swap image"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.face_swap_photo.create(
    assets={
        "face_mappings": [
            {
                "new_face": "api-assets/id/1234.png",
                "original_face": "api-assets/id/0-0.png",
            }
        ],
        "face_swap_mode": "all-faces",
        "source_file_path": "api-assets/id/1234.png",
        "target_file_path": "api-assets/id/1234.png",
    },
    name="Face Swap image",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.face_swap_photo.create(
    assets={
        "face_mappings": [
            {
                "new_face": "api-assets/id/1234.png",
                "original_face": "api-assets/id/0-0.png",
            }
        ],
        "face_swap_mode": "all-faces",
        "source_file_path": "api-assets/id/1234.png",
        "target_file_path": "api-assets/id/1234.png",
    },
    name="Face Swap image",
)

```

#### Response

##### Type
[V1FaceSwapPhotoCreateResponse](/magic_hour/types/models/v1_face_swap_photo_create_response.py)

##### Example
`{"credits_charged": 5, "frame_cost": 5, "id": "cuid-example"}`

