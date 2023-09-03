import json
import matplotlib.pyplot as plt

from plot_serializer.plot import Plot, Axis, Trace


class Deserializer:
    def __init__(self) -> None:
        self._plot = None
        pass

    def from_json(self, filename):
        with open(filename, "r") as openfile:
            # Reading from json file
            d = json.load(openfile)
        p = Plot()
        p.axes = []
        for a in d["axes"]:
            axis = Axis()
            axis.xlabel = a["xlabel"]
            axis.ylabel = a["ylabel"]
            axis.traces = []
            for t in a["traces"]:
                plotted_element = Trace()
                axis.traces.append(self.dict_to_object(t, plotted_element))
            p.axes.append(axis)
        return p

    def dict_to_object(self, d, o):
        for key, value in d.items():
            setattr(o, key, value)
        return o

    def json_to_matplotlib(self, json_file):
        self.plot = self.from_json(json_file)
        fig = plt.figure()
        for axis in self.plot.axes:
            ax = fig.add_subplot()
            ax.set_xlabel(axis.xlabel)
            ax.set_ylabel(axis.ylabel)
            for t in axis.traces:
                ax.plot(t.xdata, t.ydata, label=t.label, color=t.color)
        return fig
