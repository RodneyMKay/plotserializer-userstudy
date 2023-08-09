import matplotlib
import json
import inspect
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
        return json.dumps(self.plot, default=lambda o: self._getattrorprop(o))

    def _getattrorprop(self, o):
        d = dict(
            (k, v)
            for k, v in inspect.getmembers(o)
            if not k.startswith("_")
            and not inspect.ismethod(v)
            and not inspect.isfunction(v)
        )
        return d
