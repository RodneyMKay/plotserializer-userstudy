import json
from plot_serializer.matplotlib.serializer import MatplotlibSerializer
from tests import read_plot
from mpl_toolkits.mplot3d.axes3d import Axes3D as MplAxes3D
from plot_serializer.matplotlib.serializer import _AxesProxy3D


def test_simple() -> None:
    serializer = MatplotlibSerializer()

    x = [1, 2, 3, 4, 3]
    y = [2, 1.5, 5, 0, 4]
    z = [3, 2, 1, 0.5, 2]

    __, ax = serializer.subplots(subplot_kw={"projection": "3d"})
    assert isinstance(ax.delegate, MplAxes3D)
    assert isinstance(ax, _AxesProxy3D)
    ax.scatter(x, y, z)

    json_string = serializer.to_json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("scatter3D_plot_simple"))

    assert output == expected


def test_size() -> None:
    serializer = MatplotlibSerializer()

    x = [1, 2, 3, 4, 3]
    y = [2, 1.5, 5, 0, 4]
    z = [3, 2, 1, 0.5, 2]
    sizes = 5

    __, ax = serializer.subplots(subplot_kw={"projection": "3d"})
    assert isinstance(ax.delegate, MplAxes3D)
    assert isinstance(ax, _AxesProxy3D)
    ax.scatter(x, y, z, s=sizes, enable_sizes=True)

    json_string = serializer.to_json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("scatter3D_plot_size"))

    assert output == expected


def test_sizes_list() -> None:
    serializer = MatplotlibSerializer()

    x = [1, 2, 3, 4, 3]
    y = [2, 1.5, 5, 0, 4]
    z = [3, 2, 1, 0.5, 2]
    sizes = [1, 5, 10, 20, 30]

    __, ax = serializer.subplots(subplot_kw={"projection": "3d"})
    assert isinstance(ax.delegate, MplAxes3D)
    assert isinstance(ax, _AxesProxy3D)
    ax.scatter(x, y, z, s=sizes, enable_sizes=True)

    json_string = serializer.to_json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("scatter3D_plot_size_list"))

    assert output == expected


def test_color_string() -> None:
    serializer = MatplotlibSerializer()

    x = [1, 2, 3, 4, 3]
    y = [2, 1.5, 5, 0, 4]
    z = [3, 2, 1, 0.5, 2]
    color = "green"

    __, ax = serializer.subplots(subplot_kw={"projection": "3d"})
    assert isinstance(ax.delegate, MplAxes3D)
    assert isinstance(ax, _AxesProxy3D)
    ax.scatter(x, y, z, c=color, enable_colors=True)

    json_string = serializer.to_json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("scatter3D_plot_color_string"))

    assert output == expected


def test_color_list_string() -> None:
    serializer = MatplotlibSerializer()

    x = [1, 2, 3, 4, 3]
    y = [2, 1.5, 5, 0, 4]
    z = [3, 2, 1, 0.5, 2]
    color = ["green", "blue", "red", "yellow", "black"]

    __, ax = serializer.subplots(subplot_kw={"projection": "3d"})
    assert isinstance(ax.delegate, MplAxes3D)
    assert isinstance(ax, _AxesProxy3D)
    ax.scatter(x, y, z, c=color, enable_colors=True)

    json_string = serializer.to_json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("scatter3D_plot_color_string_list"))

    assert output == expected


def test_color_hex() -> None:
    serializer = MatplotlibSerializer()

    x = [1, 2, 3, 4, 3]
    y = [2, 1.5, 5, 0, 4]
    z = [3, 2, 1, 0.5, 2]
    color = ["#008000ff", "#0000ffff", "#ff0000ff", "#ffff00ff", "#000000ff"]

    __, ax = serializer.subplots(subplot_kw={"projection": "3d"})
    assert isinstance(ax.delegate, MplAxes3D)
    assert isinstance(ax, _AxesProxy3D)
    ax.scatter(x, y, z, c=color, enable_colors=True)

    json_string = serializer.to_json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("scatter3D_plot_color_hex"))

    assert output == expected


def test_color_rgb() -> None:
    serializer = MatplotlibSerializer()

    x = [1, 2, 3, 4, 3]
    y = [2, 1.5, 5, 0, 4]
    z = [3, 2, 1, 0.5, 2]
    color = [
        (0.0, 0.5019607843137255, 0.0),
        (0.0, 0.0, 1.0),
        (1.0, 0.0, 0.0),
        (1.0, 1.0, 0.0),
        (0.0, 0.0, 0.0),
    ]

    __, ax = serializer.subplots(subplot_kw={"projection": "3d"})
    assert isinstance(ax.delegate, MplAxes3D)
    assert isinstance(ax, _AxesProxy3D)
    ax.scatter(x, y, z, c=color, enable_colors=True)

    json_string = serializer.to_json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("scatter3D_plot_color_rgb"))

    assert output == expected


def test_color_cmap() -> None:
    serializer = MatplotlibSerializer()

    x = [1, 2, 3, 4, 3]
    y = [2, 1.5, 5, 0, 4]
    z = [3, 2, 1, 0.5, 2]
    color = [0.1, 0.4, 0.6, 0.8, 1]

    __, ax = serializer.subplots(subplot_kw={"projection": "3d"})
    assert isinstance(ax.delegate, MplAxes3D)
    assert isinstance(ax, _AxesProxy3D)
    ax.scatter(x, y, z, c=color, cmap="cividis", enable_colors=True)
    ax.set_title("via cividis cmap")
    ax.set_xlabel("testX")
    ax.set_ylabel("testY")
    ax.set_zlabel("testZ")

    json_string = serializer.to_json()
    output = json.loads(json_string)
    expected = json.loads(read_plot("scatter3D_plot_color_cmap"))

    assert output == expected
