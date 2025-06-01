from typing import AsyncGenerator

from fastapi import FastAPI, APIRouter, Depends, HTTPException, status

from src.application.core.service import get_service_implementation
from src.domain.api.router import Router
from src.domain.core.exceptions import TeamNotFoundError, PlayerNotFoundError
from src.domain.core.service import Service
from src.infrastructure.api import ExceptionHandler
from src.infrastructure.loggers import application as logger
from src.presentation.schema import (
    SGoal,
    SGoalsResponse,
    SGoalsRequest,
)
from src.presentation.schema import STeamStatsRequest, STeamStatsResponse, SVersusResponse, SVersusRequest

router = APIRouter()


class RouterImplementation(Router):
    @staticmethod
    @router.get(
        path="/stats",
        summary="Get team's statistics",
        responses={
            status.HTTP_200_OK: {"model": STeamStatsResponse},
            status.HTTP_404_NOT_FOUND: {"content": {"application/json": {"example": {
                "detail": [{
                    "loc": ["string", 0],
                    "msg": "Team not found",
                    "type": "string",
                }]
            }}}},
        },
    )
    async def get_team_stats(  # type: ignore[override]
        request: STeamStatsRequest = Depends(STeamStatsRequest),
        service: Service = Depends(get_service_implementation),
    ) -> STeamStatsResponse:
        logger.info("get_team_stats API request")
        async with ExceptionHandler(exceptions={
            TeamNotFoundError: HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Team is not found"),
        }):
            response = await service.get_team_stats(team_name=request.team_name)
        return STeamStatsResponse(
            wins=response.wins,
            losses=response.losses,
            balance=response.balance,
        )

    @staticmethod
    @router.get(
        path="/versus",
        summary="Get players' games' amount",
        responses={
            status.HTTP_200_OK: {"model": SVersusResponse},
            status.HTTP_404_NOT_FOUND: {"content": {"application/json": {"example": {
                "detail": [
                    {
                        "loc": ["string", 0],
                        "msg": "Team is not found",
                        "type": "string",
                    },
                    {
                        "loc": ["string", 0],
                        "msg": "Player is not found",
                        "type": "string",
                    },
                ]
            }}}},
        },
    )
    async def get_player_versus(  # type: ignore[override]
        request: SVersusRequest = Depends(SVersusRequest),
        service: Service = Depends(get_service_implementation),
    ) -> SVersusResponse:
        logger.info("get_player_versus API request")
        async with ExceptionHandler(exceptions={
            PlayerNotFoundError: HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="One or both players are not found"),
            TeamNotFoundError: HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player's team is not found"),
        }):
            response = await service.get_versus_matches(player1_id=request.player1_id, player2_id=request.player2_id)
        return SVersusResponse(amount=response.amount)

    @staticmethod
    @router.get(
        path="/goals",
        summary="Get player's goals",
        responses={status.HTTP_200_OK: {"model": SGoalsRequest}},
    )
    async def get_goals(  # type: ignore[override]
        request: SGoalsRequest = Depends(SGoalsRequest),
        service: Service = Depends(get_service_implementation),
    ) -> SGoalsResponse:
        logger.info("get_goals API request")
        response = await service.get_goals(player_id=request.player_id)
        return list(map(
            lambda goal: SGoal(
                match=goal.match,
                time=goal.time,
            ),
            response.goals,
        ))


async def lifespan(app: FastAPI) -> AsyncGenerator:  # noqa
    service: Service = get_service_implementation()
    await service.login()
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="lksh-enter-2025",
        summary="Test assignment for lksh-2025",
        version="0.1.0",
        docs_url="/",
    )
    app.include_router(router)
    return app
