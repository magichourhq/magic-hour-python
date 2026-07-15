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


class CharacterReplaceClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.V1CharacterReplaceCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1CharacterReplaceCreateResponse:
        """
        Character Replace

        **What this API does**

        Create the same Character Replace you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding character replace into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a character replace job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/character-replace).

        POST /v1/character-replace

        Args:
            data: V1CharacterReplaceCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.character_replace.create()
        ```
        """
        _json = (
            to_encodable(
                item=data, dump_with=params._SerializerV1CharacterReplaceCreateBody
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/character-replace",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1CharacterReplaceCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncCharacterReplaceClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.V1CharacterReplaceCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1CharacterReplaceCreateResponse:
        """
        Character Replace

        **What this API does**

        Create the same Character Replace you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding character replace into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a character replace job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/character-replace).

        POST /v1/character-replace

        Args:
            data: V1CharacterReplaceCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.character_replace.create()
        ```
        """
        _json = (
            to_encodable(
                item=data, dump_with=params._SerializerV1CharacterReplaceCreateBody
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/character-replace",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1CharacterReplaceCreateResponse,
            request_options=request_options or default_request_options(),
        )
