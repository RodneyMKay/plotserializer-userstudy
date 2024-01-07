from typing import Any, Generic, TypeVar


T = TypeVar("T")


class Proxy(Generic[T]):
    def __init__(self, delegate: T) -> None:
        self._delegate = delegate

    def __getattr__(self, __name: str) -> Any:
        return getattr(self._delegate, __name)

    def delegate(self) -> T:
        return self._delegate
