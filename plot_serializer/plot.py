from typing import Dict, List
from typing_extensions import Self


class Trace:
    def __init__(self: Self) -> None:
        self._xdata: List[int] | None = None
        self._ydata: List[int] | None = None
        self._label: str | None = None
        self._type: str | None = None
        self._color: str | None = None

    @property
    def xdata(self) -> List[int] | None:
        return self._xdata

    @xdata.setter
    def xdata(self: Self, data: List[int]) -> None:
        if not isinstance(data, list):
            raise TypeError("xdata must be a list.")

        if self.ydata is not None and len(data) != len(self.ydata):
            print(f">>> XDATA: {self.xdata}")
            print(f">>> YDATA: {self.ydata}")
            raise RuntimeError("Length of xdata and ydata differs.")

        self._xdata = data

    @property
    def ydata(self: Self) -> List[int] | None:
        return self._ydata

    @ydata.setter
    def ydata(self: Self, data: List[int]) -> None:
        if not isinstance(data, list):
            raise TypeError("ydata must be a list.")

        if self.xdata is not None and len(data) != len(self.xdata):
            raise RuntimeError("Length of xdata and ydata differs.")

        self._ydata = data

    @property
    def label(self: Self) -> str | None:
        return self._label

    @label.setter
    def label(self, label: str) -> None:
        if not isinstance(label, str):
            raise TypeError("label must be a string.")

        self._label = label

    @property
    def type(self: Self) -> str | None:
        return self._type

    @type.setter
    def type(self: Self, type: str) -> None:
        if not isinstance(type, str):
            raise TypeError("type must be a string.")

        self._type = type

    @property
    def color(self: Self) -> str | None:
        return self._color

    @color.setter
    def color(self: Self, color: str) -> None:
        if not isinstance(color, str):
            raise TypeError("color must be a string")

        self._color = color


class Axis:
    def __init__(self: Self, unit_ontology: str = "default") -> None:
        self._traces: List[Trace] = list()
        self._title: str | None = None
        self._xlabel: str | None = None
        self._ylabel: str | None = None
        self._xquantity: str | None = None
        self._yquantity: str | None = None
        self._xunit: str | None = None
        self._yunit: str | None = None
        self.unit_ontology: str = unit_ontology

    @property
    def traces(self: Self) -> List[Trace]:
        return self._traces

    @traces.setter
    def traces(self, trace_list: List[Trace]) -> None:
        if not all(isinstance(p, Trace) for p in trace_list):
            raise TypeError("Must be a list of instances of Trace.")
        self._traces = trace_list

    @property
    def title(self: Self) -> str | None:
        return self._title

    @title.setter
    def title(self: Self, title: str) -> None:
        if not isinstance(title, str):
            raise TypeError("title must be a string.")
        self._title = title

    @property
    def xlabel(self: Self) -> str | None:
        return self._xlabel

    @xlabel.setter
    def xlabel(self: Self, xlabel: str) -> None:
        if not isinstance(xlabel, str):
            raise TypeError("xlabel must be a string.")

        self._xlabel = xlabel

    @property
    def ylabel(self: Self) -> str | None:
        return self._ylabel

    @ylabel.setter
    def ylabel(self: Self, ylabel: str) -> None:
        if not isinstance(ylabel, str):
            raise TypeError("ylabel must be a string.")

        self._ylabel = ylabel

    @property
    def xquantity(self: Self) -> str | None:
        return self._xquantity

    @xquantity.setter
    def xquantity(self: Self, xquantity: str | None) -> None:
        if (not isinstance(xquantity, str)) and (xquantity is not None):
            raise TypeError("xquantity must be a string or None.")

        self._xquantity = xquantity

    @property
    def yquantity(self: Self) -> str | None:
        return self._yquantity

    @yquantity.setter
    def yquantity(self: Self, yquantity: str | None) -> None:
        if (not isinstance(yquantity, str)) and (yquantity is not None):
            raise TypeError("yquantity must be a string or None.")

        self._yquantity = yquantity

    @property
    def xunit(self: Self) -> str | None:
        return self._xunit

    @xunit.setter
    def xunit(self: Self, xunit: str | None) -> None:
        if (not isinstance(xunit, str)) and (xunit is not None):
            raise TypeError("xunit must be a string or None.")

        # if not unit_in_ontology(xunit, self.unit_ontology):
        #     warn(
        #         "Unit {} is not in the selected ontology.".format(xunit),
        #         OntologyWarning,
        #     )
        self._xunit = xunit

    @property
    def yunit(self) -> str | None:
        return self._yunit

    @yunit.setter
    def yunit(self: Self, yunit: str | None) -> None:
        if (not isinstance(yunit, str)) and (yunit is not None):
            raise TypeError("yunit must be a string or None.")

        # if not unit_in_ontology(yunit, self.unit_ontology):
        #     warn(
        #         "Unit {} is not in the selected ontology.".format(yunit),
        #         OntologyWarning,
        #     )
        self._yunit = yunit


class Dataset:
    def __init__(self: Self) -> None:
        self._URL = None
        self._file_name = None


class Plot:
    # __slots__ = ["_id", "_axes", "_title", "_caption"]
    def __init__(self: Self) -> None:
        self._id: str | None = None
        self._axes: List[Axis] = list()
        self._title: str | None = None
        self._caption: str | None = None
        self._dataset = None

    @property
    def axes(self: Self) -> List[Axis]:
        return self._axes

    @axes.setter
    def axes(self: Self, axes: List[Axis]) -> None:
        self._axes = axes

    @property
    def id(self: Self) -> str | None:
        return self._id

    @id.setter
    def id(self: Self, id: str) -> None:
        if not isinstance(id, str):
            raise TypeError("id must be a string.")

        self._id = id

    def add_plot_metadata(
        self: Self, title: str | None, id: str | None, caption: str | None
    ) -> None:
        self._id = id
        self._title = title
        self._caption = caption

    def add_custom_metadata(self: Self, metadata_dict: Dict[str, str]) -> None:
        for k, v in metadata_dict.items():
            # FIXME: We are a plot! Why do we set metadata at self.plot?!
            setattr(self.plot, k, v)
