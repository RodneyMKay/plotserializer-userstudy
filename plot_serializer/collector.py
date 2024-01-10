from typing import Callable, List, TextIO, Union
from plot_serializer.model import Figure, MetadataValue
from abc import ABC


class Collector(ABC):
    """
    A Collector is an object that has a subclass for different libraries
    (e.g. MatplotlibCollector). The Collector allows you to use a library like
    you would normally, while collecting all the data you specify inside the plotting
    library and providing methods for serializing that information to json.
    """

    def __init__(self) -> None:
        self._figure = Figure()
        self._collect_actions: List[Callable[[], None]] = []

    def _add_collect_action(self, action: Callable[[], None]) -> None:
        self._collect_actions.append(action)

    def add_custom_metadata(self, name: str, value: MetadataValue) -> None:
        self._figure.metadata[name] = value

    def serialized_figure(self) -> Figure:
        return self._figure

    def json(self) -> str:
        """
        Returns the data that has been collected so far as a json-encoded string.

        Returns:
            str: Json string
        """
        for collect_action in self._collect_actions:
            collect_action()

        return self._figure.model_dump_json(indent=2, exclude_defaults=True)

    def write_json_file(self, file: Union[TextIO, str]) -> None:
        """
        Writes the collected data as json to a file on disk.

        Args:
            file (Union[TextIO, str]): Either a filepath as string or a TextIO object
        """
        if isinstance(file, str):
            with open(file, "w") as file:
                self.write_json_file(file)
        else:
            file.write(self.json())
