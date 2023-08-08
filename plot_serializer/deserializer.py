import json
import matplotlib.pyplot as plt

from plot_serializer.plot import Plot, Axis, PlottedElement


class Deserializer:
    def __init__(self) -> None:
        self._plot = None
        pass

    def from_json(self, filename):
        with open(filename, 'r') as openfile:
            # Reading from json file
            d = json.load(openfile)
        p = Plot()
        p.axes = []
        for a in d["axes"]:
            axis = Axis()
            axis.plotted_elements = []
            for pe in a["plotted_elements"]:
                plotted_element = PlottedElement()
                axis.plotted_elements.append(self.dict_to_object(pe, plotted_element))
            p.axes.append(axis)
        return p
        pass

    def dict_to_object(self, d, o):
        for key, value in d.items():
            setattr(o, key, value)
        return o

    def json_to_matplotlib(self, json_file):
        self.plot = self.from_json(json_file)
        fig = plt.figure()
        for axis in self.plot.axes:
            ax = fig.add_subplot()
            for pe in axis.plotted_elements:
                ax.plot(pe.xdata, pe.ydata, label=pe.label)
        return fig