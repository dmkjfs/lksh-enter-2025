from src.infrastructure.exceptions import Exc


class TeamNotFoundError(Exc):
    """Team with this name is not found"""


class PlayerNotFoundError(Exc):
    """Player with this identificator is not found"""
