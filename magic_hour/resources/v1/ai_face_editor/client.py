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


class AiFaceEditorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.V1AiFaceEditorCreateBodyAssets,
        style: params.V1AiFaceEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiFaceEditorCreateResponse:
        """
        AI Face Editor

        Edit facial features of an image using AI. Each edit costs 1 frame. The height/width of the output image depends on your subscription. Please refer to our [pricing](/pricing) page for more details

        POST /v1/ai-face-editor

        Args:
            name: The name of image
            assets: Provide the assets for face editor
            style: Face editing parameters
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_face_editor.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            style={
                "enhance_face": False,
                "eye_gaze_horizontal": 0.0,
                "eye_gaze_vertical": 0.0,
                "eye_open_ratio": 0.0,
                "eyebrow_direction": 0.0,
                "head_pitch": 0.0,
                "head_roll": 0.0,
                "head_yaw": 0.0,
                "lip_open_ratio": 0.0,
                "mouth_grim": 0.0,
                "mouth_position_horizontal": 0.0,
                "mouth_position_vertical": 0.0,
                "mouth_pout": 0.0,
                "mouth_purse": 0.0,
                "mouth_smile": 0.0,
            },
            name="Face Editor image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets, "style": style},
            dump_with=params._SerializerV1AiFaceEditorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-face-editor",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiFaceEditorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiFaceEditorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.V1AiFaceEditorCreateBodyAssets,
        style: params.V1AiFaceEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiFaceEditorCreateResponse:
        """
        AI Face Editor

        Edit facial features of an image using AI. Each edit costs 1 frame. The height/width of the output image depends on your subscription. Please refer to our [pricing](/pricing) page for more details

        POST /v1/ai-face-editor

        Args:
            name: The name of image
            assets: Provide the assets for face editor
            style: Face editing parameters
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_face_editor.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            style={
                "enhance_face": False,
                "eye_gaze_horizontal": 0.0,
                "eye_gaze_vertical": 0.0,
                "eye_open_ratio": 0.0,
                "eyebrow_direction": 0.0,
                "head_pitch": 0.0,
                "head_roll": 0.0,
                "head_yaw": 0.0,
                "lip_open_ratio": 0.0,
                "mouth_grim": 0.0,
                "mouth_position_horizontal": 0.0,
                "mouth_position_vertical": 0.0,
                "mouth_pout": 0.0,
                "mouth_purse": 0.0,
                "mouth_smile": 0.0,
            },
            name="Face Editor image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets, "style": style},
            dump_with=params._SerializerV1AiFaceEditorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-face-editor",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiFaceEditorCreateResponse,
            request_options=request_options or default_request_options(),
        )
