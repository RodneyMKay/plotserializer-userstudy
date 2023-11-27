"""Adapters


"""
from typing_extensions import Self
from plot_serializer.plot import Plot, Axis, Trace
from matplotlib.figure import Figure as MplFigure
from matplotlib.axis import Axis as MplAxis


class MatplotlibAdapter(Plot):
    def __init__(self: Self, figure: MplFigure) -> None:
        super().__init__()
        self.axes = self.get_axes(figure)
        pass

    def get_axes(self: Self, figure: MplFigure):
        axes = []
        for axis in figure.axes:
            a = Axis()
            a.traces = self.get_traces(axis)
            axes.append(a)
        return axes

    def get_traces(self: Self, axis: MplAxis):
        lines = self.get_lines(axis)
        # collections = self.get_collections()
        return lines

    def get_lines(self: Self, axis: MplAxis):
        lines = []
        if len(axis.lines) > 0:
            for line in axis.lines:
                trace = Trace()
                trace.xdata = list(line.get_xdata())
                trace.ydata = list(line.get_ydata())
                trace.label = line.get_label()
                trace.color = line.get_color()
                trace.type = str(type(line))
                lines.append(trace)
        return lines
