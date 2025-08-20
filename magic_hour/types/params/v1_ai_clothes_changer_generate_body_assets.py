import pydantic
import typing_extensions


class V1AiClothesChangerGenerateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for clothes changer
    """

    garment_file_path: typing_extensions.Required[str]
    """
    The image of the outfit. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """

    garment_type: typing_extensions.Required[
        typing_extensions.Literal["dresses", "lower_body", "upper_body"]
    ]
    """
    The type of the outfit.
    """

    person_file_path: typing_extensions.Required[str]
    """
    The image with the person. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """
