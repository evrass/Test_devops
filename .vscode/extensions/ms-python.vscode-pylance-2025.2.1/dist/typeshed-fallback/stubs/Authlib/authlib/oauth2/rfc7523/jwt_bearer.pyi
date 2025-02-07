from _typeshed import Incomplete

from authlib.oauth2.rfc6749 import BaseGrant, TokenEndpointMixin

JWT_BEARER_GRANT_TYPE: str

class JWTBearerGrant(BaseGrant, TokenEndpointMixin):
    GRANT_TYPE = JWT_BEARER_GRANT_TYPE
    CLAIMS_OPTIONS: Incomplete
    @staticmethod
    def sign(
        key,
        issuer,
        audience,
        subject: Incomplete | None = None,
        issued_at: Incomplete | None = None,
        expires_at: Incomplete | None = None,
        claims: Incomplete | None = None,
        **kwargs,
    ): ...
    def process_assertion_claims(self, assertion): ...
    def resolve_public_key(self, headers, payload): ...
    def validate_token_request(self) -> None: ...
    def create_token_response(self): ...
    def resolve_issuer_client(self, issuer) -> None: ...
    def resolve_client_key(self, client, headers, payload) -> None: ...
    def authenticate_user(self, subject) -> None: ...
    def has_granted_permission(self, client, user) -> None: ...
