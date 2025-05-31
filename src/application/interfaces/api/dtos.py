from pydantic import BaseModel

from src.domain.interfaces.api.dtos import BaseMatchDTO, BaseTeamDTO, BasePlayerDTO, BaseGoalDTO


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


class GoalDTO(BaseGoalDTO, BaseModel):
    id: int
    player: int
    match: int
    minute: int


type MatchesDTO = list[MatchDTO]
type TeamsDTO = list[TeamDTO]
type GoalsDTO = list[GoalDTO]
