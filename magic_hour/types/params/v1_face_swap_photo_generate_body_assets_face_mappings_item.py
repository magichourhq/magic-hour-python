import pydantic
import typing_extensions


class V1FaceSwapPhotoGenerateBodyAssetsFaceMappingsItem(typing_extensions.TypedDict):
    """
    V1FaceSwapPhotoGenerateBodyAssetsFaceMappingsItem
    """

    new_face: typing_extensions.Required[str]
    """
    The face image that will be used to replace the face in the `original_face`. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """

    original_face: typing_extensions.Required[str]
    """
    The face detected from the image in `target_file_path`. The file name is in the format of `<face_frame>-<face_index>.png`. This value is corresponds to the response in the [face detection API](https://docs.magichour.ai/api-reference/files/get-face-detection-details).
    
    * The face_frame is the frame number of the face in the target image. For images, the frame number is always 0.
    * The face_index is the index of the face in the target image, starting from 0 going left to right.
    """
