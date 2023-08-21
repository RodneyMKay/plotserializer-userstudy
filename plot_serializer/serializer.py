import matplotlib
import json
import inspect
from collections import OrderedDict
from plot_serializer.adapters import Plot, MatplotlibAdapter


class Serializer:
    def __init__(self, p=None) -> None:
        self._plot = None
        if p is not None:
            self.load_plot(p)
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

    def load_plot(self, p) -> None:
        if isinstance(p, matplotlib.pyplot.Figure):
            self.plot = MatplotlibAdapter(p)
        else:
            raise NotImplementedError(
                "Only matplotlib is implemented. Make sure you submit a matplotlib.pyplot.Figure object."
            )

    def to_json(self, header=["id"]) -> str:
        """Exports plot to json.

        Args:
            header (list, optional): list of keys to appear on top of the json string. Defaults to ["id"].

        Returns:
            str: json string
        """
        d = json.loads(json.dumps(self.plot, default=lambda o: self._getattrorprop(o)))
        od = OrderedDict()
        for k in header:
            od[k] = d[k]
        for k in set(d.keys()) - set(header):
            od[k] = d[k]
        return json.dumps(od)

    def add_plot_metadata(self, title=None, id=None, caption=None):
        pass

    def add_axis_metadata(self, axis, xunit, yunit):
        pass

    def add_custom_metadata(self, metadata_dict: dict, obj) -> None:
        if obj in [
            self.plot,
            *self.plot.axes,
            *[p for a in self.plot.axes for p in a.plotted_elements],
        ]:
            for k, v in metadata_dict.items():
                setattr(obj, k, v)
            return obj
        else:
            raise ValueError(
                "obj must be the plot or its attributes assigned to the Serializer function"
            )

    def _getattrorprop(self, o):
        d = dict(
            (k, v)
            for k, v in inspect.getmembers(o)
            if not k.startswith("_")
            and not inspect.ismethod(v)
            and not inspect.isfunction(v)
        )
        return d
