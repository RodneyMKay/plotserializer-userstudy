"""Adapters


"""
from typing import List
from typing_extensions import Self

from matplotlib.axes import Axes as MplAxes
from matplotlib.figure import Figure as MplFigure

from plot_serializer.plot import Plot as plPlot, Axis as plAxis, Trace as plTrace


class MatplotlibAdapter(plPlot):
    def __init__(self: Self, figure: MplFigure) -> None:
        super().__init__()
        self.axes = self.get_axes(figure)

    def get_axes(self: Self, figure: MplFigure) -> List[plAxis]:
        return_axes: List[plAxis] = []
        for axes in figure.axes:
            axis = plAxis()
            axis.traces = self.get_traces(axes)
            return_axes.append(axis)
        return return_axes

    def get_traces(self: Self, axes: MplAxes) -> List[plTrace]:
        lines = self.get_lines(axes)
        # collections = self.get_collections()
        return lines

    def get_lines(self: Self, axes: MplAxes) -> List[plTrace]:
        lines: List[plTrace] = []
        if len(axes.lines) > 0:
            for line in axes.lines:
                trace = plTrace()
                # FIXME: xdata and ydata could potentially also return
                # ArrayLike that aren't actually of type int.
                trace.xdata = list(line.get_xdata())
                trace.ydata = list(line.get_ydata())
                trace.label = str(line.get_label())
                trace.color = str(line.get_color())
                trace.type = str(type(line))
                lines.append(trace)
        return lines
