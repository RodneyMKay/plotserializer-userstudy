import matplotlib
import json
from plot_serializer.adapters import Plot, MatplotlibAdapter


class Serializer:
    def __init__(self, p) -> None:
        self._plot = None
        self.plot = self.convert_plot(p)
        pass

    @property
    def plot(self):
        return self._plot

    @plot.setter
    def plot(self, plot):
        if not issubclass(type(plot), Plot):
            raise TypeError("plot must be a subclass of plot_serializer.adapters.Plot")
        else:
            self._plot = plot

    def convert_plot(self, p) -> Plot:
        if isinstance(p, matplotlib.pyplot.Figure):
            converted_plot = MatplotlibAdapter(p)
        else:
            raise NotImplementedError(
                "Only matplotlib is implemented. Make sure you submit a matplotlib.pyplot.Figure object."
            )
        return converted_plot

    def to_json(self) -> str:
        return json.dumps(self.plot, default=lambda o: getattr(o, "__dict__", str(o)))

