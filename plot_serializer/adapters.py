"""Adapters


"""
from typing import List
from typing_extensions import Self

from matplotlib.axes import Axes as MplAxes
from matplotlib.collections import PathCollection
from matplotlib.container import BarContainer, ErrorbarContainer
from matplotlib.figure import Figure as MplFigure
from matplotlib.lines import Line2D

from plot_serializer.plot import Plot as plPlot, Axis as plAxis, Trace as plTrace

from plot_serializer.datastructure import (
    Canvas,
    DataPoint,
    MPLLineDataStyling,
    Plot,
    Axis,
    DataCollection,
    Units,
)


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


class My_New_MatplotlibAdapter(Canvas):
    def __init__(self: Self, figure: MplFigure) -> None:
        super().__init__(plots=self.get_plots(figure), styling=None)

        # TODO
        self.styling = None

    def get_plots(self: Self, figure: MplFigure):
        print("get_plots:")
        list: List = []

        for axe in figure.axes:
            print(f"axe get_titel: {axe.get_title()}")
            print(f"axe titel: {axe.title}")

            list.append(
                Plot(
                    title=axe.get_title(),
                    axes=self.get_axes(axe),
                    graphs=self.get_graphs(axe),
                )
            )

        return list

    # NOTE: axes as in plural of axis not MPLAxes !!!
    def get_axes(self: Self, axe: MplAxes) -> List[Axis]:
        print("get_axes:")
        # TODO 3D stuff

        axe.xaxis.set_label("Test")
        axe.yaxis

        print(axe.xaxis.label)
        print(axe.xaxis.get_label())
        print(axe.yaxis.label)
        print(axe.yaxis.get_label())

        # TODO
        xaxis: Axis = Axis(label="TODO")
        yaxis: Axis = Axis(label="TODO")
        return [xaxis, yaxis]

    def get_graphs(self: Self, axe: MplAxes) -> List[DataCollection]:
        list: List[DataCollection] = []

        for line in axe.lines:
            list.append(self.get_line_data(line))

        for collection in axe.collections:
            if isinstance(collection, PathCollection):
                list.append(self.get_scatter_data(collection))

        for container in axe.containers:
            if isinstance(container, BarContainer):
                list.append(self.get_barchart_data(container))

            if isinstance(container, ErrorbarContainer):
                list.append(self.get_errorbar_data(container))

        return list

    def get_line_data(self: Self, line: Line2D) -> DataCollection:
        print("get_line_data:")
        xdata = line.get_xdata()
        ydata = line.get_ydata()
        lable = line.get_label()
        color = line.get_color()
        line_type = type(line)

        print(f"- -x data: {xdata}")
        print(f"- -y data: {ydata}")
        print(f"- -lable: {lable}")
        print(f"- -color: {color}")
        print(f"- -line type: {line_type}")

        if len(xdata) != len(ydata):
            # TODO which error to use ?
            # FIXME could use izip_longest for [(data, None), (data, None)]
            raise IndexError("(len(xdata) != len(ydata):)")

        data: List[DataPoint] = []

        for x, y in zip(xdata, ydata):
            data.append(DataPoint(values=(x, y)))

        styling: MPLLineDataStyling = MPLLineDataStyling(
            color=color, label=lable, type=line_type
        )

        # TODO get Units
        return DataCollection(units=Units(units=None), data=data, styling=styling)

    def get_scatter_data(self: Self, collection: PathCollection) -> DataCollection:
        sizes = collection.get_sizes()
        data_points = collection.get_offsets()
        # get Color information from ScalarMappable
        colors = collection.to_rgba(range(len(collection.get_offsets()) + 1))

        print(f"- -size: {sizes}")
        print(f'- -"offset": {data_points}')
        print(f"- -color: {colors}")

        # TODO
        raise NotImplementedError("get_scatter_data")

    def get_barchart_data(self: Self, container: BarContainer) -> DataCollection:
        print(f"- -patches: {container.patches}")

        for patch in container.patches:
            print(f"- -patch: {patch}")

        # TODO
        raise NotImplementedError("get_barchart_data")

    def get_errorbar_data(self: Self, container: ErrorbarContainer) -> DataCollection:
        # TODO
        raise NotImplementedError("get_errorbar_data")
