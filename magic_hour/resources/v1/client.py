from magic_hour.resources.v1.ai_clothes_changer import (
    AiClothesChangerClient,
    AsyncAiClothesChangerClient,
)
from magic_hour.resources.v1.ai_face_editor import (
    AiFaceEditorClient,
    AsyncAiFaceEditorClient,
)
from magic_hour.resources.v1.ai_gif_generator import (
    AiGifGeneratorClient,
    AsyncAiGifGeneratorClient,
)
from magic_hour.resources.v1.ai_headshot_generator import (
    AiHeadshotGeneratorClient,
    AsyncAiHeadshotGeneratorClient,
)
from magic_hour.resources.v1.ai_image_editor import (
    AiImageEditorClient,
    AsyncAiImageEditorClient,
)
from magic_hour.resources.v1.ai_image_generator import (
    AiImageGeneratorClient,
    AsyncAiImageGeneratorClient,
)
from magic_hour.resources.v1.ai_image_upscaler import (
    AiImageUpscalerClient,
    AsyncAiImageUpscalerClient,
)
from magic_hour.resources.v1.ai_meme_generator import (
    AiMemeGeneratorClient,
    AsyncAiMemeGeneratorClient,
)
from magic_hour.resources.v1.ai_photo_editor import (
    AiPhotoEditorClient,
    AsyncAiPhotoEditorClient,
)
from magic_hour.resources.v1.ai_qr_code_generator import (
    AiQrCodeGeneratorClient,
    AsyncAiQrCodeGeneratorClient,
)
from magic_hour.resources.v1.ai_talking_photo import (
    AiTalkingPhotoClient,
    AsyncAiTalkingPhotoClient,
)
from magic_hour.resources.v1.ai_voice_generator import (
    AiVoiceGeneratorClient,
    AsyncAiVoiceGeneratorClient,
)
from magic_hour.resources.v1.animation import AnimationClient, AsyncAnimationClient
from magic_hour.resources.v1.audio_projects import (
    AsyncAudioProjectsClient,
    AudioProjectsClient,
)
from magic_hour.resources.v1.auto_subtitle_generator import (
    AsyncAutoSubtitleGeneratorClient,
    AutoSubtitleGeneratorClient,
)
from magic_hour.resources.v1.face_detection import (
    AsyncFaceDetectionClient,
    FaceDetectionClient,
)
from magic_hour.resources.v1.face_swap import AsyncFaceSwapClient, FaceSwapClient
from magic_hour.resources.v1.face_swap_photo import (
    AsyncFaceSwapPhotoClient,
    FaceSwapPhotoClient,
)
from magic_hour.resources.v1.files import AsyncFilesClient, FilesClient
from magic_hour.resources.v1.image_background_remover import (
    AsyncImageBackgroundRemoverClient,
    ImageBackgroundRemoverClient,
)
from magic_hour.resources.v1.image_projects import (
    AsyncImageProjectsClient,
    ImageProjectsClient,
)
from magic_hour.resources.v1.image_to_video import (
    AsyncImageToVideoClient,
    ImageToVideoClient,
)
from magic_hour.resources.v1.lip_sync import AsyncLipSyncClient, LipSyncClient
from magic_hour.resources.v1.photo_colorizer import (
    AsyncPhotoColorizerClient,
    PhotoColorizerClient,
)
from magic_hour.resources.v1.text_to_video import (
    AsyncTextToVideoClient,
    TextToVideoClient,
)
from magic_hour.resources.v1.video_projects import (
    AsyncVideoProjectsClient,
    VideoProjectsClient,
)
from magic_hour.resources.v1.video_to_video import (
    AsyncVideoToVideoClient,
    VideoToVideoClient,
)
from make_api_request import AsyncBaseClient, SyncBaseClient


