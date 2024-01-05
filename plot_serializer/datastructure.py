from typing import List, Type, Tuple
from typing_extensions import Self

from pydantic import BaseModel
from abc import ABC

# TODO: Name stuff better


class StylingABC(BaseModel, ABC):
    pass


class AxisStyling(StylingABC):
    pass


class DataStyling(StylingABC):
    pass


class CanvasStyling(StylingABC):
    pass


class MPLLineDataStyling(DataStyling):
    type: Type
    label: str | None
    color: str | None


class MPLAxisStyling(AxisStyling):
    pass


class MPLCanvasStyling(CanvasStyling):
    titel: str | None
    legend: bool
    # TODO grid, spines ...


class DataPoint(BaseModel):
    # TODO can be Tuple
    values: Tuple


class Units(BaseModel):
    # TODO can be Tuple
    units: Tuple | None


class DataCollection(BaseModel):
    units: Units
    data: List[DataPoint]
    styling: DataStyling


class Axis(BaseModel):
    label: str
    pass


# equivalent to one subplot
class Plot(BaseModel):
    title: str | None
    axes: List[Axis]

    # TODO: Naming [graph | graphdata, data | dataCollection, plot | plotData] ???
    graphs: List[DataCollection]

    def get_axis_dimentions(self: Self):
        return len(self.axes)


# equivalent to Figure
# ???: Even needed?
class Canvas(BaseModel):
    plots: List[Plot]
    styling: CanvasStyling | None
