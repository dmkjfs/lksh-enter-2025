from abc import abstractmethod
from types import TracebackType
from typing import Self

from src.domain.interfaces.base import BaseInterface
from src.domain.interfaces.api.dtos import (
    BaseMatchesDTO,
    BasePlayerDTO,
    BaseTeamDTO,
    BaseTeamsDTO,
    BaseGoalsDTO,
)


class APIClient(BaseInterface):
    @abstractmethod
    async def get_matches(self) -> BaseMatchesDTO:
        raise NotImplementedError()

    @abstractmethod
    async def get_teams(self) -> BaseTeamsDTO:
        raise NotImplementedError()

    @abstractmethod
    async def get_team(self, team_id: int) -> BaseTeamDTO | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_player(self, player_id: int) -> BasePlayerDTO | None:
        raise NotImplementedError()

    @abstractmethod
    async def login(self, reason: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def get_match_goals(self, match_id: int) -> BaseGoalsDTO:
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
