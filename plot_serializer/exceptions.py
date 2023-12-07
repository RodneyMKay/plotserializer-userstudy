from typing_extensions import Self


class OntologyWarning(UserWarning):
    def __init__(self: Self, message: str):
        super().__init__(message)
