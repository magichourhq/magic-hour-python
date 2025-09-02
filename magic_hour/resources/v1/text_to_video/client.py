import typing
import typing_extensions

from magic_hour.helpers.logger import get_sdk_logger
from magic_hour.resources.v1.video_projects.client import (
    AsyncVideoProjectsClient,
    VideoProjectsClient,
)
from magic_hour.types import models, params
from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)


logger = get_sdk_logger(__name__)


class TextToVideoClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        end_seconds: float,
        orientation: typing_extensions.Literal["landscape", "portrait", "square"],
        style: params.V1TextToVideoCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate text-to-video (alias for create with additional functionality).

        Create a Text To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Args:
            name: The name of video. This value is mainly used for your own identification of the video.
            resolution: Controls the output video resolution. Defaults to `720p` if not specified.
            end_seconds: The total duration of the output video in seconds.
            orientation: Determines the orientation of the output video
            style: V1TextToVideoCreateBodyStyle
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Text-to-Video API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.text_to_video.generate(
            end_seconds=5.0,
            orientation="landscape",
            style={"prompt": "a dog running through a meadow"},
            resolution="720p",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        create_response = self.create(
            end_seconds=end_seconds,
            orientation=orientation,
            style=style,
            name=name,
            resolution=resolution,
            request_options=request_options,
        )
        logger.info(f"Text-to-Video response: {create_response}")

        video_projects_client = VideoProjectsClient(base_client=self._base_client)
        response = video_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

        return response

    def create(
        self,
        *,
        end_seconds: float,
        orientation: typing_extensions.Literal["landscape", "portrait", "square"],
        style: params.V1TextToVideoCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1TextToVideoCreateResponse:
        """
        Text-to-Video

        Create a Text To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](https://magichour.ai/products/text-to-video).


        POST /v1/text-to-video

        Args:
            name: The name of video. This value is mainly used for your own identification of the video.
            resolution: Controls the output video resolution. Defaults to `720p` if not specified.

        480p and 720p are available on Creator, Pro, or Business tiers. However, 1080p require Pro or Business tier.

        **Options:**
        - `480p` - Supports only 5 or 10 second videos. Output: 24fps. Cost: 120 credits per 5 seconds.
        - `720p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 300 credits per 5 seconds.
        - `1080p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 600 credits per 5 seconds.
            end_seconds: The total duration of the output video in seconds.

        The value must be greater than or equal to 5 seconds and less than or equal to 60 seconds.

        Note: For 480p resolution, the value must be either 5 or 10.
            orientation: Determines the orientation of the output video
            style: V1TextToVideoCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.text_to_video.create(
            end_seconds=5.0,
            orientation="landscape",
            style={"prompt": "a dog running"},
            name="Text To Video video",
            resolution="720p",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "resolution": resolution,
                "end_seconds": end_seconds,
                "orientation": orientation,
                "style": style,
            },
            dump_with=params._SerializerV1TextToVideoCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/text-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1TextToVideoCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncTextToVideoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        end_seconds: float,
        orientation: typing_extensions.Literal["landscape", "portrait", "square"],
        style: params.V1TextToVideoCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate text-to-video (alias for create with additional functionality).

        Create a Text To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Args:
            name: The name of video. This value is mainly used for your own identification of the video.
            resolution: Controls the output video resolution. Defaults to `720p` if not specified.
            end_seconds: The total duration of the output video in seconds.
            orientation: Determines the orientation of the output video
            style: V1TextToVideoCreateBodyStyle
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Text-to-Video API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.text_to_video.generate(
            end_seconds=5.0,
            orientation="landscape",
            style={"prompt": "a dog running through a meadow"},
            resolution="720p",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        create_response = await self.create(
            end_seconds=end_seconds,
            orientation=orientation,
            style=style,
            name=name,
            resolution=resolution,
            request_options=request_options,
        )
        logger.info(f"Text-to-Video response: {create_response}")

        video_projects_client = AsyncVideoProjectsClient(base_client=self._base_client)
        response = await video_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

        return response

    async def create(
        self,
        *,
        end_seconds: float,
        orientation: typing_extensions.Literal["landscape", "portrait", "square"],
        style: params.V1TextToVideoCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1TextToVideoCreateResponse:
        """
        Text-to-Video

        Create a Text To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](https://magichour.ai/products/text-to-video).


        POST /v1/text-to-video

        Args:
            name: The name of video. This value is mainly used for your own identification of the video.
            resolution: Controls the output video resolution. Defaults to `720p` if not specified.

        480p and 720p are available on Creator, Pro, or Business tiers. However, 1080p require Pro or Business tier.

        **Options:**
        - `480p` - Supports only 5 or 10 second videos. Output: 24fps. Cost: 120 credits per 5 seconds.
        - `720p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 300 credits per 5 seconds.
        - `1080p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 600 credits per 5 seconds.
            end_seconds: The total duration of the output video in seconds.

        The value must be greater than or equal to 5 seconds and less than or equal to 60 seconds.

        Note: For 480p resolution, the value must be either 5 or 10.
            orientation: Determines the orientation of the output video
            style: V1TextToVideoCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.text_to_video.create(
            end_seconds=5.0,
            orientation="landscape",
            style={"prompt": "a dog running"},
            name="Text To Video video",
            resolution="720p",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "resolution": resolution,
                "end_seconds": end_seconds,
                "orientation": orientation,
                "style": style,
            },
            dump_with=params._SerializerV1TextToVideoCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/text-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1TextToVideoCreateResponse,
            request_options=request_options or default_request_options(),
        )
