from typing import Annotated, Dict, List, Literal, Optional, Union
from pydantic import BaseModel, Field


# --------------------
#  General classes


Scale = Union[Literal["linear"], Literal["logarithmic"]]


class Axis(BaseModel):
    label: Optional[str] = None
    scale: Optional[Scale] = None  # Defaults to linear


MetadataValue = Union[int, float, str]
Metadata = Dict[str, MetadataValue]


# --------------------
#  2D Plot


class Point2D(BaseModel):
    x: float
    y: float
    color: Optional[str] = None
    size: Optional[float] = None


class ScatterTrace2D(BaseModel):
    type: Literal["scatter"]
    datapoints: List[Point2D]


class LineTrace2D(BaseModel):
    type: Literal["line"]
    line_color: Optional[str] = None
    line_thickness: Optional[float] = None
    line_style: Optional[str] = None
    label: Optional[str] = None
    datapoints: List[Point2D]


class Bar2D(BaseModel):
    y: float
    label: str
    color: Optional[str] = None


class BarTrace2D(BaseModel):
    type: Literal["bar"]
    datapoints: List[Bar2D]


Trace2D = Annotated[
    Union[ScatterTrace2D, LineTrace2D, BarTrace2D], Field(discriminator="type")
]


class Plot2D(BaseModel):
    type: Literal["2d"]
    title: Optional[str] = None
    x_axis: Axis
    y_axis: Axis
    traces: List[Trace2D]


# --------------------
#  Pie Plot


class Slice(BaseModel):
    size: float
    radius: Optional[float] = None
    offset: Optional[float] = None
    name: Optional[str] = None
    color: Optional[str] = None


class PiePlot(BaseModel):
    type: Literal["pie"]
    title: Optional[str] = None
    slices: List[Slice]


# --------------------
#  Figure


Plot = Annotated[Union[PiePlot, Plot2D], Field(discriminator="type")]


class Figure(BaseModel):
    title: Optional[str] = None
    plots: List[Plot] = []
    metadata: Metadata = {}
