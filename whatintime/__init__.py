import time
from enum import Enum, auto
from functools import wraps
from typing import Callable


class TimeFormat(Enum):
    NS = auto()
    MS = auto()
    S = auto()
    M = auto()
    H = auto()

    def __call__(self, ns: int) -> float:
        if self == TimeFormat.NS:
            return ns
        elif self == TimeFormat.MS:
            return ns / 1000
        elif self == TimeFormat.S:
            return ns / 1000 / 1000
        elif self == TimeFormat.M:
            return ns / 1000 / 1000 / 60
        elif self == TimeFormat.H:
            return ns / 1000 / 1000 / 60 / 60


def whatintime(time_format: TimeFormat = TimeFormat.NS) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.monotonic_ns()
            ret = func(*args, **kwargs)
            end = time.monotonic_ns()
            print(
                f"Function {func.__name__} took {time_format(start-end)}{time_format.name}"
            )
            return ret

        return wrapper

    return decorator
