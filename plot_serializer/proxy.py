from typing import Any, Generic, TypeVar


T = TypeVar("T")


class Proxy(Generic[T]):
    def __init__(self, delegate: T) -> None:
        self._delegate = delegate

    def __getattribute__(self, __name: str) -> Any:
        own_value = super().__getattribute__(__name)

        if own_value is not None:
            return own_value

        return self._delegate.__getattribute__(__name)

    def proxy_call(self, name: str, *args: Any, **kwargs: Any) -> Any:
        return self._delegate.__getattribute__(name)(*args, **kwargs)
