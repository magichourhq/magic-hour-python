"""
Generated by Sideko (sideko.dev)
"""

from magic_hour.core import AsyncBaseClient, SyncBaseClient
from magic_hour.resources.v1.image_projects import (
    AsyncImageProjectsClient,
    ImageProjectsClient,
)
from magic_hour.resources.v1.video_projects import (
    AsyncVideoProjectsClient,
    VideoProjectsClient,
)
from magic_hour.resources.v1.ai_headshot_generator import (
    AiHeadshotGeneratorClient,
    AsyncAiHeadshotGeneratorClient,
)
from magic_hour.resources.v1.ai_image_generator import (
    AiImageGeneratorClient,
    AsyncAiImageGeneratorClient,
)
from magic_hour.resources.v1.face_swap import AsyncFaceSwapClient, FaceSwapClient
from magic_hour.resources.v1.face_swap_photo import (
    AsyncFaceSwapPhotoClient,
    FaceSwapPhotoClient,
)
from magic_hour.resources.v1.files import AsyncFilesClient, FilesClient
from magic_hour.resources.v1.image_to_video import (
    AsyncImageToVideoClient,
    ImageToVideoClient,
)
from magic_hour.resources.v1.lip_sync import AsyncLipSyncClient, LipSyncClient
from magic_hour.resources.v1.text_to_video import (
    AsyncTextToVideoClient,
    TextToVideoClient,
)
from magic_hour.resources.v1.video_to_video import (
    AsyncVideoToVideoClient,
    VideoToVideoClient,
)


class V1Client:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.image_projects = ImageProjectsClient(base_client=self._base_client)
        self.video_projects = VideoProjectsClient(base_client=self._base_client)
        self.ai_headshot_generator = AiHeadshotGeneratorClient(
            base_client=self._base_client
        )
        self.ai_image_generator = AiImageGeneratorClient(base_client=self._base_client)
        self.face_swap = FaceSwapClient(base_client=self._base_client)
        self.face_swap_photo = FaceSwapPhotoClient(base_client=self._base_client)
        self.files = FilesClient(base_client=self._base_client)
        self.image_to_video = ImageToVideoClient(base_client=self._base_client)
        self.lip_sync = LipSyncClient(base_client=self._base_client)
        self.text_to_video = TextToVideoClient(base_client=self._base_client)
        self.video_to_video = VideoToVideoClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncV1Client:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.image_projects = AsyncImageProjectsClient(base_client=self._base_client)
        self.video_projects = AsyncVideoProjectsClient(base_client=self._base_client)
        self.ai_headshot_generator = AsyncAiHeadshotGeneratorClient(
            base_client=self._base_client
        )
        self.ai_image_generator = AsyncAiImageGeneratorClient(
            base_client=self._base_client
        )
        self.face_swap = AsyncFaceSwapClient(base_client=self._base_client)
        self.face_swap_photo = AsyncFaceSwapPhotoClient(base_client=self._base_client)
        self.files = AsyncFilesClient(base_client=self._base_client)
        self.image_to_video = AsyncImageToVideoClient(base_client=self._base_client)
        self.lip_sync = AsyncLipSyncClient(base_client=self._base_client)
        self.text_to_video = AsyncTextToVideoClient(base_client=self._base_client)
        self.video_to_video = AsyncVideoToVideoClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
