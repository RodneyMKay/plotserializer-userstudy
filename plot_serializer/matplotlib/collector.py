from typing import Any, List, Literal, Sequence, Tuple
from matplotlib.figure import Figure as MplFigure
import matplotlib.pyplot
import numpy as np
from plot_serializer.collector import Collector
from plot_serializer.model import Figure, PiePlot, Slice

from plot_serializer.proxy import Proxy


class AxesProxy(Proxy):
    def __init__(self, delegate: Any, figure: Figure) -> None:
        self._figure = figure
        super().__init__(delegate)

    def pie(self, *args: Any, **kwargs: Any) -> Any:
        slices: List[Slice] = []

        size_list = args[0]
        color_list = kwargs.get("colors") or list()
        explode_list = kwargs.get("explode") or list()
        label_list = kwargs.get("labels") or list()
        radius_list = kwargs.get("radius") or list()

        for i, size in enumerate(size_list):
            color = color_list[i] if i < len(color_list) else None
            explode = explode_list[i] if i < len(explode_list) else None
            label = label_list[i] if i < len(label_list) else None
            radius = radius_list[i] if i < len(radius_list) else None

            slices.append(
                Slice(size=size, radius=radius, offset=explode, name=label, color=color)
            )

        pie_plot = PiePlot(type="pie", slices=slices)
        self._figure.plots.append(pie_plot)
        return self.proxy_call("pie", *args, **kwargs)


class MatplotlibCollector(Collector):
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
            **fig_kw,
        )

        new_axes: Any

        if isinstance(axes, np.ndarray):
            new_axes = np.array(map(lambda x: AxesProxy(x, self._figure), axes))
        else:
            new_axes = AxesProxy(axes, self._figure)

        return (figure, new_axes)
