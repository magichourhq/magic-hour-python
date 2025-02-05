from typing import (
    Any,
    List,
    TypeVar,
    Dict,
    Optional,
    Type,
    Union,
    cast,
)
from typing_extensions import TypeGuard

import httpx
from pydantic import BaseModel

from .api_error import ApiError
from .auth import AuthProvider
from .request import RequestConfig, RequestOptions, default_request_options, QueryParams
from .response import from_encodable, AsyncStreamResponse, StreamResponse
from .utils import get_response_type, filter_binary_response
from .binary_response import BinaryResponse

NoneType = type(None)
T = TypeVar(
    "T",
    bound=Union[object, None, str, "BaseModel", List[Any], Dict[str, Any], Any],
)


class BaseClient:
    """Base client class providing core HTTP client functionality.

    Handles authentication, request building, and response processing for HTTP API clients.
    Serves as the foundation for both synchronous and asynchronous client implementations.

    Attributes:
        _base_url: Base URL for the API endpoint
        _auths: Dictionary mapping auth provider IDs to AuthProvider instances
    """

    def __init__(
        self,
        *,
        base_url: str,
    ):
        """Initialize the base client.

        Args:
            base_url: Base URL for the API endpoint
        """
        self._base_url = base_url
        self._auths: Dict[str, AuthProvider] = {}

    def register_auth(self, auth_id: str, provider: AuthProvider):
        """Register an authentication provider.

        Args:
            auth_id: Unique identifier for the auth provider
            provider: AuthProvider instance to handle authentication
        """
        self._auths[auth_id] = provider

    def default_headers(self) -> Dict[str, str]:
        """Get default headers for requests.

        Returns:
            Dictionary of default headers
        """
        headers: Dict[str, str] = {
            "x-sideko-sdk-language": "Python",
        }
        return headers

    def get_base_url(self) -> str:
        """Get the base URL for the API endpoint.

        Returns:
            Base URL string
        """
        return self._base_url

    def build_url(self, path: str) -> str:
        """Build a complete URL by combining base URL and path.

        Args:
            path: API endpoint path

        Returns:
            Complete URL string
        """
        base = self._base_url
        if base.endswith("/"):
            base = base[:-1]
        if path.startswith("/"):
            path = path[1:]

        return f"{base}/{path}"

    def _cast_to_raw_response(
        self, res: httpx.Response, cast_to: Union[Type[T], Any]
    ) -> TypeGuard[T]:
        """Determines if the provided cast_to is an httpx.Response"""
        try:
            return issubclass(cast_to, httpx.Response)
        except TypeError:
            return False

    def _apply_auth(
        self, *, cfg: RequestConfig, auth_names: List[str]
    ) -> RequestConfig:
        """Apply authentication to the request configuration.

        Args:
            cfg: Request configuration to modify
            auth_names: List of auth provider IDs to apply

        Returns:
            Modified request configuration
        """
        for auth_name in auth_names:
            auth_provider = self._auths.get(auth_name)
            if auth_provider is not None:
                cfg = auth_provider.add_to_request(cfg)

        return cfg

    def _apply_headers(
        self,
        *,
        cfg: RequestConfig,
        opts: RequestOptions,
        content_type: Optional[str] = None,
        explicit_headers: Optional[Dict[str, str]] = None,
    ) -> RequestConfig:
        """Apply headers to the request configuration.

        Args:
            cfg: Request configuration to modify
            opts: Request options containing additional headers
            content_type: Optional content type header
            explicit_headers: Optional explicitly specified headers

        Returns:
            Modified request configuration
        """
        headers = cfg.get("headers", {})
        headers.update(self.default_headers())

        if content_type is not None:
            headers["content-type"] = content_type

        if explicit_headers is not None:
            headers.update(explicit_headers)

        additional_headers = opts.get("additional_headers", None)
        if additional_headers is not None:
            headers.update(additional_headers)

        if len(headers) > 0:
            cfg["headers"] = headers

        return cfg

    def _apply_query_params(
        self,
        *,
        cfg: RequestConfig,
        opts: RequestOptions,
        query_params: Optional[QueryParams] = None,
    ) -> RequestConfig:
        """Apply query parameters to the request configuration.

        Args:
            cfg: Request configuration to modify
            opts: Request options containing additional parameters
            query_params: Optional query parameters to add

        Returns:
            Modified request configuration
        """
        params = cfg.get("params", {})

        if query_params is not None:
            params.update(query_params)

        additional_params = opts.get("additional_params", None)
        if additional_params is not None:
            params.update(additional_params)

        if len(params) > 0:
            cfg["params"] = params

        return cfg

    def _apply_timeout(
        self,
        *,
        cfg: RequestConfig,
        opts: RequestOptions,
    ) -> RequestConfig:
        """Apply timeout settings to the request configuration.

        Args:
            cfg: Request configuration to modify
            opts: Request options containing timeout settings

        Returns:
            Modified request configuration
        """
        timeout = opts.get("timeout", None)

        if timeout is not None:
            cfg["timeout"] = timeout

        return cfg

    def _apply_body(
        self,
        *,
        cfg: RequestConfig,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        content: Optional[httpx._types.RequestContent] = None,
    ) -> RequestConfig:
        """Apply request body content to the request configuration.

        Args:
            cfg: Request configuration to modify
            data: Optional form data
            files: Optional files to upload
            json: Optional JSON data
            content: Optional raw content

        Returns:
            Modified request configuration
        """
        if data is not None:
            cfg["data"] = data

        if files is not None:
            cfg["files"] = files

        if json is not None:
            cfg["json"] = json

        if content is not None:
            cfg["content"] = content

        return cfg

    def build_request(
        self,
        *,
        method: str,
        path: str,
        auth_names: Optional[List[str]] = None,
        query_params: Optional[QueryParams] = None,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        content_type: Optional[str] = None,
        content: Optional[httpx._types.RequestContent] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> RequestConfig:
        """Build a complete request configuration.

        Args:
            method: HTTP method
            path: API endpoint path
            auth_names: List of auth provider IDs
            query_params: Query parameters
            headers: Request headers
            data: Form data
            files: Files to upload
            json: JSON data
            content_type: Content type header
            content: Raw content
            request_options: Additional request options

        Returns:
            Complete request configuration
        """
        opts = request_options or default_request_options()
        req_cfg: RequestConfig = {"method": method, "url": self.build_url(path)}
        req_cfg = self._apply_auth(cfg=req_cfg, auth_names=auth_names or [])
        req_cfg = self._apply_headers(
            cfg=req_cfg, opts=opts, content_type=content_type, explicit_headers=headers
        )
        req_cfg = self._apply_query_params(
            cfg=req_cfg, opts=opts, query_params=query_params
        )
        req_cfg = self._apply_body(
            cfg=req_cfg, data=data, files=files, json=json, content=content
        )
        req_cfg = self._apply_timeout(cfg=req_cfg, opts=opts)

        return req_cfg

    def process_response(
        self,
        *,
        response=httpx.Response,
        cast_to: Union[Type[T], Any],
    ) -> T:
        """Process an HTTP response and convert it to the desired type.

        Args:
            response: HTTP response to process
            cast_to: Type to cast the response data to

        Returns:
            Processed response data of the specified type

        Raises:
            ApiError: If the response indicates an error
        """

        if response.status_code == 204 or cast_to == NoneType:
            return cast(T, None)
        elif cast_to == BinaryResponse:
            return cast(
                T,
                BinaryResponse(content=response.content, headers=response.headers),
            )

        response_type = get_response_type(response.headers)

        if response_type == "json":
            if cast_to is type(Any):
                return response.json()
            return from_encodable(
                data=response.json(), load_with=filter_binary_response(cast_to=cast_to)
            )
        elif response_type == "text":
            return cast(T, response.text)
        else:
            return cast(
                T,
                BinaryResponse(content=response.content, headers=response.headers),
            )


class SyncBaseClient(BaseClient):
    """Synchronous HTTP client implementation.

    Provides synchronous HTTP request capabilities building on the base client functionality.
    """

    def __init__(
        self,
        *,
        base_url: str,
        httpx_client: httpx.Client,
    ):
        """Initialize the synchronous client.

        Args:
            base_url: Base URL for the API endpoint
            httpx_client: Synchronous HTTPX client instance
        """
        super().__init__(base_url=base_url)
        self.httpx_client = httpx_client

    def request(
        self,
        *,
        method: str,
        path: str,
        cast_to: Union[Type[T], Any],
        auth_names: Optional[List[str]] = None,
        query_params: Optional[QueryParams] = None,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        content_type: Optional[str] = None,
        content: Optional[httpx._types.RequestContent] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> T:
        """Make a synchronous HTTP request.

        Args:
            method: HTTP method
            path: API endpoint path
            cast_to: Type to cast the response to
            auth_names: List of auth provider IDs
            query_params: Query parameters
            headers: Request headers
            data: Form data
            files: Files to upload
            json: JSON data
            content_type: Content type header
            content: Raw content
            request_options: Additional request options

        Returns:
            Response data of the specified type

        Raises:
            ApiError: If the request fails
        """
        req_cfg = self.build_request(
            method=method,
            path=path,
            auth_names=auth_names,
            query_params=query_params,
            headers=headers,
            data=data,
            files=files,
            json=json,
            content_type=content_type,
            content=content,
            request_options=request_options,
        )
        response = self.httpx_client.request(**req_cfg)

        if not response.is_success:
            raise ApiError(response=response)

        if self._cast_to_raw_response(res=response, cast_to=cast_to):
            return response

        return self.process_response(response=response, cast_to=cast_to)

    def stream_request(
        self,
        *,
        method: str,
        path: str,
        cast_to: Union[Type[T], Any],
        auth_names: Optional[List[str]] = None,
        query_params: Optional[QueryParams] = None,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        content_type: Optional[str] = None,
        content: Optional[httpx._types.RequestContent] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> StreamResponse[T]:
        """Make a streaming synchronous HTTP request.

        Args:
            method: HTTP method
            path: API endpoint path
            cast_to: Type to cast the response to
            auth_names: List of auth provider IDs
            query_params: Query parameters
            headers: Request headers
            data: Form data
            files: Files to upload
            json: JSON data
            content_type: Content type header
            content: Raw content
            request_options: Additional request options

        Returns:
            StreamResponse containing the streaming response

        Raises:
            ApiError: If the request fails
        """
        req_cfg = self.build_request(
            method=method,
            path=path,
            auth_names=auth_names,
            query_params=query_params,
            headers=headers,
            data=data,
            files=files,
            json=json,
            content_type=content_type,
            content=content,
            request_options=request_options,
        )
        context = self.httpx_client.stream(**req_cfg)
        response = context.__enter__()
        return StreamResponse(response, context, cast_to)


class AsyncBaseClient(BaseClient):
    """Asynchronous HTTP client implementation.

    Provides asynchronous HTTP request capabilities building on the base client functionality.
    """

    def __init__(
        self,
        *,
        base_url: str,
        httpx_client: httpx.AsyncClient,
    ):
        """Initialize the asynchronous client.

        Args:
            base_url: Base URL for the API endpoint
            httpx_client: Asynchronous HTTPX client instance
        """
        super().__init__(base_url=base_url)
        self.httpx_client = httpx_client

    async def request(
        self,
        *,
        method: str,
        path: str,
        cast_to: Union[Type[T], Any],
        auth_names: Optional[List[str]] = None,
        query_params: Optional[QueryParams] = None,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        content_type: Optional[str] = None,
        content: Optional[httpx._types.RequestContent] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> T:
        """Make an asynchronous HTTP request.

        Args:
            method: HTTP method
            path: API endpoint path
            cast_to: Type to cast the response to
            auth_names: List of auth provider IDs
            query_params: Query parameters
            headers: Request headers
            data: Form data
            files: Files to upload
            json: JSON data
            content_type: Content type header
            content: Raw content
            request_options: Additional request options

        Returns:
            Response data of the specified type

        Raises:
            ApiError: If the request fails
        """
        req_cfg = self.build_request(
            method=method,
            path=path,
            auth_names=auth_names,
            query_params=query_params,
            headers=headers,
            data=data,
            files=files,
            json=json,
            content_type=content_type,
            content=content,
            request_options=request_options,
        )
        response = await self.httpx_client.request(**req_cfg)

        if not response.is_success:
            raise ApiError(response=response)

        if self._cast_to_raw_response(res=response, cast_to=cast_to):
            return response

        return self.process_response(response=response, cast_to=cast_to)

    async def stream_request(
        self,
        *,
        method: str,
        path: str,
        cast_to: Union[Type[T], Any],
        auth_names: Optional[List[str]] = None,
        query_params: Optional[QueryParams] = None,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        content_type: Optional[str] = None,
        content: Optional[httpx._types.RequestContent] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncStreamResponse[T]:
        """Make a streaming asynchronous HTTP request.

        Args:
            method: HTTP method
            path: API endpoint path
            cast_to: Type to cast the response to
            auth_names: List of auth provider IDs
            query_params: Query parameters
            headers: Request headers
            data: Form data
            files: Files to upload
            json: JSON data
            content_type: Content type header
            content: Raw content
            request_options: Additional request options

        Returns:
            AsyncStreamResponse containing the streaming response

        Raises:
            ApiError: If the request fails
        """
        req_cfg = self.build_request(
            method=method,
            path=path,
            auth_names=auth_names,
            query_params=query_params,
            headers=headers,
            data=data,
            files=files,
            json=json,
            content_type=content_type,
            content=content,
            request_options=request_options,
        )
        context = self.httpx_client.stream(**req_cfg)
        response = await context.__aenter__()
        return AsyncStreamResponse(response, context, cast_to)
