from abc import ABC, abstractmethod
from dataclasses import dataclass
from types import TracebackType
from typing import Callable, Self

from src.domain.core.dtos import BasePlayersResponseDTO, BaseStatsResponseDTO, BaseVersusResponseDTO, BaseGoalsResponseDTO
from src.domain.interfaces.api.client import APIClient


@dataclass
class Service(ABC):
    api_client_factory: Callable[[], APIClient]

    @abstractmethod
    async def get_players(self) -> BasePlayersResponseDTO:
        raise NotImplementedError()

    @abstractmethod
    async def get_team_stats(self, team_name: str) -> BaseStatsResponseDTO:
        raise NotImplementedError()

    @abstractmethod
    async def get_versus_matches(self, player1_id: int, player2_id: int) -> BaseVersusResponseDTO:
        raise NotImplementedError()

    @abstractmethod
    async def get_goals(self, player_id: int) -> BaseGoalsResponseDTO:
        raise NotImplementedError()

    @abstractmethod
    async def login(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def __aenter__(self) -> Self:
        return self

    @abstractmethod
    async def __aexit__(
        self,
        exc_type: type[Exception] | None,
        exc_val: Exception | None,
        exc_tb: TracebackType | None,
    ) -> None:
        pass
