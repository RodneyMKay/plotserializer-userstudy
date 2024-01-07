from typing import Any, List, Tuple, Union
from matplotlib.axes import Axes as MplAxes
from matplotlib.figure import Figure as MplFigure
import matplotlib.pyplot
import numpy as np
from plot_serializer.model import Figure

from plot_serializer.proxy import Proxy


class AxesProxy(Proxy):
    def pie():
        pass


class MatplotlibCollector:
    def __init__(self) -> None:
        self._figure = Figure()

    def subplots(
        *args: Any,
        **kwargs: Any,
    ) -> Tuple[MplFigure, Any]:
        figure, axes = matplotlib.pyplot.subplots(*args, **kwargs)

        new_axes: Any

        if isinstance(axes, np.ndarray):
            new_axes = np.array(map(lambda x: AxesProxy(x), axes))
        else:
            new_axes = AxesProxy(axes)

        return (figure, new_axes)
