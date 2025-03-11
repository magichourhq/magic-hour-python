from typing import Any, Dict, Type, Union, Sequence, List
from urllib.parse import quote_plus

import httpx
from typing_extensions import TypedDict, Required, NotRequired
from pydantic import TypeAdapter, BaseModel

from .type_utils import NotGiven
from .query import QueryParams

"""
Request configuration and utility functions for handling HTTP requests.
This module provides type definitions and helper functions for building
and processing HTTP requests in a type-safe manner.
"""


class RequestConfig(TypedDict):
    """
    Configuration for HTTP requests.

    Defines all possible parameters that can be passed to an HTTP request,
    including required method and URL, as well as optional parameters like
    content, headers, authentication, etc.
    """

    method: Required[str]
    url: Required[httpx._types.URLTypes]
    content: NotRequired[httpx._types.RequestContent]
    data: NotRequired[httpx._types.RequestData]
    files: NotRequired[httpx._types.RequestFiles]
    json: NotRequired[Any]
    params: NotRequired[QueryParams]
    headers: NotRequired[Dict[str, str]]
    cookies: NotRequired[Dict[str, str]]
    auth: NotRequired[httpx._types.AuthTypes]
    follow_redirects: NotRequired[bool]
    timeout: NotRequired[httpx._types.TimeoutTypes]
    extensions: NotRequired[httpx._types.RequestExtensions]


class RequestOptions(TypedDict):
    """
    Additional options for customizing request behavior.

    Provides configuration for timeouts and additional headers/parameters
    that should be included with requests.

    Attributes:
        timeout: Number of seconds to await an API call before timing out
        additional_headers: Extra headers to include in the request
        additional_params: Extra query parameters to include in the request
    """

    timeout: NotRequired[int]
    additional_headers: NotRequired[Dict[str, str]]
    additional_params: NotRequired[QueryParams]


def default_request_options() -> RequestOptions:
    """
    Provides default request options.

    Returns an empty dictionary as the base configuration, allowing defaults
    to be handled by the underlying HTTP client.
    """
    return {}


def model_dump(item: Any) -> Any:
    """
    Recursively converts Pydantic models to dictionaries.

    Handles nested structures including lists and individual models,
    preserving alias information and excluding unset values.
    """
    if isinstance(item, list):
        return [model_dump(i) for i in item]
    if isinstance(item, BaseModel):
        return item.model_dump(exclude_unset=True, by_alias=True)
    else:
        return item


def to_encodable(
    *, item: Any, dump_with: Union[Type, Union[Type, Any], List[Type]]
) -> Any:
    """
    Validates and converts an item to an encodable format using a specified type.
    Uses Pydantic's TypeAdapter for validation and converts the result
    to a format suitable for encoding in requests.
    """
    filtered_item = filter_not_given(item)
    adapter: TypeAdapter = TypeAdapter(dump_with)
    validated_item = adapter.validate_python(filtered_item)
    return model_dump(validated_item)


def to_content(*, file: httpx._types.FileTypes) -> httpx._types.RequestContent:
    """
    Converts the various ways files can be provided to something that is accepted by
    the httpx.request content kwarg
    """
    if isinstance(file, tuple):
        file_content: httpx._types.FileContent = file[1]
    else:
        file_content = file

    if hasattr(file_content, "read") and callable(file_content.read):
        return file_content.read()
    else:
        return file_content


def encode_param(
    value: Any, explode: bool
) -> Union[httpx._types.PrimitiveData, Sequence[httpx._types.PrimitiveData]]:
    """
    Encodes parameter values for use in URLs.

    Handles both simple values and collections, with special handling for
    unexploded collections (combining them with commas) versus exploded ones.

    Args:
        explode: Whether to explode collections into separate parameters
    """
    if isinstance(value, (list, dict)) and not explode:
        return quote_plus(",".join(map(str, value)))
    else:
        return value


def filter_not_given(value: Any) -> Any:
    """Helper function to recursively filter out NotGiven values"""
    if isinstance(value, NotGiven):
        return None  # This will trigger filtering at the container level
    elif isinstance(value, dict):
        return {
            k: filter_not_given(v)
            for k, v in value.items()
            if not isinstance(v, NotGiven)
        }
    elif isinstance(value, (list, tuple)):
        return type(value)(
            filter_not_given(item) for item in value if not isinstance(item, NotGiven)
        )
    return value


def _get_default_for_type(value_type: Any) -> Any:
    """Helper to provide appropriate default values for required fields"""
    if value_type is dict or isinstance(value_type, dict):
        return {}
    elif value_type is list or isinstance(value_type, list):
        return []
    return None
