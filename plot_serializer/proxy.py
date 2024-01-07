from typing import Any


class Proxy:
    def __init__(self, delegate: Any) -> None:
        self._delegate = delegate

    def __getattribute__(self, __name: str) -> Any:
        if __name.startswith("_"):
            return super().__getattribute__(__name)

        own_value = super().__getattribute__(__name)

        if own_value is not None:
            return own_value

        return self._delegate.__getattribute__(__name)

    def proxy_call(self, name: str, *args: Any, **kwargs: Any) -> Any:
        return self._delegate.__getattribute__(name)(*args, **kwargs)
