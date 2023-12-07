from typing import Any, Dict, List
from typing_extensions import Self
import json
import inspect
import warnings
from collections import OrderedDict
from plot_serializer.adapters import MatplotlibAdapter
from plot_serializer.exceptions import OntologyWarning
from plot_serializer.plot import Plot, Axis, Trace
from matplotlib.figure import Figure as MplFigure


SerializablePlotType = MplFigure
_CustomMetadataApplicable = Plot | Axis | Trace


class Serializer:
    def __init__(
        self: Self,
        plot: SerializablePlotType | None = None,
        suppress_ontology_warnings: bool = False,
    ) -> None:
        self._plot: None | Plot = None
        self._axis: None | List[Axis] = None

        if plot is not None:
            self.load_plot(plot)

        if suppress_ontology_warnings is True:
            warnings.filterwarnings(action="ignore", category=OntologyWarning)

    @property
    def plot(self: Self) -> Plot | None:
        return self._plot

    @plot.setter
    def plot(self: Self, plot: Plot) -> None:
        if not issubclass(type(plot), Plot):
            raise TypeError("plot must be a subclass of plot_serializer.adapters.Plot")
        else:
            self._plot = plot

    @property
    def axis(self: Self) -> List[Axis] | None:
        return self._axis

    @axis.setter
    def axis(self: Self, axis: List[Axis]) -> None:
        self._axis = axis

    def load_plot(self: Self, plot: SerializablePlotType) -> None:
        if isinstance(plot, MplFigure):
            self.plot = MatplotlibAdapter(plot)
            self.axis = MatplotlibAdapter(plot).get_axes(plot)
        else:
            raise NotImplementedError(
                "Only matplotlib is implemented. Make sure you submit a matplotlib.pyplot.Figure object."
            )

    def to_json(self: Self, header: List[str] = ["id"]) -> str:
        """Exports plot to json.

        Args:
            header (list, optional): list of keys to appear on top of the json string. Defaults to ["id"].

        Returns:
            str: json string
        """
        d = json.loads(
            json.dumps(
                self.plot, default=lambda o: self._get_attributes_and_properties_of(o)
            )
        )
        od = OrderedDict()
        for k in header:
            od[k] = d[k]
        for k in set(d.keys()) - set(header):
            od[k] = d[k]
        return json.dumps(od)

    def add_plot_metadata(
        self: Self,
        id: str | None = None,
        title: str | None = None,
        caption: str | None = None,
    ) -> None:
        """Adds plot metadata to the plot object.

        Args:
            id (str, optional): the id of plot. Defaults to None.
            title (str, optional): the title of plot. Defaults to None.
            caption (str, optional): the caption of plot. Defaults to None.
        """
        plot = self.plot

        if plot is None:
            raise ValueError("A plot to add metadata to, is required!")

        plot.add_plot_metadata(title, id, caption)

    def add_axis_metadata(
        self: Self,
        axis_index: int,
        title: str,
        xlabel: str,
        ylabel: str,
        xunit: str | None = None,
        yunit: str | None = None,
        xquantity: str | None = None,
        yquantity: str | None = None,
    ) -> None:
        """Adds axis metadata to the axis selected by index

        Args:
            axis_index (int): the index of subplot
            title (str): the title of subplot
            xlabel (str): the label of x-axis
            ylabel (str): the label of y-axis
            xunit (str, optional): the unit of x-axis. Defaults to None.
            yunit (str, optional): the unit of y-axis. Defaults to None.
            xquantity (str, optional): the quantity of x-axis. Defaults to None.
            yquantity (str, optional): the quantity of y-axis. Defaults to None.
        """
        plot = self.plot

        if plot is None:
            raise ValueError("Plot cannot be None!")

        # TODO: überprüfen die anzhal des subplots
        plot.axes[axis_index].title = title
        plot.axes[axis_index].xlabel = xlabel
        plot.axes[axis_index].ylabel = ylabel
        plot.axes[axis_index].xunit = xunit
        plot.axes[axis_index].yunit = yunit
        plot.axes[axis_index].xquantity = xquantity
        plot.axes[axis_index].yquantity = yquantity

    def add_custom_metadata(
        self: Self, metadata_dict: Dict[str, str], obj: _CustomMetadataApplicable
    ) -> _CustomMetadataApplicable:
        """Adds custom metadata to a specified object.

        Args:
            metadata_dict (dict): dictionary that contains metadata to add
            obj (plot_serializer.plot.Plot | plot_serializer.plot.Axis |
                plot_serializer.plot.Trace): Plot, Axis, or Trace
                assigned to Serializer

        Raises:
            ValueError: obj must be the plot or its attributes assigned to the
                Serializer function

        Returns:
            plot_serializer.plot.Plot |
            plot_serializer.plot.Axis |
            plot_serializer.plot.Trace: obj including metadata
        """
        plot = self.plot

        if plot is None:
            raise ValueError("Plot must not be null!")

        if obj in [
            plot,
            *plot.axes,
            *[t for a in plot.axes for t in a.traces],
        ]:
            for k, v in metadata_dict.items():
                setattr(obj, k, v)
            return obj
        else:
            raise ValueError(
                "obj must be the plot or its attributes assigned to the Serializer function"
            )

    def _get_attributes_and_properties_of(
        self: Self, object: Any
    ) -> Dict[str, Any]:  # TODO: Sepcify this further
        return dict(
            (name, member)
            for name, member in inspect.getmembers(object)
            if not name.startswith("_")
            and not inspect.ismethod(member)
            and not inspect.isfunction(member)
        )
