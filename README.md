# Magic Hour Python SDK

[![PyPI - Version](https://img.shields.io/pypi/v/magic_hour)](https://pypi.org/project/magic_hour/)

Magic Hour provides an API (beta) that can be integrated into your own application to generate videos and images using AI.

Webhook documentation can be found [here](https://magichour.ai/docs/webhook).

If you have any questions, please reach out to us via [discord](https://discord.gg/JX5rgsZaJp).

## Install

```
pip install magic_hour
```

## Usage

Initialize the client

### Synchronous Client

```python
from magic_hour import Client

# generate your API Key at https://magichour.ai/developer
client = Client(token="my api key")
```

### Asynchronous Client

```python
from magic_hour import AsyncClient

# generate your API Key at https://magichour.ai/developer
client = AsyncClient(token="my api key")
```

> [!WARNING]
> Any API call that renders a video will utilize frames in your account.

## Module Documentation and Snippets

### [v1.ai_clothes_changer](magic_hour/resources/v1/ai_clothes_changer/README.md)

* [create](magic_hour/resources/v1/ai_clothes_changer/README.md#create) - AI Clothes Changer

### [v1.ai_headshot_generator](magic_hour/resources/v1/ai_headshot_generator/README.md)

* [create](magic_hour/resources/v1/ai_headshot_generator/README.md#create) - AI Headshots

### [v1.ai_image_generator](magic_hour/resources/v1/ai_image_generator/README.md)

* [create](magic_hour/resources/v1/ai_image_generator/README.md#create) - AI Images

### [v1.ai_image_upscaler](magic_hour/resources/v1/ai_image_upscaler/README.md)

* [create](magic_hour/resources/v1/ai_image_upscaler/README.md#create) - AI Image Upscaler

### [v1.ai_photo_editor](magic_hour/resources/v1/ai_photo_editor/README.md)

* [create](magic_hour/resources/v1/ai_photo_editor/README.md#create) - AI Photo Editor

### [v1.ai_qr_code_generator](magic_hour/resources/v1/ai_qr_code_generator/README.md)

* [create](magic_hour/resources/v1/ai_qr_code_generator/README.md#create) - AI QR Code

### [v1.animation](magic_hour/resources/v1/animation/README.md)

* [create](magic_hour/resources/v1/animation/README.md#create) - Animation

### [v1.face_swap](magic_hour/resources/v1/face_swap/README.md)

* [create](magic_hour/resources/v1/face_swap/README.md#create) - Face Swap video

### [v1.face_swap_photo](magic_hour/resources/v1/face_swap_photo/README.md)

* [create](magic_hour/resources/v1/face_swap_photo/README.md#create) - Face Swap Photo

### [v1.files.upload_urls](magic_hour/resources/v1/files/upload_urls/README.md)

* [create](magic_hour/resources/v1/files/upload_urls/README.md#create) - Generate asset upload urls

### [v1.image_background_remover](magic_hour/resources/v1/image_background_remover/README.md)

* [create](magic_hour/resources/v1/image_background_remover/README.md#create) - Image Background Remover

### [v1.image_projects](magic_hour/resources/v1/image_projects/README.md)

* [delete](magic_hour/resources/v1/image_projects/README.md#delete) - Delete image
* [get](magic_hour/resources/v1/image_projects/README.md#get) - Get image details

### [v1.image_to_video](magic_hour/resources/v1/image_to_video/README.md)

* [create](magic_hour/resources/v1/image_to_video/README.md#create) - Image-to-Video

### [v1.lip_sync](magic_hour/resources/v1/lip_sync/README.md)

* [create](magic_hour/resources/v1/lip_sync/README.md#create) - Lip Sync

### [v1.text_to_video](magic_hour/resources/v1/text_to_video/README.md)

* [create](magic_hour/resources/v1/text_to_video/README.md#create) - Text-to-Video

### [v1.video_projects](magic_hour/resources/v1/video_projects/README.md)

* [delete](magic_hour/resources/v1/video_projects/README.md#delete) - Delete video
* [get](magic_hour/resources/v1/video_projects/README.md#get) - Get video details

### [v1.video_to_video](magic_hour/resources/v1/video_to_video/README.md)

* [create](magic_hour/resources/v1/video_to_video/README.md#create) - Video-to-Video

<!-- MODULE DOCS END -->
