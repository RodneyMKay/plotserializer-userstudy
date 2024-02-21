from plot_serializer.matplotlib.serializer import MatplotlibSerializer

serializer = MatplotlibSerializer()
fig, ax = serializer.subplots()

x = [1, 2, 3, 4, 3, 2, 6, 2, 4, 3]
y = [2, 1.5, 5, 0, 4, 7, 5, 2, 1, 3]
ax.scatter(x, y)
serializer.to_json()
serializer.write_json_file("line_plot_simple")
