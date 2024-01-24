import json
from plot_serializer.matplotlib.collector import MatplotlibCollector
from tests import read_plot


def test_simple() -> None:
    collector = MatplotlibCollector()

    names = ["a", "b", "c", "d", "e", "f", "g", "h"]
    heights = [10, 20, 30, 40, 50, 60, 70, 80]

    _, ax = collector.subplots()
    ax.bar(names, heights)

    json_string = collector.json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("bar_plot_simple"))

    assert output == expected


def test_all_features() -> None:
    collector = MatplotlibCollector()

    names = ["a", "b", "c", "d", "e", "f", "g", "h"]
    heights = [10, 20, 30, 40, 50, 60, 70, 80]
    color = ["red", "green", "blue", "orange", "purple", "cyan", "blue", "blue"]

    _, ax = collector.subplots()
    ax.bar(names, heights, color=color)
    ax.set_title("My amazing bar plot")

    ax.set_yscale("log")
    ax.set_ylabel("log axis")

    json_string = collector.json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("bar_plot_all_features"))

    assert output == expected
