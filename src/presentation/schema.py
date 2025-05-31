from pydantic import BaseModel

from src.domain.api.schema import (
    BaseSTeamStatsRequest,
    BaseSTeamStatsResponse,
    BaseSVersusRequest,
    BaseSVersusResponse,
    BaseSGoalsRequest,
    BaseSGoal,
)


class STeamStatsRequest(BaseSTeamStatsRequest, BaseModel):
    team_name: str


class STeamStatsResponse(BaseSTeamStatsResponse, BaseModel):
    wins: int
    losses: int
    balance: int


class SVersusRequest(BaseSVersusRequest, BaseModel):
    player1_id: int
    player2_id: int


class SVersusResponse(BaseSVersusResponse, BaseModel):
    amount: int


class SGoalsRequest(BaseSGoalsRequest, BaseModel):
    player_id: int


class SGoal(BaseSGoal, BaseModel):
    match: int
    time: int


type SGoalsResponse = list[SGoal]
