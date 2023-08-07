from typing import Union


class Plot:
    def __init__(self) -> None:
        # self._axes = None
        pass


class Axis:
    def __init__(self) -> None:
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
        if type(data) != list:
            raise TypeError("xdata must be a list.")
        if self.ydata is not None and len(data) != len(self.ydata):
            raise RuntimeError("Length of xdata and ydata differs.")
        self._xdata = data

    @property
    def ydata(self):
        return self._ydata

    @ydata.setter
    def ydata(self, data):
        if type(data) != list:
            raise TypeError("ydata must be a list.")
        if self.xdata is not None and len(data) != len(self.xdata):
            raise RuntimeError("Length of xdata and ydata differs.")
        self._ydata = data

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        if type(label) != str:
            raise TypeError("label must be a string.")
        self._label = label


class MatplotlibAdapter(Plot):
    def __init__(self, fig) -> None:
        super().__init__()
        self.axes = self.get_axes(fig)
        pass

    def get_axes(self, fig):
        axes = []
        for axis in fig.axes:
            a = Axis()
            a.plotted_elements = self.get_plotted_elements(axis)
            axes.append(a)
        return axes

    def get_plotted_elements(self, axis):
        lines = self.get_lines(axis)
        # collections = self.get_collections()
        return lines

    def get_lines(self, axis):
        lines = []
        if len(axis.lines) > 0:
            for line in axis.lines:
                pe = PlottedElement()
                pe.xdata = list(line.get_xdata())
                pe.ydata = list(line.get_ydata())
                pe.label = line.get_label()
                pe.type = type(line)
                lines.append(pe)
        return lines
