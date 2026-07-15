import typing

from magic_hour.types import models, params
from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)


class AiVideoEditorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.V1AiVideoEditorCreateBodyAssets,
        end_seconds: float,
        style: params.V1AiVideoEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        start_seconds: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiVideoEditorCreateResponse:
        """
        AI Video Editor

        **What this API does**

        Create the same Video Editor you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding video editor into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a video editor job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/video-editor).

        POST /v1/ai-video-editor

        Args:
            name: Give your video a custom name for easy identification.
            start_seconds: Start time of your clip (seconds). Must be ≥ 0.
            assets: Provide the assets for video editing.
            end_seconds: End time of your clip in seconds. Must be greater than `start_seconds`. Duration must be between 3 and 10 seconds.
            style: V1AiVideoEditorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_video_editor.create(
            assets={"video_file_path": "api-assets/id/1234.mp4"},
            end_seconds=5.0,
            style={"prompt": "Change the car color to blue"},
            name="My Video Editor video",
            start_seconds=0.0,
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "start_seconds": start_seconds,
                "assets": assets,
                "end_seconds": end_seconds,
                "style": style,
            },
            dump_with=params._SerializerV1AiVideoEditorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-video-editor",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVideoEditorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiVideoEditorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.V1AiVideoEditorCreateBodyAssets,
        end_seconds: float,
        style: params.V1AiVideoEditorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        start_seconds: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiVideoEditorCreateResponse:
        """
        AI Video Editor

        **What this API does**

        Create the same Video Editor you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding video editor into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a video editor job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/video-editor).

        POST /v1/ai-video-editor

        Args:
            name: Give your video a custom name for easy identification.
            start_seconds: Start time of your clip (seconds). Must be ≥ 0.
            assets: Provide the assets for video editing.
            end_seconds: End time of your clip in seconds. Must be greater than `start_seconds`. Duration must be between 3 and 10 seconds.
            style: V1AiVideoEditorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_video_editor.create(
            assets={"video_file_path": "api-assets/id/1234.mp4"},
            end_seconds=5.0,
            style={"prompt": "Change the car color to blue"},
            name="My Video Editor video",
            start_seconds=0.0,
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "start_seconds": start_seconds,
                "assets": assets,
                "end_seconds": end_seconds,
                "style": style,
            },
            dump_with=params._SerializerV1AiVideoEditorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-video-editor",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVideoEditorCreateResponse,
            request_options=request_options or default_request_options(),
        )
