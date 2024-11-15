"""
Generated by Sideko (sideko.dev)
"""

import abc
import typing

from pydantic import BaseModel

from .request import RequestConfig


class AuthProvider(abc.ABC):
    @abc.abstractmethod
    def add_to_request(self, cfg: RequestConfig) -> RequestConfig:
        """Adds relevant auth to request kwargs"""


class AuthBasic(BaseModel, AuthProvider):
    username: typing.Optional[str]
    password: typing.Optional[str]

    def add_to_request(self, cfg: RequestConfig) -> RequestConfig:
        if self.username is not None and self.password is not None:
            cfg["auth"] = (self.username, self.password)

        return cfg


class AuthBearer(BaseModel, AuthProvider):
    val: typing.Optional[str]

    def add_to_request(self, cfg: RequestConfig) -> RequestConfig:
        if self.val is not None:
            # Add bearer header auth val
            headers = cfg.get("headers", dict())
            headers["Authorization"] = f"Bearer {self.val}"
            cfg["headers"] = headers

        return cfg


class AuthKeyQuery(BaseModel, AuthProvider):
    query_name: str
    val: typing.Optional[str]

    def add_to_request(self, cfg: RequestConfig) -> RequestConfig:
        if self.val is not None:
            # Add query auth value
            params = cfg.get("params", dict())
            params[self.query_name] = self.val
            cfg["params"] = params

        return cfg


class AuthKeyHeader(BaseModel, AuthProvider):
    header_name: str
    val: typing.Optional[str]

    def add_to_request(self, cfg: RequestConfig) -> RequestConfig:
        if self.val is not None:
            # Add header auth val
            headers = cfg.get("headers", {})
            headers[self.header_name] = self.val
            cfg["headers"] = headers

        return cfg


class AuthKeyCookie(BaseModel, AuthProvider):
    cookie_name: str
    val: typing.Optional[str]

    def add_to_request(self, cfg: RequestConfig) -> RequestConfig:
        if self.val is not None:
            # Add cookie auth val
            cookies = cfg.get("cookies", dict())
            cookies[self.cookie_name] = self.val
            cfg["cookies"] = cookies

        return cfg
