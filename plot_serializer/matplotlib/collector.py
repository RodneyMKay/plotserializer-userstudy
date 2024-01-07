from typing import Any, List, Literal, Sequence, Tuple, Union
from matplotlib.axes import Axes as MplAxes
from matplotlib.figure import Figure as MplFigure
import matplotlib.pyplot
import numpy as np
from plot_serializer.model import Figure, Line

from plot_serializer.proxy import Proxy


class Line2DProxy(Proxy):
    pass


class PathCollectionProxy(Proxy):
    pass


class WedgeProxy(Proxy):
    pass


class TextProxy(Proxy):
    pass


class AxesProxy(Proxy):
    def pie(
        self,
    ) -> Union[
        Tuple[List[WedgeProxy], List[TextProxy]],
        Tuple[List[WedgeProxy], List[TextProxy], List[TextProxy]],
    ]:
        pass

    def plot(self, *args, **kwargs) -> Line2DProxy:
        self.proxy_call("plot", args, kwargs)
        pass

    def scatter(
        self,
    ) -> PathCollectionProxy:
        pass


class MatplotlibCollector:
    def __init__(self) -> None:
        self._figure = Figure()

    def subplots(
        self,
        nrows: int = 1,
        ncols: int = 1,
        *,
        sharex: bool | Literal["none", "all", "row", "col"] = False,
        sharey: bool | Literal["none", "all", "row", "col"] = False,
        squeeze: bool = True,
        width_ratios: Sequence[float] | None = None,
        height_ratios: Sequence[float] | None = None,
        subplot_kw: dict[str, Any] | None = None,
        gridspec_kw: dict[str, Any] | None = None,
        **fig_kw: Any,
    ) -> Tuple[MplFigure, Any]:
        figure, axes = matplotlib.pyplot.subplots(
            nrows,
            ncols,
            sharex=sharex,
            sharey=sharey,
            squeeze=squeeze,
            width_ratios=width_ratios,
            height_ratios=height_ratios,
            subplot_kw=subplot_kw,
            gridspec_kw=gridspec_kw,
            fig_kw=fig_kw,
        )

        new_axes: Any

        if isinstance(axes, np.ndarray):
            new_axes = np.array(map(AxesProxy, axes))
        else:
            new_axes = AxesProxy(axes)

        return (figure, new_axes)
