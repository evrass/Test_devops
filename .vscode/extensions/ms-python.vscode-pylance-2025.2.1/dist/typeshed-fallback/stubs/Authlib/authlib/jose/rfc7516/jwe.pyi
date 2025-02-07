from _typeshed import Incomplete

class JsonWebEncryption:
    REGISTERED_HEADER_PARAMETER_NAMES: Incomplete
    ALG_REGISTRY: Incomplete
    ENC_REGISTRY: Incomplete
    ZIP_REGISTRY: Incomplete
    def __init__(self, algorithms: Incomplete | None = None, private_headers: Incomplete | None = None) -> None: ...
    @classmethod
    def register_algorithm(cls, algorithm) -> None: ...
    def serialize_compact(self, protected, payload, key, sender_key: Incomplete | None = None): ...
    def serialize_json(self, header_obj, payload, keys, sender_key: Incomplete | None = None): ...
    def serialize(self, header, payload, key, sender_key: Incomplete | None = None): ...
    def deserialize_compact(self, s, key, decode: Incomplete | None = None, sender_key: Incomplete | None = None): ...
    def deserialize_json(self, obj, key, decode: Incomplete | None = None, sender_key: Incomplete | None = None): ...
    def deserialize(self, obj, key, decode: Incomplete | None = None, sender_key: Incomplete | None = None): ...
    @staticmethod
    def parse_json(obj): ...
    def get_header_alg(self, header): ...
    def get_header_enc(self, header): ...
    def get_header_zip(self, header): ...

def prepare_key(alg, header, key): ...
