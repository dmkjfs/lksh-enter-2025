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


class BaseStatsRequestDTO(ABC):
    team_name: str


class BaseStatsResponseDTO(ABC):
    wins: int
    losses: int
    balance: int


class BaseVersusRequestDTO(ABC):
    player1_id: int
    player2_id: int


class BaseVersusResponseDTO(ABC):
    amount: int


class BasePlayersResponseDTO(ABC):
    players: list[str]


class BaseMatchesResponseDTO(ABC):
    matches: list[BaseMatchDTO]


class BaseTeamsResponseDTO(ABC):
    teams: list[BaseTeamDTO]


class BaseGoalDTO(ABC):
    match: int
    time: int


class BaseGoalsRequestDTO(ABC):
    player_id: int


class BaseGoalsResponseDTO(ABC):
    goals: list[BaseGoalDTO]
