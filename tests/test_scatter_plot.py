import json
from plot_serializer.matplotlib.serializer import MatplotlibSerializer
from tests import read_plot


def test_simple() -> None:
    serializer = MatplotlibSerializer()

    x = [1, 2, 3, 4, 3]
    y = [2, 1.5, 5, 0, 4]

    _, ax = serializer.subplots()
    ax.scatter(x, y)

    json_string = serializer.to_json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("scatter_plot_simple"))

    assert output == expected


def test_sizes() -> None:
    serializer = MatplotlibSerializer()

    x = [1, 2, 3, 4, 3]
    y = [2, 1.5, 5, 0, 4]
    sizes = [1, 5, 10, 20, 30]

    _, ax = serializer.subplots()
    ax.scatter(x, y, s=sizes, enable_sizes=True)

    json_string = serializer.to_json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("scatter_plot_sizes"))

    assert output == expected


def test_sizes_enabled_false() -> None:
    serializer = MatplotlibSerializer()
    x = [1, 2, 3, 4, 3]
    y = [2, 1.5, 5, 0, 4]
    sizes = [1, 5, 10, 20, 30]

    _, ax = serializer.subplots()
    ax.scatter(x, y, s=sizes, enable_sizes=False)

    json_string = serializer.to_json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("scatter_plot_sizes_disabled"))

    assert output == expected


def test_color_list_string() -> None:
    serializer = MatplotlibSerializer()

    x = [1, 2, 3, 4, 3]
    y = [2, 1.5, 5, 0, 4]
    color = ["green", "blue", "red", "yellow", "black"]
    sizes = [1, 5, 10, 20, 30]

    _, ax = serializer.subplots()
    ax.scatter(x, y, c=color, s=sizes, enable_colors=True)

    json_string = serializer.to_json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("scatter_plot_color"))

    assert output == expected


def test_color_enabled_false() -> None:
    serializer = MatplotlibSerializer()

    x = [1, 2, 3, 4, 3]
    y = [2, 1.5, 5, 0, 4]
    color = [1, 0.5, 3, 0.2, 0.1]
    sizes = [1, 5, 10, 20, 30]

    _, ax = serializer.subplots()
    ax.scatter(x, y, c=color, s=sizes, enable_colors=False, enable_sizes=True)

    json_string = serializer.to_json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("scatter_plot_color_disabled"))

    assert output == expected


def test_all_enabled() -> None:
    serializer = MatplotlibSerializer()

    x = [1, 2, 3, 4, 3]
    y = [2, 1.5, 5, 0, 4]
    color = [1, 0.5, 3, 0.2, 0.1]
    sizes = [1, 5, 10, 20, 30]

    _, ax = serializer.subplots()
    ax.scatter(x, y, c=color, s=sizes, enable_colors=True, enable_sizes=True)

    json_string = serializer.to_json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("scatter_plot_all_enabled"))

    assert output == expected
