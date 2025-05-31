from abc import ABC, abstractmethod

from src.domain.api.schema import BaseSTeamStatsRequest, BaseSVersusRequest, BaseSGoalsRequest
from src.presentation.schema import SGoalsResponse
from src.presentation.schema import STeamStatsResponse, SVersusResponse


class Router(ABC):
    @abstractmethod
    async def get_team_stats(self, request: BaseSTeamStatsRequest) -> STeamStatsResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_player_versus(self, request: BaseSVersusRequest) -> SVersusResponse:
        raise NotImplementedError()

    @abstractmethod
    async def get_goals(self, request: BaseSGoalsRequest) -> SGoalsResponse:
        raise NotImplementedError()
