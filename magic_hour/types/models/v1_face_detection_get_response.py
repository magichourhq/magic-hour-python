import pydantic
import typing
import typing_extensions

from .v1_face_detection_get_response_faces_item import (
    V1FaceDetectionGetResponseFacesItem,
)


class V1FaceDetectionGetResponse(pydantic.BaseModel):
    """
    V1FaceDetectionGetResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    credits_charged: int = pydantic.Field(
        alias="credits_charged",
    )
    """
    The credits charged for the task.
    """
    faces: typing.List[V1FaceDetectionGetResponseFacesItem] = pydantic.Field(
        alias="faces",
    )
    """
    The faces detected in the image or video. The list is populated as faces are detected.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    The id of the task. This value is returned by the [face detection API](/api-reference/files/face-detection#response-id).
    """
    status: typing_extensions.Literal["complete", "error", "queued", "rendering"] = (
        pydantic.Field(
            alias="status",
        )
    )
    """
    The status of the detection.
    """
