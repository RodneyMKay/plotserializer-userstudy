import matplotlib
import json
import inspect
from collections import OrderedDict
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

    def to_json(self, header=["id"]) -> str:
        d = json.loads(json.dumps(self.plot, default=lambda o: self._getattrorprop(o)))
        od = OrderedDict()
        for k in header:
            od[k] = d[k]
        for k in set(d.keys()) - set(header):
            od[k] = d[k]
        return json.dumps(od)

    def add_id(self, id) -> None:
        self.plot.id = id

    def add_custom_metadata(self, metadata_dict: dict) -> None:
        for k, v in metadata_dict.items():
            setattr(self.plot, k, v)

    def _getattrorprop(self, o):
        d = dict(
            (k, v)
            for k, v in inspect.getmembers(o)
            if not k.startswith("_")
            and not inspect.ismethod(v)
            and not inspect.isfunction(v)
        )
        return d
