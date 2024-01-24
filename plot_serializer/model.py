from typing import Annotated, Dict, List, Literal, Optional, Union
from pydantic import BaseModel, Field


# --------------------
#  Vectors


class Vec2F(BaseModel):
    x: float
    y: float


class Vec3F(BaseModel):
    x: float
    y: float
    z: float


class Vec4F(BaseModel):
    x: float
    y: float
    z: float
    w: float


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
    position: Vec2F
    color: Optional[str] = None
    size: Optional[float] = None


class Line(BaseModel):
    color: Optional[str] = None
    thickness: Optional[float] = None
    linestyle: Optional[str] = None
    label: Optional[str] = None
    datapoints: List[Vec2F]


class Plot2D(BaseModel):
    type: Literal["2d"]
    title: Optional[str] = None
    x_axis: Axis
    y_axis: Axis
    lines: List[Line]
    points: List[Point2D]


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
# Bar Plot


class Bar(BaseModel):
    name: str
    height: float
    color: Optional[str] = None


class BarPlot(BaseModel):
    type: Literal["bar"]
    title: Optional[str] = None
    y_axis: Axis
    bars: List[Bar]


# --------------------
#  Figure


Plot = Annotated[Union[PiePlot, Plot2D, BarPlot], Field(discriminator="type")]


class Figure(BaseModel):
    title: Optional[str] = None
    plots: List[Plot] = []
    metadata: Metadata = {}
