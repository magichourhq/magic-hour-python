import pydantic


class V1FaceDetectionGetResponseFacesItem(pydantic.BaseModel):
    """
    V1FaceDetectionGetResponseFacesItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    path: str = pydantic.Field(
        alias="path",
    )
    """
    The path to the face image. This should be used in face swap photo/video API calls as `.assets.face_mappings.original_face`
    """
    url: str = pydantic.Field(
        alias="url",
    )
    """
    The url to the face image. This is used to render the image in your applications.
    """
