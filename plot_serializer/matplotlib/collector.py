from typing import (
    Any,
    Iterable,
    List,
    Optional,
    Tuple,
    Union,
)

from matplotlib.figure import Figure as MplFigure
from matplotlib.axes import Axes as MplAxes
import matplotlib.pyplot

import numpy as np

from plot_serializer.collector import Collector
from plot_serializer.proxy import Proxy
from plot_serializer.model import (
    Axis,
    Bar,
    BarPlot,
    Figure,
    PiePlot,
    Plot,
    Scale,
    Slice,
)


def _convert_matplotlib_scale(scale: str) -> Scale:
    if scale == "linear":
        return "linear"
    elif scale == "log":
        return "logarithmic"
    else:
        raise NotImplementedError(
            "This type of scaling is not supported in PlotSerializer yet!"
        )


def _convert_matplotlib_color(color: str) -> str:
    # TODO: We leave the color as-is for now, but we should probably
    #  build some kind of conversion later, so plotserializer has a
    #  predictable color format between different plotting libraries.
    return color


class AxesProxy(Proxy[MplAxes]):
    def __init__(self, delegate: MplAxes, figure: Figure, collector: Collector) -> None:
        super().__init__(delegate)
        self._figure = figure
        self._collector = collector
        self._plot: Optional[Plot] = None

    # FIXME: size_list cannot only be floats, but also different other types of data
    def pie(self, size_list: Iterable[float], **kwargs: Any) -> Any:
        if self._plot is not None:
            raise NotImplementedError(
                "PlotSerializer does not yet support adding multiple plots per axes!"
            )

        slices: List[Slice] = []

        color_list = kwargs.get("colors") or []
        explode_list = kwargs.get("explode") or []
        label_list = kwargs.get("labels") or []
        radius_list = kwargs.get("radius") or []

        for i, size in enumerate(size_list):
            color = color_list[i] if i < len(color_list) else None
            explode = explode_list[i] if i < len(explode_list) else None
            label = label_list[i] if i < len(label_list) else None
            radius = radius_list[i] if i < len(radius_list) else None

            slices.append(
                Slice(
                    size=size,
                    radius=radius,
                    offset=explode,
                    name=label,
                    color=_convert_matplotlib_color(color),
                )
            )

        pie_plot = PiePlot(slices=slices)
        self._plot = pie_plot
        return self.delegate().pie(size_list, **kwargs)

    # FIXME: name_list and height_list cannot only be floats, but also different other types of data
    def bar(
        self, name_list: Iterable[str], height_list: Iterable[float], **kwargs: Any
    ) -> Any:
        if self._plot is not None:
            raise NotImplementedError(
                "PlotSerializer does not yet support adding multiple plots per axes!"
            )

        bars: List[Bar] = []

        color_list = kwargs.get("color") or []

        for i, name in enumerate(name_list):
            height = height_list[i]
            color = color_list[i] if i < len(color_list) else None

            bars.append(
                Bar(name=name, height=height, color=_convert_matplotlib_color(color))
            )

        bar_plot = BarPlot(y_axis=Axis(), bars=bars)
        self._plot = bar_plot
        return self.delegate().bar(name_list, height_list, **kwargs)

    def _on_collect(self) -> None:
        if self._plot is None:
            return

        self._plot.title = self._delegate.get_title()

        if isinstance(self._plot, BarPlot):
            ylabel = self._delegate.get_ylabel()
            yscale = _convert_matplotlib_scale(self._delegate.get_yscale())

            self._plot.y_axis.label = ylabel
            self._plot.y_axis.scale = yscale

        self._figure.plots.append(self._plot)


class MatplotlibCollector(Collector):
    def _create_axes_proxy(self, mpl_axes: MplAxes) -> AxesProxy:
        proxy = AxesProxy(mpl_axes, self._figure, self)
        self._add_collect_action(lambda: proxy._on_collect())
        return proxy

    def subplots(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> Tuple[MplFigure, Union[MplAxes, Any]]:
        figure, axes = matplotlib.pyplot.subplots(*args, **kwargs)

        new_axes: Any

        if isinstance(axes, np.ndarray):
            new_axes = np.array(list(map(self._create_axes_proxy, axes)))
        else:
            new_axes = self._create_axes_proxy(axes)

        return (figure, new_axes)
