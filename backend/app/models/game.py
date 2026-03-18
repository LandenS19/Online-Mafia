from pydantic import BaseModel
from .player import Player

class CreateGame(BaseModel):
    game_id: int


class Game(BaseModel):
    game_id: int
    players: list[Player] = []# List of Players not the host
    host: Player  # Host of the game
    state: str = "lobby" # State of the game (e.g., "lobby", "in_progress", "finished")

game_list: list[Game] = []
public_game_list: list[CreateGame] = []