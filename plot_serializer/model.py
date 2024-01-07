from math import degrees, radians
from typing import Annotated, List, Literal, Optional, Union
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
#  2D Plot


class Point2D(BaseModel):
    position: Vec2F
    color: Optional[str] = None
    size: Optional[float] = None


class Line(BaseModel):
    datapoints: List[Point2D]
    color: Optional[str] = None
    thickness: Optional[float] = None
    linestyle: Optional[str] = None


class Axis(BaseModel):
    unit: str
    label: Optional[str] = None
    scale: Optional[str] = None
    show: bool = True


class Plot2D(BaseModel):
    type: Literal["2d"]
    title: Optional[str]
    x_axis: Axis
    y_axis: Axis
    lines: List[Line]
    points: List[Point2D]


# --------------------
#  Pie Plot


class Slice(BaseModel):
    # size = f in [0 - 360]
    degrees: float
    height: Optional[float]
    name: Optional[str]
    color: Optional[str]


class PiePlot(BaseModel):
    """order der slices ist order der Liste"""

    type: Literal["pie"]
    title: Optional[str]
    slice: List[Slice]


# --------------------
# Bar Plot


class Bar(BaseModel):
    position: float
    height: float
    width: float


class BarPlot(BaseModel):
    type: Literal["bar"]
    title: Optional[str]
    bars: List[Bar]


# --------------------
#  Figure

Plot = Annotated[Union[PiePlot, Plot2D, BarPlot], Field(descriminator="type")]


class Figure(BaseModel):
    title: Optional[str] = None
    plots: List[Plot] = []
