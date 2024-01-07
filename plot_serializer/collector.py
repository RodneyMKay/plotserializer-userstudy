from typing import TextIO, Union
from plot_serializer.model import Figure
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

    def json(self) -> str:
        """
        Returns the data that has been collected so far as a json-encoded string.

        Returns:
            str: Json string
        """
        return self._figure.model_dump_json(indent=2, exclude_defaults=True)

    def write_to_file(self, file: Union[TextIO, str]) -> None:
        """
        Writes the collected data as json to a file on disk.

        Args:
            file (Union[TextIO, str]): Either a filepath as string or a TextIO object
        """
        if isinstance(file, str):
            with open(file, "w") as file:
                self.write_to_file(file)
        else:
            file.write(self.json())
