from collections.abc import Collection
from typing_extensions import TypeAlias

from authlib.oauth2 import OAuth2Request
from authlib.oauth2.rfc6749 import AuthorizationEndpointMixin, BaseGrant, ClientMixin, TokenEndpointMixin

_ServerResponse: TypeAlias = tuple[int, str, list[tuple[str, str]]]

class AuthorizationCodeGrant(BaseGrant, AuthorizationEndpointMixin, TokenEndpointMixin):
    TOKEN_ENDPOINT_AUTH_METHODS: Collection[str]
    AUTHORIZATION_CODE_LENGTH: int
    RESPONSE_TYPES: Collection[str]
    GRANT_TYPE: str
    def validate_authorization_request(self) -> str: ...
    def create_authorization_response(self, redirect_uri: str, grant_user) -> _ServerResponse: ...
    def validate_token_request(self) -> None: ...
    def create_token_response(self) -> _ServerResponse: ...
    def generate_authorization_code(self) -> str: ...
    def save_authorization_code(self, code: str, request: OAuth2Request) -> None: ...
    def query_authorization_code(self, code: str, client: ClientMixin): ...
    def delete_authorization_code(self, authorization_code) -> None: ...
    def authenticate_user(self, authorization_code): ...

def validate_code_authorization_request(grant: AuthorizationCodeGrant) -> str: ...
