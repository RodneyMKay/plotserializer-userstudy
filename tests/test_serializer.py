import sys
import json
from typing import Any, Dict, List, Tuple
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure as MplFigure
from matplotlib.axes import Axes as MplAxes
import pytest

from plot_serializer.serializer import Serializer


def create_benchmark_plot() -> Tuple[MplFigure, MplAxes]:
    np.random.seed(19680801)

    x = np.linspace(0.5, 3.5, 100)
    y1 = 3 + np.cos(x)
    y2 = 1 + np.cos(1 + x / 0.75) / 2

    fig: MplFigure = plt.figure(figsize=(7.5, 7.5))
    ax = fig.add_axes((0.2, 0.17, 0.68, 0.7), aspect=1)

    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)

    ax.tick_params(which="major", width=1.0, length=10, labelsize=14)
    ax.tick_params(which="minor", width=1.0, length=5, labelsize=10, labelcolor="0.25")

    ax.grid(linestyle="--", linewidth=0.5, color=".25", zorder=-10)

    ax.plot(x, y1, c="C0", lw=2.5, label="Blue signal", zorder=10)
    ax.plot(x, y2, c="C1", lw=2.5, label="Orange signal")
    # ax.scatter(X[::3], Y3[::3], label="scatter")

    ax.set_title("Example figure", fontsize=20, verticalalignment="bottom")
    ax.set_xlabel("TIME in s", fontsize=14)
    ax.set_ylabel("DISTANCE in m", fontsize=14)
    ax.legend(loc="upper right", fontsize=14)
    return fig, ax


def serialize_plot() -> str:
    figure, _ = create_benchmark_plot()
    serializer = Serializer(figure)

    plot = serializer.plot

    if plot is None:
        raise ValueError("Plot should really not be None here.")

    plot.id = "id:ad0cca21"
    plot.axes[0].xunit = "second"
    plot.axes[0].yunit = "blah"
    serializer.add_custom_metadata({"date_created": "11.08.2023"}, plot)
    json_object = serializer.to_json()

    return json_object


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="does not run on linux")
def test_to_json() -> None:
    benchmark_file = open("tests/test_plot.json")
    benchmark_dict = json.load(benchmark_file)

    dict_from_serialized = json.loads(serialize_plot())

    np.testing.assert_array_equal(
        np.array(benchmark_dict.keys()),
        np.array(dict_from_serialized.keys()),
        strict=False,
    )

    assert dict_from_serialized == pytest.approx(benchmark_dict, abs=1e-3)


def test_to_json_linux() -> None:
    benchmark_file = open("tests/test_plot.json")
    benchmark_dict = json.load(benchmark_file)

    dict_from_serialized = json.loads(serialize_plot())

    np.testing.assert_array_equal(
        np.array(benchmark_dict.keys()),
        np.array(dict_from_serialized.keys()),
        strict=False,
    )
    for key, value in dict_from_serialized.items():
        assert _recursive_search(value, benchmark_dict[key])


def _recursive_search(first: object, second: object) -> bool:
    if isinstance(first, dict) and isinstance(second, dict):
        return _nested_dict_search(first, second)

    if isinstance(first, list) and isinstance(second, list):
        return _list_search(first, second)

    return first == second


def _nested_dict_search(first: Dict[Any, Any], second: Dict[Any, Any]) -> bool:
    bool_list = []
    for key, value in first.items():
        if isinstance(value, dict):
            bool_list.append(_recursive_search(value, second[key]))
        elif isinstance(value, list):
            bool_list.append(_list_search(value, second[key]))
        else:
            try:
                bool_list.append(np.allclose(value, second[key]))
            except (TypeError, np.exceptions.DTypePromotionError):
                bool_list.append(value == second[key])
    return all(bool_list)


def _list_search(first: List[Any], second: List[Any]) -> bool:
    bool_list = []
    for index, item in enumerate(first):
        if isinstance(item, dict):
            bool_list.append(_nested_dict_search(item, second[index]))
        else:
            try:
                bool_list.append(np.allclose(item, second[index]))
            except (TypeError, np.exceptions.DTypePromotionError):
                bool_list.append(item == second[index])
    return all(bool_list)
