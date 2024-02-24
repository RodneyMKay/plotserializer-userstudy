import json
import os

from plot_serializer.model import (
    Figure,
    PiePlot,
    Plot2D,
    LineTrace2D,
    BarTrace2D,
    ScatterTrace2D,
)

import matplotlib.pyplot as plt
from matplotlib.axes import Axes as MplAxes


class Deserializer:
    # FIXME add filename parameter
    def json_to_figure(self, filename: str) -> Figure:
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, filename)
        with open(filename, "r") as openfile:
            # Reading from json file
            d = json.load(openfile)
        # logic to parse everything
        figure = Figure.model_validate_json(json_data=json.dumps(d))
        return figure

    # FIXME add filename parameter
    def json_to_matplotlib_figure(self, filename: str) -> None:
        model_figure = self.json_to_figure(filename=filename)
        fig, axs = plt.subplots(len(model_figure.plots))
        if len(model_figure.plots) == 1:
            axs = [axs]  # make axs subcribtable
        if model_figure.title is not None:
            fig.suptitle(model_figure.title)
        i = 0
        for plot in model_figure.plots:
            if plot.title is not None:
                axs[i].title.set_text(plot.title)
            if isinstance(plot, Plot2D):
                self._parse_Plot2D(plot, axs[i])
            elif isinstance(plot, PiePlot):
                self._parse_PiePlot(plot, axs[i])
            i += 1
        plt.show()

    def _parse_axis(self, plot: Plot2D, ax: MplAxes) -> None:
        # FIXME make sure this is not causing erros for unspecified scales
        ax.set_xlabel("" if plot.x_axis.label is None else plot.x_axis.label)
        ax.set_xscale("" if plot.x_axis.scale is None else plot.x_axis.scale)
        ax.set_ylabel("" if plot.y_axis.label is None else plot.y_axis.label)
        ax.set_yscale("" if plot.y_axis.scale is None else plot.y_axis.scale)

    def _parse_Plot2D(self, p: Plot2D, ax: MplAxes) -> None:
        self._parse_axis(p, ax)
        if p.title is not None:
            plt.title(p.title)
        if p.x_axis.label is not None:
            ax.set_xlabel(p.x_axis.label)
        if p.x_axis.scale is not None:
            ax.set_xscale(p.x_axis.scale)
        if p.y_axis.label is not None:
            ax.set_ylabel(p.y_axis.label)
        if p.x_axis.scale is not None:
            ax.set_yscale(p.x_axis.scale)
        for trace in p.traces:
            if isinstance(trace, LineTrace2D):
                self._parse_LineTrace2D(trace=trace, ax=ax)
            elif isinstance(trace, ScatterTrace2D):
                self._parse_ScatterTrace2D(trace=trace, ax=ax)
            elif isinstance(trace, BarTrace2D):
                self._parse_BarTrace2D(trace=trace, ax=ax)

    def _parse_LineTrace2D(self, trace: LineTrace2D, ax: MplAxes) -> None:
        # FIXME don't show legend if there arent any legends i.e. none 2Dplots
        # plt.legend(loc="upper center")
        x = []
        y = []
        for point in trace.datapoints:
            x.append(point.x)
            y.append(point.y)
        ax.plot(
            x,
            y,
            label=trace.label,
            color=trace.line_color,
            linewidth=trace.line_thickness,
            linestyle=trace.line_style,
        )

    def _parse_ScatterTrace2D(self, trace: ScatterTrace2D, ax: MplAxes) -> None:
        x = []
        y = []
        for point in trace.datapoints:
            x.append(point.x)
            y.append(point.y)
        ax.scatter(x, y)

    def _parse_BarTrace2D(self, trace: BarTrace2D, ax: MplAxes) -> None:
        label = []
        y = []
        color: list[str] = []
        for bar in trace.datapoints:
            label.append(bar.label)
            y.append(bar.y)
            if bar.color is not None:
                color.append(bar.color)
        ax.bar(label, y, color=color if color != [] else None)

    def _parse_PiePlot(self, p: PiePlot, ax: MplAxes) -> None:
        size = []
        radius = []
        offset: list[float] = []
        name: list[str] = []
        color: list[str] = []

        for slice in p.slices:
            size.append(slice.size)
            if slice.name is not None:
                name.append(slice.name)
            if slice.radius is not None:
                radius.append(slice.radius)
            if slice.offset is not None:
                offset.append(slice.offset)
            if slice.color is not None:
                color.append(slice.color)
        ax.pie(
            size,
            labels=name if name != [] else None,
            colors=color if color != [] else None,
            explode=offset if offset != [] else None,
        )
