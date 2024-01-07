from abc import ABC, abstractmethod
from typing import Any
from typing_extensions import Self

from plot_serializer.model import Figure


class Adapter(ABC):
    @abstractmethod
    def serialize(self: Self, figure: Any) -> Figure:
        pass

    @abstractmethod
    def deserialize(self: Self, figure: Figure) -> Any:
        pass


def select_adapter(name: str):
    pass
