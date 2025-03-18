import typing

from magic_hour.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from magic_hour.types import models, params


class AiClothesChangerClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.PostV1AiClothesChangerBodyAssets,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1AiClothesChangerResponse:
        """
        AI Clothes Changer

        Change outfits in photos in seconds with just a photo reference. Each photo costs 25 frames.

        POST /v1/ai-clothes-changer

        Args:
            name: The name of image
            assets: Provide the assets for clothes changer
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_clothes_changer.create(
            assets={
                "garment_file_path": "api-assets/id/outfit.png",
                "garment_type": "dresses",
                "person_file_path": "api-assets/id/model.png",
            },
            name="Clothes Changer image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets},
            dump_with=params._SerializerPostV1AiClothesChangerBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-clothes-changer",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1AiClothesChangerResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiClothesChangerClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.PostV1AiClothesChangerBodyAssets,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1AiClothesChangerResponse:
        """
        AI Clothes Changer

        Change outfits in photos in seconds with just a photo reference. Each photo costs 25 frames.

        POST /v1/ai-clothes-changer

        Args:
            name: The name of image
            assets: Provide the assets for clothes changer
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_clothes_changer.create(
            assets={
                "garment_file_path": "api-assets/id/outfit.png",
                "garment_type": "dresses",
                "person_file_path": "api-assets/id/model.png",
            },
            name="Clothes Changer image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets},
            dump_with=params._SerializerPostV1AiClothesChangerBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-clothes-changer",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1AiClothesChangerResponse,
            request_options=request_options or default_request_options(),
        )
