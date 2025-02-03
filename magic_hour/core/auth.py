import abc
import datetime
from typing import Any, Dict, TypedDict, Optional, List, Tuple, Literal

import jsonpointer  # type: ignore
import httpx
from pydantic import BaseModel
from .request import RequestConfig


class AuthProvider(abc.ABC, BaseModel):
    """
    Abstract base class defining the interface for authentication providers.

    Each concrete implementation handles a specific authentication method
    and modifies the request configuration accordingly.
    """

    @abc.abstractmethod
    def add_to_request(self, cfg: RequestConfig) -> RequestConfig:
        """
        Adds authentication details to the request configuration.

        Args:
            cfg: The request configuration to modify

        Returns:
            The modified request configuration with authentication details added
        """

    @abc.abstractmethod
    def set_value(self, val: Optional[str]) -> None:
        """
        Generic method to set an auth value.

        Args:
            val: Authentication value to set
        """


class AuthBasic(AuthProvider):
    """
    Implements HTTP Basic Authentication.

    Adds username and password credentials to the request using the standard
    HTTP Basic Authentication scheme.
    """

    username: Optional[str]
    password: Optional[str]

    def add_to_request(self, cfg: RequestConfig) -> RequestConfig:
        """
        Adds Basic Authentication credentials to the request configuration.

        Only modifies the configuration if both username and password are provided.
        """
        if self.username is not None and self.password is not None:
            cfg["auth"] = (self.username, self.password)
        return cfg

    def set_value(self, val: Optional[str]) -> None:
        """
        Sets value as the username
        """
        self.username = val


class AuthBearer(AuthProvider):
    """
    Implements Bearer token authentication.

    Adds a Bearer token to the request's Authorization header following
    the OAuth 2.0 Bearer Token scheme.
    """

    val: Optional[str]

    def add_to_request(self, cfg: RequestConfig) -> RequestConfig:
        """
        Adds Bearer token to the Authorization header.

        Only modifies the configuration if a token value is provided.
        """
        if self.val is not None:
            headers = cfg.get("headers", dict())
            headers["Authorization"] = f"Bearer {self.val}"
            cfg["headers"] = headers
        return cfg

    def set_value(self, val: Optional[str]) -> None:
        """
        Sets value as the bearer token
        """
        self.val = val


class AuthKeyQuery(AuthProvider):
    """
    Implements query parameter-based authentication.

    Adds an authentication token or key as a query parameter with a
    configurable parameter name.
    """

    query_name: str
    val: Optional[str]

    def add_to_request(self, cfg: RequestConfig) -> RequestConfig:
        """
        Adds authentication value as a query parameter.

        Only modifies the configuration if a value is provided.
        """
        if self.val is not None:
            params = cfg.get("params", dict())
            params[self.query_name] = self.val
            cfg["params"] = params
        return cfg

    def set_value(self, val: Optional[str]) -> None:
        """
        Sets value as the key
        """
        self.val = val


class AuthKeyHeader(AuthProvider):
    """
    Implements header-based authentication.

    Adds an authentication token or key as a custom header with a
    configurable header name.
    """

    header_name: str
    val: Optional[str]

    def add_to_request(self, cfg: RequestConfig) -> RequestConfig:
        """
        Adds authentication value as a custom header.

        Only modifies the configuration if a value is provided.
        """
        if self.val is not None:
            headers = cfg.get("headers", {})
            headers[self.header_name] = self.val
            cfg["headers"] = headers
        return cfg

    def set_value(self, val: Optional[str]) -> None:
        """
        Sets value as the key
        """
        self.val = val


class AuthKeyCookie(AuthProvider):
    """
    Implements cookie-based authentication.

    Adds an authentication token or key as a cookie with a
    configurable cookie name.
    """

    cookie_name: str
    val: Optional[str]

    def add_to_request(self, cfg: RequestConfig) -> RequestConfig:
        """
        Adds authentication value as a cookie.

        Only modifies the configuration if a value is provided.
        """
        if self.val is not None:
            cookies = cfg.get("cookies", dict())
            cookies[self.cookie_name] = self.val
            cfg["cookies"] = cookies
        return cfg

    def set_value(self, val: Optional[str]) -> None:
        """
        Sets value as the key
        """
        self.val = val


