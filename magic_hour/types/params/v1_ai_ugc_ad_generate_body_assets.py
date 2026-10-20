import typing_extensions


class V1AiUgcAdGenerateBodyAssets(typing_extensions.TypedDict, total=False):
    """Provide the prepared image for UGC ad generation."""

    image_file_path: typing_extensions.Required[str]
    """
    Prepared image to animate. Accepts a local image path or a direct URL.
    Paths beginning with `api-assets` are already uploaded and reused as is.
    """
