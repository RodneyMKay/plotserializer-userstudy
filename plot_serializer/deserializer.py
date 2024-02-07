import json
import os
from turtle import title

from plot_serializer.model import BarPlot, Figure, PiePlot, Plot2D

import matplotlib.pyplot as plt
from matplotlib.axes import Axes as MplAxes


class Deserializer:
    # FIXME add filename parameter
    def json_to_figure(self) -> Figure:
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "../tests/plots/line_plot_all_features.json")
        with open(filename, "r") as openfile:
            # Reading from json file
            d = json.load(openfile)
        # logic to parse everything
        figure = Figure.model_validate_json(json_data=json.dumps(d))
        return figure

    # FIXME add filename parameter
    def json_to_matplotlib_figure(self) -> None:
        old_fig = self.json_to_figure()
        fig, axs = plt.subplots(len(old_fig.plots))
        if len(old_fig.plots) == 1:
            axs = [axs]  # make axs subcribtable
        # fig.suptitle(t=old_fig.title)
        i = 0
        for plot in old_fig.plots:
            if isinstance(plot, Plot2D):
                self._parse_Plot2D(plot, axs[i])
            elif isinstance(plot, PiePlot):
                axs[i] = self._parse_PiePlot(plot)
            elif isinstance(plot, BarPlot):
                axs[i] = self._parse_BarPlot(plot)
            i += 1
        plt.show()

    def _parse_Plot2D(self, p: Plot2D, ax: MplAxes) -> None:
        for line in p.lines:
            x = []
            y = []
            for point in line.datapoints:
                x.append(point.x)
                y.append(point.y)
            ax.plot(x, y)
        # FIXME add points for scatter

    def _parse_PiePlot(self, p: PiePlot) -> MplAxes:
        raise NotImplementedError()

    def _parse_BarPlot(self, p: BarPlot) -> MplAxes:
        raise NotImplementedError()
