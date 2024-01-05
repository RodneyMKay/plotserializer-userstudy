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


# --------------------
#  2D Plot


class Point(BaseModel):
    position: Vec2F
    color: Optional[str]
    size: Optional[float]


class Line(BaseModel):
    datapoints: List[Point]
    color: Optional[str]
    thickness: Optional[float]


class Axis(BaseModel):
    unit: str


class Plot2D(BaseModel):
    type: Literal["2d"]
    x_axis: Axis
    y_axis: Axis
    lines: List[Line]
    points: List[Point]


# --------------------
#  Pie Plot


class Slice(BaseModel):
    size: float
    name: str
    color: Optional[str]


class PiePlot(BaseModel):
    type: Literal["pie"]
    slice: List[Slice]


# --------------------
#  Figure

Plot = Annotated[Union[PiePlot, Plot2D], Field(descriminator="type")]


class Figure(BaseModel):
    plots: List[Plot]
