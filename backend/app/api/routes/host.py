from fastapi import APIRouter, Body
from typing import Annotated
from ...models import game
from ...models import player
from ...state_machine import game_state, utils

router = APIRouter()

@router.post("/create-game")
async def create(player: Annotated[player.HostCreate, Body()], game: Annotated[game.CreateGame, Body()]):
    new_game = game_state.create_game(player.username, game)
    return new_game

@router.post("/start-game")
async def start_game(player: Annotated[player.StartGameRequest, Body()]):
    p = utils.get_player_by_id(player.user_id)
    g = utils.get_game_by_id(player.game_id)
    if p != g.host:
        return {"error": "Only the host can start the game 1"}
    else:
        game_state.start_game(p, g)
        return {"message": f"Game {player.game_id} started"}