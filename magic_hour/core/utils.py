import typing
import re
from typing_extensions import Literal

import httpx

from .binary_response import BinaryResponse


def remove_none_from_dict(
    original: typing.Dict[str, typing.Optional[typing.Any]],
) -> typing.Dict[str, typing.Any]:
    new: typing.Dict[str, typing.Any] = {}
    for key, value in original.items():
        if value is not None:
            new[key] = value
    return new


def get_response_type(headers: httpx.Headers) -> Literal["json", "text", "binary"]:
    """Check response type based on content type"""
    content_type = headers.get("content-type")

    if re.search("^application/(.+[+])?json", content_type):
        return "json"
    elif re.search("^text/(.+)", content_type):
        return "text"
    else:
        return "binary"


def is_union_type(type_hint: typing.Any) -> bool:
    """Check if a type hint is a Union type."""
    return hasattr(type_hint, "__origin__") and type_hint.__origin__ is typing.Union


def filter_binary_response(cast_to: typing.Type) -> typing.Type:
    """
    Filters out BinaryResponse from a Union type.
    If cast_to is not a Union, returns it unchanged.
    """
    if not is_union_type(cast_to):
        return cast_to

    types = typing.get_args(cast_to)
    filtered = tuple(t for t in types if t != BinaryResponse)

    # If everything was filtered out, return original type
    if not filtered:
        return cast_to
    # If only one type remains, return it directly
    if len(filtered) == 1:
        return typing.cast(typing.Type, filtered[0])
    # Otherwise return new Union with filtered types
    return typing.cast(typing.Type, typing.Union[filtered])  # type: ignore
