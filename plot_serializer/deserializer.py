from typing_extensions import Self
from typing import Any, Dict, TypeVar
import json
import matplotlib.pyplot as plt
from matplotlib.figure import Figure as MplFigure

from plot_serializer.plot import Plot, Axis, Trace


_T = TypeVar("_T")


class Deserializer:
    def __init__(self: Self) -> None:
        self._plot = None
        pass

    def from_json(self: Self, filename: str) -> Plot:
        """Creates a Plot object out of a JSON file created with Serializer.

        Args:
            filename (str): path to the JSON file

        Returns:
            plot_serializer.Plot: Plot object from the JSON file
        """
        with open(filename, "r") as openfile:
            # Reading from json file
            file = json.load(openfile)
        plot = Plot()
        plot.axes = []
        for axis_object in file["axes"]:
            axis = Axis()
            axis.traces = []
            for trace_object in axis_object["traces"]:
                plotted_element = Trace()
                axis.traces.append(self.dict_to_object(trace_object, plotted_element))
            plot.axes.append(axis)
        return plot

    def dict_to_object(self: Self, dictonary: Dict[str, Any], object: _T) -> _T:
        for key, value in dictonary.items():
            setattr(object, key, value)
        return object

    def json_to_matplotlib(self: Self, json_file: str) -> MplFigure:
        """Converts the Plot objects from JSON to matplotlib.pyplot.

        Args:
            json_file (str): path to the JSON file

        Returns:
            matplotlib.pyplot.Figure: matplotlib.pyplot.Figure created from the JSON file
        """
        self.plot = self.from_json(json_file)
        fig = plt.figure()
        for axis in self.plot.axes:
            ax = fig.add_subplot()
            for t in axis.traces:
                ax.plot(t.xdata, t.ydata, label=t.label, color=t.color)
        return fig
