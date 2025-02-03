import pydantic


class PostV1FilesUploadUrlsResponseItemsItem(pydantic.BaseModel):
    """
    PostV1FilesUploadUrlsResponseItemsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    expires_at: str = pydantic.Field(
        alias="expires_at",
    )
    """
    when the upload url expires, and will need to request a new one.
    """
    file_path: str = pydantic.Field(
        alias="file_path",
    )
    """
    this value is used in APIs that needs assets, such as image_file_path, video_file_path, and audio_file_path
    """
    upload_url: str = pydantic.Field(
        alias="upload_url",
    )
    """
    Used to upload the file to storage, send a PUT request with the file as data to upload.
    """
