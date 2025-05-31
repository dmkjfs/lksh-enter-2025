from abc import ABC


class BasePlayerDTO(ABC):
    id: int
    name: str
    surname: str
    number: int


class BaseTeamDTO(ABC):
    id: int
    name: str
    players: list[int]


class BaseMatchDTO(ABC):
    id: int
    team1: int
    team1_score: int
    team2: int
    team2_score: int


class BaseGoalDTO(ABC):
    id: int
    player: int
    match: int
    minute: int


type BaseMatchesDTO = list[BaseMatchDTO]
type BaseTeamsDTO = list[BaseTeamDTO]
type BaseGoalsDTO = list[BaseGoalDTO]
