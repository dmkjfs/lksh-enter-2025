from types import TracebackType
from typing import Self

import aiohttp

from src.domain.interfaces.api.client import APIClient
from src.application.interfaces.api.dtos import (
    MatchDTO,
    MatchesDTO,
    PlayerDTO,
    TeamDTO,
    TeamsDTO,
    GoalsDTO,
    GoalDTO,
)
from src.infrastructure.config import settings


class APIClientImplementation(APIClient, aiohttp.ClientSession):
    def __init__(self) -> None:
        super().__init__(base_url=settings.api_base_url)

    async def get_matches(self) -> MatchesDTO:  # type: ignore[override]
        response = await self.get(
            url="/matches",
            headers={"Authorization": settings.api_token},
        )
        response.raise_for_status()
        return list(map(
            lambda match: MatchDTO(**match),
            await response.json(),
        ))

    async def get_teams(self) -> TeamsDTO:  # type: ignore[override]
        response = await self.get(
            url="/teams",
            headers={"Authorization": settings.api_token},
        )
        response.raise_for_status()
        return list(map(
            lambda team: TeamDTO(**team),
            await response.json(),
        ))

    async def get_team(self, team_id: int) -> TeamDTO | None:
        response = await self.get(
            url=f"/teams/{team_id}",
            headers={"Authorization": settings.api_token},
        )

        if response.status == 404:
            return None

        response.raise_for_status()
        return TeamDTO(**await response.json())

    async def get_player(self, player_id: int) -> PlayerDTO | None:
        response = await self.get(
            url=f"/players/{player_id}",
            headers={"Authorization": settings.api_token},
        )

        if response.status == 404:
            return None

        response.raise_for_status()
        return PlayerDTO(**await response.json())

    async def login(self, reason: str) -> None:
        await self.post(
            url="/login",
            data={"reason": reason},
            headers={"Authorization": settings.api_token},
        )

    async def get_match_goals(self, match_id: int) -> GoalsDTO:  # type: ignore[override]
        response = await self.get(
            url="/goals",
            params={"match_id": match_id},
            headers={"Authorization": settings.api_token},
        )

        response.raise_for_status()
        return list(map(
            lambda goal: GoalDTO(**goal),
            await response.json(),
        ))

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.close()


def get_api_client_implementation() -> APIClientImplementation:
    return APIClientImplementation()
