import matplotlib
import json
from plot_serializer.adapters import Plot, MatplotlibAdapter


class Serializer:
    def __init__(self, p) -> None:
        self.plot = self.convert_plot(p)
        pass

    def convert_plot(self, p) -> Plot:
        if type(p) == matplotlib.pyplot.Figure:
            converted_plot = MatplotlibAdapter(p)
        else:
            raise NotImplementedError(
                "Only matplotlib is implemented. Make sure you submit a matplotlib.pyplot.Figure object."
            )
        return converted_plot

    def to_json(self) -> None:
        return json.loads(
            json.dumps(self.plot, default=lambda o: getattr(o, "__dict__", str(o)))
        )
