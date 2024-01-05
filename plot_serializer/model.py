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
    x1: float
    x2: float
    x3: float
    x4: float


# --------------------
#  2D Plot


class Point2D(BaseModel):
    position: Vec2F
    color: Union[int, str, None]
    size: Optional[float]


class Line(BaseModel):
    datapoints: List[Point2D]
    color: Union[int, str, None]
    thickness: Optional[float]
    linestyle: Optional[str]


class Axis(BaseModel):
    label: Optional[str]
    unit: str
    scale: Optional[str]


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
    size: float
    name: str
    color: Optional[str]


class PiePlot(BaseModel):
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
    title: Optional[str]
    plots: List[Plot]
