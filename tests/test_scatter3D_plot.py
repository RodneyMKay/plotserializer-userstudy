# import json
# from plot_serializer.matplotlib.serializer import MatplotlibSerializer
# from tests import read_plot


# def test_simple() -> None:
#     serializer = MatplotlibSerializer()

#     x = [1, 2, 3, 4, 3]
#     y = [2, 1.5, 5, 0, 4]

#     _, ax = serializer.subplots()
#     ax.scatter(x, y)

#     json_string = serializer.to_json()
#     output = json.loads(json_string)
#     expected = json.loads(read_plot("line_plot_simple"))

#     assert output == expected


# def test_size() -> None:
#     serializer = MatplotlibSerializer()

#     x = [1, 2, 3, 4, 3]
#     y = [2, 1.5, 5, 0, 4]
#     sizes = 5

#     _, ax = serializer.subplots()
#     ax.scatter(x, y, enable_sizes=True)

#     json_string = serializer.to_json()
#     output = json.loads(json_string)
#     expected = json.loads(read_plot("line_plot_simple"))

#     assert output == expected

# def test_sizes_list() -> None:
#     serializer = MatplotlibSerializer()

#     x = [1, 2, 3, 4, 3]
#     y = [2, 1.5, 5, 0, 4]
#     sizes = [1, 5, 10, 20, 30]

#     _, ax = serializer.subplots()
#     ax.scatter(x, y, enable_sizes=True)

#     json_string = serializer.to_json()
#     output = json.loads(json_string)
#     expected = json.loads(read_plot("line_plot_simple"))

#     assert output == expected


# def test_color_string() -> None
#     serializer = MatplotlibSerializer()

#     x = [1, 2, 3, 4, 3]
#     y = [2, 1.5, 5, 0, 4]
#     color = "green"

#     _, ax = serializer.subplots()
#     ax.scatter(x, y, c=color, enable_colors=True)

#     json_string = serializer.to_json()
#     output = json.loads(json_string)
#     expected = json.loads(read_plot("line_plot_simple"))

#     assert output == expected


# def test_color_list_string() -> None:
#     serializer = MatplotlibSerializer()

#     x = [1, 2, 3, 4, 3]
#     y = [2, 1.5, 5, 0, 4]
#     color = ["green", "blue", "red", "yellow", "black"]

#     _, ax = serializer.subplots()
#     ax.scatter(x, y, c=color, enable_colors=True)

#     json_string = serializer.to_json()
#     output = json.loads(json_string)
#     expected = json.loads(read_plot("line_plot_simple"))

#     assert output == expected


# def test_color_enabled_false() -> None:
#     serializer = MatplotlibSerializer()

#     x = [1, 2, 3, 4, 3]
#     y = [2, 1.5, 5, 0, 4]
#     color = ["green", "blue", "red", "yellow", "black"]

#     _, ax = serializer.subplots()
#     ax.scatter(x, y, c=color, enable_colors=True)

#     json_string = serializer.to_json()
#     output = json.loads(json_string)
#     expected = json.loads(read_plot("line_plot_simple"))

#     assert output == expected

# def test_color_hex() -> None:
#     serializer = MatplotlibSerializer()

#     x = [1, 2, 3, 4, 3]
#     y = [2, 1.5, 5, 0, 4]
#     color = ["#008000ff", "#0000ffff", "#ff0000ff", "#ffff00ff", "#000000ff"]

#     _, ax = serializer.subplots()
#     ax.scatter(x, y, c=color, enable_colors=True)

#     json_string = serializer.to_json()
#     output = json.loads(json_string)
#     expected = json.loads(read_plot("line_plot_simple"))

#     assert output == expected

# def test_color_rgb() -> None:
#     serializer = MatplotlibSerializer()

#     x = [1, 2, 3, 4, 3]
#     y = [2, 1.5, 5, 0, 4]
#     color = [(0.0, 0.5019607843137255, 0.0), (0.0, 0.0, 1.0),(1.0, 0.0, 0.0),(1.0, 1.0, 0.0), (0.0, 0.0, 0.0)]

#     _, ax = serializer.subplots()
#     ax.scatter(x, y, c=color, enable_colors=True)

#     json_string = serializer.to_json()
#     output = json.loads(json_string)
#     expected = json.loads(read_plot("line_plot_simple"))

#     assert output == expected
