import json

from typing import Any, Dict, Union
from typing_extensions import Literal, Sequence

import httpx


# Type alias for query parameters that can handle both primitive data and sequences
QueryParams = Dict[
    str, Union[httpx._types.PrimitiveData, Sequence[httpx._types.PrimitiveData]]
]
QueryParamStyle = Literal["form", "spaceDelimited", "pipeDelimited", "deepObject"]


def encode_query_param(
    params: QueryParams,
    name: str,
    value: Any,
    style: QueryParamStyle = "form",
    explode: bool = True,
):
    if style == "form":
        _encode_form(params, name, value, explode)
    elif style == "spaceDelimited":
        _encode_spaced_delimited(params, name, value, explode)
    elif style == "pipeDelimited":
        _encode_pipe_delimited(params, name, value, explode)
    elif style == "deepObject":
        _encode_deep_object(params, name, value, explode)
    else:
        raise NotImplementedError(f"query param style '{style}' not implemented")


def _query_str(val: Any) -> str:
    """jsonify value without wrapping quotes for strings"""
    if isinstance(val, str):
        return val
    return json.dumps(val)


def _encode_form(params: QueryParams, name: str, value: Any, explode: bool):
    """
    Encodes query params in the `form` style as defined by OpenAPI with both explode and non-explode
    variants.
    """
    if isinstance(value, list) and not explode:
        # non-explode form lists should be encoded like /users?id=3,4,5
        params[name] = ",".join(map(_query_str, value))
    elif isinstance(value, dict):
        if explode:
            # explode form objects should be encoded like /users?key0=val0&key1=val1
            # the input param name will be omitted
            for k, v in value.items():
                params[k] = _query_str(v)
        else:
            # non-explode form objects should be encoded like /users?id=key0,val0,key1,val1
            encoded_chunks = []
            for k, v in value.items():
                encoded_chunks.extend([str(k), _query_str(v)])
            params[name] = ",".join(encoded_chunks)
    else:
        params[name] = value


def _encode_spaced_delimited(params: QueryParams, name: str, value: Any, explode: bool):
    """
    Encodes query params in the `spaceDelimited` style as defined by OpenAPI with both explode and non-explode
    variants.
    """
    if isinstance(value, list) and not explode:
        # non-explode spaceDelimited lists should be encoded like /users?id=3%204%205
        params[name] = " ".join(map(_query_str, value))
    else:
        # according to the docs, spaceDelimited + explode=false only effects lists,
        # all other encodings are marked as n/a or are the same as `form` style
        # fall back on form style as it is the default for query params
        _encode_form(params, name, value, explode)


def _encode_pipe_delimited(params: QueryParams, name: str, value: Any, explode: bool):
    """
    Encodes query params in the `pipeDelimited` style as defined by OpenAPI with both explode and non-explode
    variants.
    """
    if isinstance(value, list) and not explode:
        # non-explode pipeDelimited lists should be encoded like /users?id=3|4|5
        params[name] = "|".join(map(_query_str, value))
    else:
        # according to the docs, pipeDelimited + explode=false only effects lists,
        # all other encodings are marked as n/a or are the same as `form` style
        # fall back on form style as it is the default for query params
        _encode_form(params, name, value, explode)


def _encode_deep_object(params: QueryParams, name: str, value: Any, explode: bool):
    """
    Encodes query params in the `deepObject` style as defined by with both explode and non-explode
    variants.
    """
    if isinstance(value, (dict, list)):
        _encode_deep_object_key(params, name, value)
    else:
        # according to the docs, deepObject style only applies to
        # object encodes, encodings for primitives are listed as n/a,
        # fall back on form style as it is the default for query params
        _encode_form(params, name, value, explode)


def _encode_deep_object_key(params: QueryParams, key: str, value: Any):
    if isinstance(value, dict):
        for k, v in value.items():
            _encode_deep_object_key(params, f"{key}[{k}]", v)
    elif isinstance(value, list):
        for i, v in enumerate(value):
            _encode_deep_object_key(params, f"{key}[{i}]", v)
    else:
        params[key] = _query_str(value)
