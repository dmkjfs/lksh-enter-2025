from dataclasses import dataclass
from types import TracebackType
from typing import Self, Literal

from src.infrastructure.exceptions import Exc


@dataclass
class ExceptionHandler:
    """
    Class for handling exceptions on CLI level. Usually, the exceptions
    are raised on lower layers, so CLI-layer has to convert them into
    client-friendly ones. Can only be used via context manager
    """

    def __enter__(self) -> Self:
        """
        :return Self: instance returns itself when entering the context manager
        """

        return self

    def __exit__(  # type: ignore[return]
        self,
        exc_type: type[Exc] | None,
        exc_val: Exc | None,
        exc_tb: TracebackType | None,
    ) -> Literal[True] | None:
        """
        Method to handle low-level exceptions and raise client-friendly
        ones

        :param exc_type: exception type
        :param exc_val: exception instance
        :param exc_tb: full traceback
        """

        if exc_type and exc_val:
            print(exc_val)
            return True
