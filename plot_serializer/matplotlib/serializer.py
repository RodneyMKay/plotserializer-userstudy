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
from matplotlib.lines import Line2D
from matplotlib.container import BarContainer

import numpy as np

from plot_serializer.serializer import Serializer
from plot_serializer.proxy import Proxy
from plot_serializer.model import (
    Axis,
    Bar2D,
    BarTrace2D,
    Figure,
    LineTrace2D,
    PiePlot,
    Plot,
    Plot2D,
    Point2D,
    Scale,
    Slice,
)


__all__ = ["MatplotlibSerializer"]


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


class _AxesProxy(Proxy[MplAxes]):
    def __init__(
        self, delegate: MplAxes, figure: Figure, serializer: Serializer
    ) -> None:
        super().__init__(delegate)
        self._figure = figure
        self._serializer = serializer
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

        pie_plot = PiePlot(type="pie", slices=slices)
        self._plot = pie_plot
        return self.delegate.pie(size_list, **kwargs)

    # FIXME: name_list and height_list cannot only be floats, but also different other types of data
    def bar(
        self, label_list: Iterable[str], height_list: Iterable[float], **kwargs: Any
    ) -> BarContainer:
        bars: List[Bar2D] = []

        color_list = kwargs.get("color") or []

        for i, label in enumerate(label_list):
            height = height_list[i]
            color = color_list[i] if i < len(color_list) else None

            bars.append(
                Bar2D(y=height, label=label, color=_convert_matplotlib_color(color))
            )

        trace = BarTrace2D(type="bar", datapoints=bars)

        if self._plot is not None:
            if not isinstance(self._plot, Plot2D):
                raise NotImplementedError(
                    "PlotSerializer does not yet support mixing 2d plots with other plots!"
                )

            self._plot.traces.append(trace)
        else:
            self._plot = Plot2D(type="2d", x_axis=Axis(), y_axis=Axis(), traces=[trace])

        return self.delegate.bar(label_list, height_list, **kwargs)

    def plot(self, *args: Any, **kwargs: Any) -> list[Line2D]:
        mpl_lines = self.delegate.plot(*args, **kwargs)
        traces: List[LineTrace2D] = []

        for mpl_line in mpl_lines:
            xdata = mpl_line.get_xdata()
            ydata = mpl_line.get_ydata()

            points: List[Point2D] = []

            for x, y in zip(xdata, ydata):
                points.append(Point2D(x=x, y=y))

            label = mpl_line.get_label()
            color = _convert_matplotlib_color(mpl_line.get_color())
            thickness = mpl_line.get_linewidth()
            linestyle = mpl_line.get_linestyle()

            traces.append(
                LineTrace2D(
                    type="line",
                    line_color=color,
                    line_thickness=thickness,
                    line_style=linestyle,
                    label=label,
                    datapoints=points,
                )
            )

        if self._plot is not None:
            if not isinstance(self._plot, Plot2D):
                raise NotImplementedError(
                    "PlotSerializer does not yet support mixing 2d plots with other plots!"
                )

            self._plot.traces += traces
        else:
            self._plot = Plot2D(type="2d", x_axis=Axis(), y_axis=Axis(), traces=traces)

        return mpl_lines

    def _on_collect(self) -> None:
        if self._plot is None:
            return

        self._plot.title = self.delegate.get_title()

        if isinstance(self._plot, Plot2D):
            xlabel = self.delegate.get_xlabel()
            xscale = _convert_matplotlib_scale(self.delegate.get_xscale())

            self._plot.x_axis.label = xlabel
            self._plot.x_axis.scale = xscale

            ylabel = self.delegate.get_ylabel()
            yscale = _convert_matplotlib_scale(self.delegate.get_yscale())

            self._plot.y_axis.label = ylabel
            self._plot.y_axis.scale = yscale

        self._figure.plots.append(self._plot)


class MatplotlibSerializer(Serializer):
    """
    Serializer specific to matplotlib. Most of the methods on this object mirror the
    matplotlib.pyplot api from matplotlib.

    Args:
        Serializer (_type_): Parent class
    """

    def _create_axes_proxy(self, mpl_axes: MplAxes) -> _AxesProxy:
        proxy = _AxesProxy(mpl_axes, self._figure, self)
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