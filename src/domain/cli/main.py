from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable

from src.domain.core.service import Service


@dataclass
class CLInterface(ABC):
    service_factory: Callable[[], Service]

    @abstractmethod
    def get_stats(self, team_name: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_versus(
        self,
        player1_id: int,
        player2_id: int,
    ) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_players(self) -> None:
        raise NotImplementedError()
