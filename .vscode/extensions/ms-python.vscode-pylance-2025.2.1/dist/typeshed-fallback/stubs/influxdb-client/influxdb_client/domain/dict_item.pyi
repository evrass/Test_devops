from _typeshed import Incomplete

class DictItem:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, type: Incomplete | None = None, key: Incomplete | None = None, val: Incomplete | None = None) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def key(self): ...
    @key.setter
    def key(self, key) -> None: ...
    @property
    def val(self): ...
    @val.setter
    def val(self, val) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
