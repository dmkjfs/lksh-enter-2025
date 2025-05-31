from abc import ABC


class BaseSTeamStatsRequest(ABC):
    team_name: str


class BaseSTeamStatsResponse(ABC):
    wins: int
    losses: int
    balance: int


class BaseSVersusRequest(ABC):
    player1_id: int
    player2_id: int


class BaseSVersusResponse(ABC):
    amount: int


class BaseSGoalsRequest(ABC):
    player_id: int


class BaseSGoal(ABC):
    match: int
    time: int


type BaseSGoalsResponse = list[BaseSGoal]
