# Magic Hour Python SDK

[![PyPI - Version](https://img.shields.io/pypi/v/magic_hour)](https://pypi.org/project/magic_hour/)

The Magic Hour Python Library provides convenient access to the Magic Hour API. This library offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

## Documentation

For full documentation of all APIs, please visit https://docs.magichour.ai

If you have any questions, please reach out to us via [discord](https://discord.gg/JX5rgsZaJp).

## Install

```sh
pip install magic_hour
```

## Synchronous Client Usage

```python
from magic_hour import Client

# generate your API Key at https://magichour.ai/developer
client = Client(token="my api key")

response = client.v1.face_swap_photo.generate(
    assets={
        "face_swap_mode": "all-faces",
        "source_file_path": "api-assets/id/1234.png",
        "target_file_path": "api-assets/id/1234.png",
    },
    name="Face Swap image",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="./outputs/",
)
print(f"Project ID: {response.id}")
print(f"Status: {response.status}")
print(f"Downloaded files: {response.downloaded_paths}")
```

### Asynchronous Client Usage

```python
from magic_hour import AsyncClient

# generate your API Key at https://magichour.ai/developer
client = AsyncClient(token="my api key")

response = await client.v1.face_swap_photo.generate(
    assets={
        "face_swap_mode": "all-faces",
        "source_file_path": "api-assets/id/1234.png",
        "target_file_path": "api-assets/id/1234.png",
    },
    name="Face Swap image",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="./outputs/",
)
print(f"Project ID: {response.id}")
print(f"Status: {response.status}")
print(f"Downloaded files: {response.downloaded_paths}")
```

## Client Functions

Most resources that generate media content support two methods:

- **`generate()`** - A high-level convenience method that handles the entire workflow
- **`create()`** - A low-level method that only initiates the generation process

### Generate Function

The `generate()` function provides a complete end-to-end solution:

- Uploads local file to Magic Hour storage
- Calls the API to start generation
- Automatically polls for completion
- Downloads generated files to your local machine
- Returns both API response data and local file paths

**Additional Parameters:**

- `wait_for_completion` (bool, default True): Whether to wait for the project to complete
- `download_outputs` (bool, default True): Whether to download the generated files
- `download_directory` (str, optional): Directory to save downloaded files (defaults to current directory)

```python
# Generate function - handles everything automatically
response = client.v1.ai_image_generator.generate(
    style={"prompt": "A beautiful sunset over mountains"},
    name="Sunset Image",
    wait_for_completion=True,      # Wait for completion
    download_outputs=True,         # Download files automatically
    download_directory="./outputs/" # Where to save files
)

# You get both the API response AND downloaded file paths
print(f"Project ID: {response.id}")
print(f"Status: {response.status}")
print(f"Downloaded files: {response.downloaded_paths}")
```

### Create Function

The `create()` function provides granular control:

- Only calls the API to start the generation process
- Returns immediately with a project ID
- Requires manual status checking and file downloading

```python
# Create function - only starts the process
create_response = client.v1.ai_image_generator.create(
    style={"prompt": "A beautiful sunset over mountains"},
    name="Sunset Image"
)

# You get just the project ID and initial response
project_id = create_response.id
print(f"Started project: {project_id}")

# You must manually handle the rest:
# 1. Poll for completion using image_projects.get() or setup webhook
# 2. Download files using the download URLs
```

### Choosing Between Which Function to use

**Use `generate()` when:**

- You want a simple, one-call solution
- You're building a straightforward application
- You don't need custom polling or download logic

**Use `create()` when:**

- You need custom status checking logic
- You're integrating with existing job processing systems
- You want to separate generation initiation from completion handling
- You need fine-grained control over the entire workflow

## Module Documentation and Snippets

### [v1.ai_clothes_changer](magic_hour/resources/v1/ai_clothes_changer/README.md)

- [create](magic_hour/resources/v1/ai_clothes_changer/README.md#create) - AI Clothes Changer

### [v1.ai_face_editor](magic_hour/resources/v1/ai_face_editor/README.md)

- [create](magic_hour/resources/v1/ai_face_editor/README.md#create) - AI Face Editor

### [v1.ai_gif_generator](magic_hour/resources/v1/ai_gif_generator/README.md)

- [create](magic_hour/resources/v1/ai_gif_generator/README.md#create) - AI GIFs

### [v1.ai_headshot_generator](magic_hour/resources/v1/ai_headshot_generator/README.md)

- [create](magic_hour/resources/v1/ai_headshot_generator/README.md#create) - AI Headshots

### [v1.ai_image_editor](magic_hour/resources/v1/ai_image_editor/README.md)

- [create](magic_hour/resources/v1/ai_image_editor/README.md#create) - AI Image Editor

### [v1.ai_image_generator](magic_hour/resources/v1/ai_image_generator/README.md)

- [create](magic_hour/resources/v1/ai_image_generator/README.md#create) - AI Images

### [v1.ai_image_upscaler](magic_hour/resources/v1/ai_image_upscaler/README.md)

- [create](magic_hour/resources/v1/ai_image_upscaler/README.md#create) - AI Image Upscaler

### [v1.ai_meme_generator](magic_hour/resources/v1/ai_meme_generator/README.md)

- [create](magic_hour/resources/v1/ai_meme_generator/README.md#create) - AI Meme Generator

### [v1.ai_photo_editor](magic_hour/resources/v1/ai_photo_editor/README.md)

- [create](magic_hour/resources/v1/ai_photo_editor/README.md#create) - AI Photo Editor

### [v1.ai_qr_code_generator](magic_hour/resources/v1/ai_qr_code_generator/README.md)

- [create](magic_hour/resources/v1/ai_qr_code_generator/README.md#create) - AI QR Code

### [v1.ai_talking_photo](magic_hour/resources/v1/ai_talking_photo/README.md)

- [create](magic_hour/resources/v1/ai_talking_photo/README.md#create) - AI Talking Photo

### [v1.animation](magic_hour/resources/v1/animation/README.md)

- [create](magic_hour/resources/v1/animation/README.md#create) - Animation

### [v1.auto_subtitle_generator](magic_hour/resources/v1/auto_subtitle_generator/README.md)

- [create](magic_hour/resources/v1/auto_subtitle_generator/README.md#create) - Auto Subtitle Generator

### [v1.face_detection](magic_hour/resources/v1/face_detection/README.md)

- [create](magic_hour/resources/v1/face_detection/README.md#create) - Face Detection
- [get](magic_hour/resources/v1/face_detection/README.md#get) - Get face detection details

### [v1.face_swap](magic_hour/resources/v1/face_swap/README.md)

- [create](magic_hour/resources/v1/face_swap/README.md#create) - Face Swap video

### [v1.face_swap_photo](magic_hour/resources/v1/face_swap_photo/README.md)

- [create](magic_hour/resources/v1/face_swap_photo/README.md#create) - Face Swap Photo

### [v1.files.upload_urls](magic_hour/resources/v1/files/upload_urls/README.md)

- [create](magic_hour/resources/v1/files/upload_urls/README.md#create) - Generate asset upload urls

### [v1.image_background_remover](magic_hour/resources/v1/image_background_remover/README.md)

- [create](magic_hour/resources/v1/image_background_remover/README.md#create) - Image Background Remover

### [v1.image_projects](magic_hour/resources/v1/image_projects/README.md)

- [delete](magic_hour/resources/v1/image_projects/README.md#delete) - Delete image
- [get](magic_hour/resources/v1/image_projects/README.md#get) - Get image details

### [v1.image_to_video](magic_hour/resources/v1/image_to_video/README.md)

- [create](magic_hour/resources/v1/image_to_video/README.md#create) - Image-to-Video

### [v1.lip_sync](magic_hour/resources/v1/lip_sync/README.md)

- [create](magic_hour/resources/v1/lip_sync/README.md#create) - Lip Sync

### [v1.photo_colorizer](magic_hour/resources/v1/photo_colorizer/README.md)

- [create](magic_hour/resources/v1/photo_colorizer/README.md#create) - Photo Colorizer

### [v1.text_to_video](magic_hour/resources/v1/text_to_video/README.md)

- [create](magic_hour/resources/v1/text_to_video/README.md#create) - Text-to-Video

### [v1.video_projects](magic_hour/resources/v1/video_projects/README.md)

- [delete](magic_hour/resources/v1/video_projects/README.md#delete) - Delete video
- [get](magic_hour/resources/v1/video_projects/README.md#get) - Get video details

### [v1.video_to_video](magic_hour/resources/v1/video_to_video/README.md)

- [create](magic_hour/resources/v1/video_to_video/README.md#create) - Video-to-Video

<!-- MODULE DOCS END -->
