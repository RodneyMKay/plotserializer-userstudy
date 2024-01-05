import sys
from typing import Any

from matplotlib import axis
from matplotlib.axes import Axes
from matplotlib.axis import Axis
from matplotlib.collections import PathCollection
from matplotlib.container import BarContainer, ErrorbarContainer
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from matplotlib.path import Path
import matplotlib.pyplot as plt

from plot_serializer.adapter import Adapter
from plot_serializer.adapter.matplotlib import MatplotlibAdapter

import numpy as np

sys.path.append(
    r"C:\Users\Jonas\Code\Uni\BP\repos\plot-serializer.git\new_data_structure"
)
from plot_serializer.datastructure import Canvas
from plot_serializer.adapters import My_New_MatplotlibAdapter


def test_main():
    fig, _ = plot()

    s_fig = My_New_MatplotlibAdapter(fig)
    print(s_fig.model_dump_json())
    # print_axes(fig.axes)

    plt.show()

    # assert false or -s flag
    assert False


def test_plot():
    fig, _ = plot()
    afig = My_New_MatplotlibAdapter(fig)

    plt.show()

    assert False


def print_axes(axes: list[Axes], tab: str = ""):
    print(f"Axes : {axes}")
    index: int = 0

    for axe in axes:
        if not isinstance(axe, Axes):
            print(f"ERROR: {axe} was not of type Axes but of type: {type(axe)}")
            continue

        print(f"-axe[{index}]: {axe}")
        print(f"-axes: {axe.axes}")
        print(f"-title : {axe.get_title()}")
        print(f"-bbox: {axe.bbox}")
        print(f"-images : {axe.images}")
        print(f"-mouse : {axe.mouseover}")
        print(f"-patches : {axe.patches}")
        print(f"-stale : {axe.stale}")
        print(f"-viewlim : {axe.viewLim}")
        print(f"-use edge : {axe.use_sticky_edges}")
        print(f"-text : {axe.texts}")
        print(f"-tables : {axe.tables}")
        print(f"-stick edge : {axe.sticky_edges}")
        print(f"-stale : {axe.stale}")

        # Plot (Lines) | Axes.plot -> List[Line2D]
        print("\n")
        print("---plot data---")
        print(f"-lines: {axe.lines}")
        for line in axe.lines:
            print(f"- -x data: {line.get_xdata()}")
            print(f"- -y data: {line.get_ydata()}")
            print(f"- -lable: {line.get_label()}")
            print(f"- -color: {line.get_color()}")
            print(f"- -line type: {type(line)}")

        # Scatter | Axes.scatter -> PathCollection
        print("\n")
        print("---scatter data---")
        print(f"-collections: {axe.collections}")
        for collection in axe.collections:
            if isinstance(collection, PathCollection):
                # size data for Scatter
                print(f"- -size: {collection.get_sizes()}")
                # x and y data of Scatter
                print(f'- -"offset": {collection.get_offsets()}')
                # get Color information from ScalarMappable
                print(
                    f"- -color: {collection.to_rgba(range(len(collection.get_offsets()) + 1))}"
                )

        # Barchart | Axes.bar -> BarContainer
        # TODO: Error bar also path of the bar container?
        print("\n")
        print("---Barchart---")
        print(f"-containers: {axe.containers}")
        for container in axe.containers:
            if isinstance(container, BarContainer):
                print(f"- -patches: {container.patches}")

                for patch in container.patches:
                    print(f"- -patch: {patch}")

            # TODO
            if isinstance(container, ErrorbarContainer):
                pass

        index = index + 1


def plot() -> tuple[Figure, Any]:
    # make data
    x = np.linspace(0, 10, 100)
    y = 4 + 2 * np.sin(2 * x)

    # plot
    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=2.0, label="my lable")
    ax.legend()

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()

    return (fig, ax)


def plot_easy():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    ax.set_title("Title")
    ax.set_xlabel("my data", fontsize=14, color="red")

    return fig, ax


def plot_test() -> tuple[Figure, Any]:
    np.random.seed(19680801)  # seed the random number generator.

    data = {
        "a": np.arange(50),
        "c": np.random.randint(0, 50, 50),
        "d": np.random.randn(50),
    }

    data["b"] = data["a"] + 10 * np.random.randn(50)
    data["d"] = np.abs(data["d"]) * 100

    fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
    print(f"data: {data}")
    ax.scatter("a", "b", c="c", s="d", data=data)
    ax.set_xlabel("entry a")
    ax.set_ylabel("entry b")

    return (fig, ax)


def plot_bar():
    x = 0.5 + np.arange(8)
    y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

    fig, ax = plt.subplots()

    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.5)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

    return (fig, ax)


def plot_scatter():
    data = {
        "x": np.linspace(0, 10, 10),
        "y": np.linspace(0, 10, 10),
        "c": np.linspace(0, 10, 10),
        "s": np.linspace(0, 10, 10) * 100,
    }

    print(f"data form plot_scatter: {data}")

    fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
    ax.scatter("x", "y", c="c", s="s", data=data)
    ax.set_xlabel("entry x")
    ax.set_ylabel("entry y")

    return (fig, ax)


def plot_2x2():
    fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(3.5, 2.5), layout="constrained")
    # for each Axes, add an artist, in this case a nice label in the middle...
    for row in range(2):
        for col in range(2):
            axs[row, col].annotate(
                f"axs[{row}, {col}]",
                (0.5, 0.5),
                transform=axs[row, col].transAxes,
                ha="center",
                va="center",
                fontsize=18,
                color="darkgrey",
            )
    fig.suptitle("plt.subplots()")

    return fig, axs


if __name__ == "__main__":
    test_main()
