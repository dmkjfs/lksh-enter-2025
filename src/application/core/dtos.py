from pydantic import BaseModel

from src.domain.core.dtos import (
    BaseTeamsResponseDTO,
    BaseMatchesResponseDTO,
    BasePlayersResponseDTO,
    BaseVersusResponseDTO,
    BaseStatsResponseDTO,
    BaseMatchDTO,
    BaseTeamDTO,
    BasePlayerDTO,
    BaseStatsRequestDTO,
    BaseVersusRequestDTO,
    BaseGoalDTO,
    BaseGoalsResponseDTO,
    BaseGoalsRequestDTO,
)


class PlayerDTO(BasePlayerDTO, BaseModel):
    id: int
    name: str
    surname: str
    number: int


class TeamDTO(BaseTeamDTO, BaseModel):
    id: int
    name: str
    players: list[int]


class MatchDTO(BaseMatchDTO, BaseModel):
    id: int
    team1: int
    team1_score: int
    team2: int
    team2_score: int


class StatsRequestDTO(BaseStatsRequestDTO, BaseModel):
    team_name: str


class StatsResponseDTO(BaseStatsResponseDTO, BaseModel):
    wins: int
    losses: int
    balance: int


class VersusRequestDTO(BaseVersusRequestDTO, BaseModel):
    player1_id: int
    player2_id: int


class VersusResponseDTO(BaseVersusResponseDTO, BaseModel):
    amount: int


class PlayersResponseDTO(BasePlayersResponseDTO, BaseModel):
    players: list[str]


class MatchesResponseDTO(BaseMatchesResponseDTO, BaseModel):
    matches: list[MatchDTO]  # type: ignore[assignment]


class TeamsResponseDTO(BaseTeamsResponseDTO, BaseModel):
    teams: list[TeamDTO]  # type: ignore[assignment]


class GoalDTO(BaseGoalDTO, BaseModel):
    match: int
    time: int


class GoalsRequestDTO(BaseGoalsRequestDTO, BaseModel):
    player_id: int


class GoalsResponseDTO(BaseGoalsResponseDTO, BaseModel):
    goals: list[GoalDTO]  # type: ignore[assignment]
