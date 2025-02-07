from _typeshed import Incomplete

from authlib.jose import BaseClaims

class ClientMetadataClaims(BaseClaims):
    REGISTERED_CLAIMS: Incomplete
    def validate(self) -> None: ...
    def validate_redirect_uris(self) -> None: ...
    def validate_token_endpoint_auth_method(self) -> None: ...
    def validate_grant_types(self) -> None: ...
    def validate_response_types(self) -> None: ...
    def validate_client_name(self) -> None: ...
    def validate_client_uri(self) -> None: ...
    def validate_logo_uri(self) -> None: ...
    def validate_scope(self) -> None: ...
    def validate_contacts(self) -> None: ...
    def validate_tos_uri(self) -> None: ...
    def validate_policy_uri(self) -> None: ...
    def validate_jwks_uri(self) -> None: ...
    def validate_jwks(self) -> None: ...
    def validate_software_id(self) -> None: ...
    def validate_software_version(self) -> None: ...
