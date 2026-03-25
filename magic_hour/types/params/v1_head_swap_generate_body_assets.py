import typing_extensions


class V1HeadSwapGenerateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the body and head images for head swap
    """

    body_file_path: typing_extensions.Required[str]
    """
    Image that receives the swapped head. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """

    head_file_path: typing_extensions.Required[str]
    """
    Image of the head to place on the body. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """
