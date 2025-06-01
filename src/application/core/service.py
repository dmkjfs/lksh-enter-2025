from dataclasses import dataclass
from types import TracebackType
from typing import Callable, Self

from src.application.core.dtos import (
    PlayersResponseDTO,
    StatsResponseDTO,
    VersusResponseDTO,
    StatsRequestDTO,
    VersusRequestDTO,
    GoalDTO,
    GoalsResponseDTO,
    GoalsRequestDTO,
)
from src.application.interfaces.api.client import get_api_client_implementation
from src.domain.core.exceptions import TeamNotFoundError, PlayerNotFoundError
from src.domain.core.service import Service
from src.domain.interfaces.api.client import APIClient
from src.domain.interfaces.api.dtos import BaseGoalDTO, BasePlayerDTO
from src.infrastructure.config import settings
from src.infrastructure.loggers import application as logger


@dataclass
class ServiceImplementation(Service):
    api_client_factory: Callable[[], APIClient]

    async def get_players(self) -> PlayersResponseDTO:
        logger.info("get_players service request")
        player_ids = set()
        players_names = list()

        async with self.api_client_factory() as client:
            response = await client.get_teams()
            for team in response:
                player_ids.update(team.players)

            for player_id in player_ids:
                player: BasePlayerDTO | None = await client.get_player(player_id)
                if player:
                    players_names.append(f"{player.name} {player.surname}")

        players_names.sort()
        return PlayersResponseDTO(players=players_names)

    async def get_team_stats(self, team_name: str) -> StatsResponseDTO:
        logger.info("get_team_stats service request")
        request = StatsRequestDTO(team_name=team_name)
        async with self.api_client_factory() as client:
            teams = await client.get_teams()
            team = next((team for team in teams if request.team_name == team.name), None)

            if not team:
                raise TeamNotFoundError("0 0 0")

            matches = await client.get_matches()

        wins = 0
        losses = 0
        goals_scored = 0
        goals_conceded = 0

        for match in matches:
            if match.team1 == team.id:
                goals_scored += match.team1_score
                goals_conceded += match.team2_score
                if match.team1_score > match.team2_score:
                    wins += 1
                elif match.team1_score < match.team2_score:
                    losses += 1
            elif match.team2 == team.id:
                goals_scored += match.team2_score
                goals_conceded += match.team1_score
                if match.team2_score > match.team1_score:
                    wins += 1
                elif match.team2_score < match.team1_score:
                    losses += 1

        return StatsResponseDTO(
            wins=wins,
            losses=losses,
            balance=abs(goals_scored - goals_conceded),
        )

    async def get_versus_matches(self, player1_id: int, player2_id: int) -> VersusResponseDTO:
        logger.info("get_versus_matches service request")
        request = VersusRequestDTO(player1_id=player1_id, player2_id=player2_id)
        async with self.api_client_factory() as client:
            player1 = await client.get_player(request.player1_id)
            player2 = await client.get_player(request.player2_id)

            if not player1 or not player2:
                raise PlayerNotFoundError("0")

            teams = await client.get_teams()

            player1_team = next((team for team in teams if request.player1_id in team.players), None)
            player2_team = next((team for team in teams if request.player2_id in team.players), None)
            if not player1_team or not player2_team:
                raise TeamNotFoundError("Team not found")

            matches = await client.get_matches()

            versus_count = len(list(filter(
                lambda match: (match.team1 == player1_team.id and match.team2 == player2_team.id) or (match.team1 == player2_team.id and match.team2 == player1_team.id),
                matches,
            )))
        return VersusResponseDTO(amount=versus_count)

    async def get_goals(self, player_id: int) -> GoalsResponseDTO:
        logger.info("get_goals service request")
        request = GoalsRequestDTO(player_id=player_id)
        async with self.api_client_factory() as client:
            response = await client.get_matches()
            team_goals: list[BaseGoalDTO] = list()
            for match in response:
                team1 = await client.get_team(team_id=match.team1)
                team2 = await client.get_team(team_id=match.team2)
                players = team1.players  # type: ignore[union-attr]  # trust server
                players.extend(team2.players)  # type: ignore[union-attr]  # trust server
                if request.player_id in players:
                    team_goals.extend(await client.get_match_goals(match_id=match.id))

            player_goals: list[GoalDTO] = list()
            for goal in team_goals:
                if goal.player == request.player_id:
                    player_goals.append(GoalDTO(
                        match=goal.match,
                        time=goal.minute,
                    ))

            return GoalsResponseDTO(goals=player_goals)

    async def login(self) -> None:
        logger.info("login service request")
        async with self.api_client_factory() as client:
            await client.login(reason=settings.reason)

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[Exception] | None,
        exc_val: Exception | None,
        exc_tb: TracebackType | None,
    ) -> None:
        pass


def get_service_implementation() -> ServiceImplementation:
    return ServiceImplementation(api_client_factory=get_api_client_implementation)