class V1Client:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.image_projects = ImageProjectsClient(base_client=self._base_client)
        self.video_projects = VideoProjectsClient(base_client=self._base_client)
        self.face_detection = FaceDetectionClient(base_client=self._base_client)
        self.ai_clothes_changer = AiClothesChangerClient(base_client=self._base_client)
        self.ai_face_editor = AiFaceEditorClient(base_client=self._base_client)
        self.ai_gif_generator = AiGifGeneratorClient(base_client=self._base_client)
        self.ai_headshot_generator = AiHeadshotGeneratorClient(
            base_client=self._base_client
        )
        self.ai_image_editor = AiImageEditorClient(base_client=self._base_client)
        self.ai_image_generator = AiImageGeneratorClient(base_client=self._base_client)
        self.ai_image_upscaler = AiImageUpscalerClient(base_client=self._base_client)
        self.ai_meme_generator = AiMemeGeneratorClient(base_client=self._base_client)
        self.ai_photo_editor = AiPhotoEditorClient(base_client=self._base_client)
        self.ai_qr_code_generator = AiQrCodeGeneratorClient(
            base_client=self._base_client
        )
        self.ai_talking_photo = AiTalkingPhotoClient(base_client=self._base_client)
        self.animation = AnimationClient(base_client=self._base_client)
        self.auto_subtitle_generator = AutoSubtitleGeneratorClient(
            base_client=self._base_client
        )
        self.face_swap = FaceSwapClient(base_client=self._base_client)
        self.face_swap_photo = FaceSwapPhotoClient(base_client=self._base_client)
        self.files = FilesClient(base_client=self._base_client)
        self.image_background_remover = ImageBackgroundRemoverClient(
            base_client=self._base_client
        )
        self.image_to_video = ImageToVideoClient(base_client=self._base_client)
        self.lip_sync = LipSyncClient(base_client=self._base_client)
        self.photo_colorizer = PhotoColorizerClient(base_client=self._base_client)
        self.text_to_video = TextToVideoClient(base_client=self._base_client)
        self.video_to_video = VideoToVideoClient(base_client=self._base_client)
        self.audio_projects = AudioProjectsClient(base_client=self._base_client)
        self.ai_voice_generator = AiVoiceGeneratorClient(base_client=self._base_client)


class AsyncV1Client:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.image_projects = AsyncImageProjectsClient(base_client=self._base_client)
        self.video_projects = AsyncVideoProjectsClient(base_client=self._base_client)
        self.face_detection = AsyncFaceDetectionClient(base_client=self._base_client)
        self.ai_clothes_changer = AsyncAiClothesChangerClient(
            base_client=self._base_client
        )
        self.ai_face_editor = AsyncAiFaceEditorClient(base_client=self._base_client)
        self.ai_gif_generator = AsyncAiGifGeneratorClient(base_client=self._base_client)
        self.ai_headshot_generator = AsyncAiHeadshotGeneratorClient(
            base_client=self._base_client
        )
        self.ai_image_editor = AsyncAiImageEditorClient(base_client=self._base_client)
        self.ai_image_generator = AsyncAiImageGeneratorClient(
            base_client=self._base_client
        )
        self.ai_image_upscaler = AsyncAiImageUpscalerClient(
            base_client=self._base_client
        )
        self.ai_meme_generator = AsyncAiMemeGeneratorClient(
            base_client=self._base_client
        )
        self.ai_photo_editor = AsyncAiPhotoEditorClient(base_client=self._base_client)
        self.ai_qr_code_generator = AsyncAiQrCodeGeneratorClient(
            base_client=self._base_client
        )
        self.ai_talking_photo = AsyncAiTalkingPhotoClient(base_client=self._base_client)
        self.animation = AsyncAnimationClient(base_client=self._base_client)
        self.auto_subtitle_generator = AsyncAutoSubtitleGeneratorClient(
            base_client=self._base_client
        )
        self.face_swap = AsyncFaceSwapClient(base_client=self._base_client)
        self.face_swap_photo = AsyncFaceSwapPhotoClient(base_client=self._base_client)
        self.files = AsyncFilesClient(base_client=self._base_client)
        self.image_background_remover = AsyncImageBackgroundRemoverClient(
            base_client=self._base_client
        )
        self.image_to_video = AsyncImageToVideoClient(base_client=self._base_client)
        self.lip_sync = AsyncLipSyncClient(base_client=self._base_client)
        self.photo_colorizer = AsyncPhotoColorizerClient(base_client=self._base_client)
        self.text_to_video = AsyncTextToVideoClient(base_client=self._base_client)
        self.video_to_video = AsyncVideoToVideoClient(base_client=self._base_client)
        self.audio_projects = AsyncAudioProjectsClient(base_client=self._base_client)
        self.ai_voice_generator = AsyncAiVoiceGeneratorClient(
            base_client=self._base_client
        )
