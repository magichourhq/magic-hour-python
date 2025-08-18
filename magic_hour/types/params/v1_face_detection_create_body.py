import pydantic
import typing
import typing_extensions

from .v1_face_detection_create_body_assets import (
    V1FaceDetectionCreateBodyAssets,
    _SerializerV1FaceDetectionCreateBodyAssets,
)


class V1FaceDetectionCreateBody(typing_extensions.TypedDict):
    """
    V1FaceDetectionCreateBody
    """

    assets: typing_extensions.Required[V1FaceDetectionCreateBodyAssets]
    """
    Provide the assets for face detection
    """

    confidence_score: typing_extensions.NotRequired[float]
    """
    Confidence threshold for filtering detected faces. 
    * Higher values (e.g., 0.9) include only faces detected with high certainty, reducing false positives. 
    * Lower values (e.g., 0.3) include more faces, but may increase the chance of incorrect detections.
    """


class _SerializerV1FaceDetectionCreateBody(pydantic.BaseModel):
    """
    Serializer for V1FaceDetectionCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1FaceDetectionCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    confidence_score: typing.Optional[float] = pydantic.Field(
        alias="confidence_score", default=None
    )
