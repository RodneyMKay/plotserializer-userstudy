import json
from typing import Any
import numpy as np
from plot_serializer.matplotlib.collector import MatplotlibCollector
from tests import read_plot


def test_simple() -> None:
    collector = MatplotlibCollector()

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [10, 20, 30, 40, 50, 60, 70, 70, 90, 100]

    _, ax = collector.subplots()
    ax.plot(x, y)

    json_string = collector.json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("line_plot_simple"))

    assert output == expected


def func(x: Any, d: float) -> Any:
    return 1 / (np.sqrt((1 - x**2) ** 2 + (2 * x * d)))


def test_all_features() -> None:
    collector = MatplotlibCollector()
    x = np.linspace(0, 3, 500)

    e = func(x, 0)
    y = func(x, 0.1)
    y2 = func(x, 0.2)
    y3 = func(x, 0.5)
    y4 = func(x, 1)

    _, ax = collector.subplots()
    ax.plot(x, e, label="Einhüllend", linestyle="--", color="gray")
    ax.plot(x, y, label="D = 0.1")
    ax.plot(x, y2, label="D = 0.2")
    ax.plot(x, y3, label="D = 0.5")
    ax.plot(x, y4, label="D = 1")

    ax.legend()
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_xlabel(r"$\omega/\omega_0$")
    ax.set_ylabel("$A/A_E$")
    ax.grid(True)
    ax.set_title("Ressonanz")

    json_string = collector.json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("line_plot_all_features"))

    assert output == expected
