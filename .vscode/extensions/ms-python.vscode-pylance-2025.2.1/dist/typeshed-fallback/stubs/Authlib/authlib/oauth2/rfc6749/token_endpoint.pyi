from _typeshed import Incomplete

class TokenEndpoint:
    ENDPOINT_NAME: Incomplete
    SUPPORTED_TOKEN_TYPES: Incomplete
    CLIENT_AUTH_METHODS: Incomplete
    server: Incomplete
    def __init__(self, server) -> None: ...
    def __call__(self, request): ...
    def create_endpoint_request(self, request): ...
    def authenticate_endpoint_client(self, request): ...
    def authenticate_token(self, request, client) -> None: ...
    def create_endpoint_response(self, request) -> None: ...
