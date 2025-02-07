from typing import Any, Final

DEBUG: Final = 1
INFO: Final = 2
WARN: Final = 3
ERROR: Final = 4
FATAL: Final = 5

class Log:
    def __init__(self, threshold: int = 3) -> None: ...
    # Arbitrary msg args' type depends on the format method
    def log(self, level: int, msg: str, *args: Any) -> None: ...
    def debug(self, msg: str, *args: Any) -> None: ...
    def info(self, msg: str, *args: Any) -> None: ...
    def warn(self, msg: str, *args: Any) -> None: ...
    def error(self, msg: str, *args: Any) -> None: ...
    def fatal(self, msg: str, *args: Any) -> None: ...

def log(level: int, msg: str, *args: Any) -> None: ...
def debug(msg: str, *args: Any) -> None: ...
def info(msg: str, *args: Any) -> None: ...
def warn(msg: str, *args: Any) -> None: ...
def error(msg: str, *args: Any) -> None: ...
def fatal(msg: str, *args: Any) -> None: ...
def set_threshold(level: int) -> int: ...
def set_verbosity(v: int) -> None: ...
