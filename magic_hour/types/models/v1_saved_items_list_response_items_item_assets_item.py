import pydantic
import typing_extensions


class V1SavedItemsListResponseItemsItemAssetsItem(pydantic.BaseModel):
    """
    V1SavedItemsListResponseItemsItemAssetsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    file_path: str = pydantic.Field(
        alias="file_path",
    )
    """
    Durable asset path. Pass it to a compatible API asset field without uploading it again.
    """
    is_primary: bool = pydantic.Field(
        alias="is_primary",
    )
    """
    Whether this asset is the saved item's primary asset.
    """
    media_kind: typing_extensions.Literal["AUDIO", "IMAGE", "VIDEO"] = pydantic.Field(
        alias="media_kind",
    )
    """
    Media type of the asset.
    """
    url: str = pydantic.Field(
        alias="url",
    )
    """
    Signed URL for previewing or downloading the asset. Expires after 24 hours.
    """
    url_expires_at: str = pydantic.Field(
        alias="url_expires_at",
    )
    """
    When the signed URL expires. The saved asset and file_path do not expire.
    """