class OAuth2PasswordForm(TypedDict, total=True):
    """
    OAuth2 authentication form for a password flow

    Details:
    https://datatracker.ietf.org/doc/html/rfc6749#section-4.3
    """

    username: str
    password: str
    client_id: Optional[str]
    client_secret: Optional[str]
    grant_type: Optional[str]
    scope: Optional[List[str]]


class OAuth2ClientCredentialsForm(TypedDict, total=True):
    """
    OAuth2 authentication form for a client credentials flow

    Details:
    https://datatracker.ietf.org/doc/html/rfc6749#section-4.4
    """

    client_id: str
    client_secret: str
    grant_type: Optional[str]
    scope: Optional[List[str]]


GrantType = Literal["password", "client_credentials"]
CredentialsLocation = Literal["request_body", "basic_authorization_header"]
BodyContent = Literal["form", "json"]


class OAuth2(AuthProvider):
    """
    Implements OAuth2 token retrieval and refreshing.
    Currently supports `password` and `client_credentials`
    grant types.
    """

    # OAuth2 provider configuration
    token_url: str
    access_token_pointer: str
    expires_in_pointer: str
    credentials_location: CredentialsLocation
    body_content: BodyContent
    request_mutator: AuthProvider

    # OAuth2 access token request values
    grant_type: GrantType
    username: Optional[str] = None
    password: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    scope: Optional[List[str]] = None

    # access_token storage
    access_token: Optional[str] = None
    expires_at: Optional[datetime.datetime] = None

    def _refresh(self) -> Tuple[str, datetime.datetime]:
        req_cfg: Dict[str, Any] = {"url": self.token_url}
        req_data: Dict[str, Any] = {"grant_type": self.grant_type}

        # add client credentials
        if self.client_id is not None or self.client_secret is not None:
            if self.credentials_location == "basic_authorization_header":
                req_cfg["auth"] = (self.client_id, self.client_secret)
            else:
                req_data["client_id"] = self.client_id
                req_data["client_secret"] = self.client_secret

        # construct request data
        if self.username is not None:
            req_data["username"] = self.username
        if self.password is not None:
            req_data["password"] = self.password
        if self.scope is not None:
            req_data["scope"] = " ".join(self.scope)

        if self.body_content == "json":
            req_cfg["json"] = req_data
            req_cfg["headers"] = {"content-type": "application/json"}
        else:
            req_cfg["data"] = req_data
            req_cfg["headers"] = {"content-type": "application/x-www-form-urlencoded"}

        # make access token request
        token_res = httpx.post(**req_cfg)
        token_res.raise_for_status()

        # retrieve access token & optional expiry seconds
        token_res_json: Dict[str, Any] = token_res.json()
        access_token = str(
            jsonpointer.resolve_pointer(token_res_json, self.access_token_pointer)
        )

        expires_in_secs = jsonpointer.resolve_pointer(
            token_res_json, self.expires_in_pointer
        )
        if not isinstance(expires_in_secs, int):
            expires_in_secs = 600
        expires_at = datetime.datetime.now() + datetime.timedelta(
            seconds=(
                expires_in_secs - 60
            )  # subtract a minute from the expiry as a buffer
        )

        return (access_token, expires_at)

    def add_to_request(self, cfg: RequestConfig) -> RequestConfig:
        token_expired = (
            self.expires_at is not None and self.expires_at <= datetime.datetime.now()
        )

        if self.access_token is None or token_expired:
            access_token, expires_at = self._refresh()
            self.expires_at = expires_at
            self.access_token = access_token

        self.request_mutator.set_value(self.access_token)
        return self.request_mutator.add_to_request(cfg)

    def set_value(self, _val: Optional[str]) -> None:
        raise NotImplementedError("an OAuth2 auth provider cannot be a request_mutator")
