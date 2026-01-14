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

    garment_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "dresses", "entire_outfit", "lower_body", "upper_body"
        ]
    ]
    """
    Type of garment to swap. If not provided, swaps the entire outfit. 
    * `upper_body` - for shirts/jackets 
    * `lower_body` - for pants/skirts 
    * `dresses` - for entire outfit (deprecated, use `entire_outfit` instead) 
    * `entire_outfit` - for entire outfit
    """

    person_file_path: typing_extensions.Required[str]
    """
    The image with the person. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """
