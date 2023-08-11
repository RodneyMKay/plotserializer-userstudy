class Plot:
    # __slots__ = ["_id", "_axes", "_title", "_caption"]
    def __init__(self) -> None:
        self._id = None
        self._axes = None
        self._title = None
        self._caption = None
        pass

    @property
    def axes(self):
        return self._axes

    @axes.setter
    def axes(self, axes):
        self._axes = axes

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if type(id) is str:
            self._id = id
        else:
            raise TypeError("id must be a string.")


class Axis:
    def __init__(self) -> None:
        self._plotted_elements = None
        self._title = None
        self._xlabel = None
        self._ylabel = None
        self._xquantity = None
        self._yquantity = None
        self._xunit = None
        self._yunit = None
        pass


class PlottedElement:
    def __init__(self) -> None:
        self._xdata = None
        self._ydata = None
        self._label = None
        self._type = None

    @property
    def xdata(self):
        return self._xdata

    @xdata.setter
    def xdata(self, data):
        if type(data) is not list:
            raise TypeError("xdata must be a list.")
        if self.ydata is not None and len(data) != len(self.ydata):
            raise RuntimeError("Length of xdata and ydata differs.")
        self._xdata = data

    @property
    def ydata(self):
        return self._ydata

    @ydata.setter
    def ydata(self, data):
        if type(data) is not list:
            raise TypeError("ydata must be a list.")
        if self.xdata is not None and len(data) != len(self.xdata):
            raise RuntimeError("Length of xdata and ydata differs.")
        self._ydata = data

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        if type(label) is not str:
            raise TypeError("label must be a string.")
        self._label = label
