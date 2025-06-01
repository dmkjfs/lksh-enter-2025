import asyncio
from dataclasses import dataclass
from typing import Callable

from src.application.core.service import get_service_implementation
from src.domain.cli.main import CLInterface
from src.domain.core.service import Service
from src.infrastructure.cli import ExceptionHandler


@dataclass
class CLImplementation(CLInterface):
    service_factory: Callable[[], Service]

    def get_stats(
        self,
        team_name: str,
        service: Service = get_service_implementation(),
    ) -> None:
        with ExceptionHandler():
            response = asyncio.run(service.get_team_stats(team_name=team_name))
            print(f"{response.wins} {response.losses} {response.balance}")

    def get_versus(
        self,
        player1_id: int,
        player2_id: int,
        service: Service = get_service_implementation(),
    ) -> None:
        with ExceptionHandler():
            response = asyncio.run(service.get_versus_matches(player1_id=player1_id, player2_id=player2_id))
            print(response.amount)

    def get_players(self, service: Service = get_service_implementation()) -> None:
        with ExceptionHandler():
            response = asyncio.run(service.get_players())
            print(*response.players, sep="\n")


def get_command_line_implementation() -> CLImplementation:
    return CLImplementation(service_factory=get_service_implementation)


if __name__ == "__main__":
    cli = get_command_line_implementation()

    cli.get_players()

    while True:
        try:
            command = input().strip()

            if command.startswith("stats? "):
                _team_name = command[6:].strip().strip('"')
                cli.get_stats(_team_name)

            elif command.startswith("versus? "):
                try:
                    _, _player1_id, _player2_id = command.split()
                    cli.get_versus(int(_player1_id), int(_player2_id))
                except ValueError:
                    print("0")
        except KeyboardInterrupt:
            break
        except EOFError:
            break
