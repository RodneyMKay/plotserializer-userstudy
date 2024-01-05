from typing import Any
from typing_extensions import Self
from plot_serializer.adapter import Adapter
from plot_serializer.model import Figure
from matplotlib.figure import Figure as MplFigure


class MatplotlibAdapter(Adapter):
    def serialize(self: Self, figure: Any) -> Figure:
        raise NotImplementedError()

    def deserialize(self: Self, figure: Figure) -> MplFigure:
        raise NotImplementedError()
