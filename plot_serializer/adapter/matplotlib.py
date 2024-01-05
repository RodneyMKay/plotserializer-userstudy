from typing import Any, List
from typing_extensions import Self
from matplotlib.collections import PathCollection
from matplotlib.container import BarContainer, ErrorbarContainer

from matplotlib.lines import Line2D as MplLine2D
from plot_serializer.adapter import Adapter
from plot_serializer.model import (
    Axis,
    BarPlot,
    Figure,
    Line,
    PiePlot,
    Plot,
    Plot2D,
    Point2D,
    Vec2F,
)
from matplotlib.figure import Figure as MplFigure
from matplotlib.axes import Axes as MplAxes


class MatplotlibAdapter(Adapter):
    def serialize(self: Self, figure: Any) -> Figure:
        return Figure(plots=self.get_plots(mplAxes=figure.axes))

        raise NotImplementedError()

    def deserialize(self: Self, figure: Figure) -> MplFigure:
        raise NotImplementedError()

    def get_plots(self: Self, mplAxes: List[MplAxes]) -> List[Plot]:
        print("get_plots:")
        list: List[Plot]

        for axe in mplAxes:
            plot2Ds: List[Plot2D] = []
            barPlots: List[BarPlot] = []
            piePlots: List[PiePlot] = []

            print(f"axe get_titel: {axe.get_title()}")
            print(f"axe titel: {axe.title}")

            for line in axe.lines:
                # TODO
                pass

            for collection in axe.collections:
                if isinstance(collection, PathCollection):
                    # TODO
                    pass

            for container in axe.containers:
                if isinstance(container, BarContainer):
                    # TODO
                    pass

                if isinstance(container, ErrorbarContainer):
                    # TODO
                    pass

        return list

    def get_xaxis(self: Self, axe: MplAxes) -> Axis:
        # TODO
        xaxis: Axis = Axis(label="TODO")
        pass

    def get_yaxes(self: Self, axe: MplAxes) -> Axis:
        # TODO
        yaxis: Axis = Axis(label="TODO")
        pass

    def get_line(self: Self, line: MplLine2D) -> Line:
        print("get_line_data:")
        xdata = line.get_xdata()
        ydata = line.get_ydata()
        lable = line.get_label()
        color = line.get_color()
        linestyle = line.get_linestyle()
        line_type = type(line)

        print(f"- -x data: {xdata}")
        print(f"- -y data: {ydata}")
        print(f"- -lable: {lable}")
        print(f"- -color: {color}")
        print(f"- -linestyle:  {linestyle}")
        print(f"- -line type: {line_type}")

        if len(xdata) != len(ydata):
            # should never happen but hey, you can never be tooooooo sure XD
            # TODO which error to use ?
            # FIXME could use izip_longest for [(data, None), (data, None)]
            raise IndexError("(len(xdata) != len(ydata):)")

        datapoints: List[Point2D] = []

        for x, y in zip(xdata, ydata):
            datapoints.append(Point2D(position=Vec2F(x, y)))

        # TODO get Units
        return Line(datapoints=datapoints, color=color, linestyle=linestyle)
