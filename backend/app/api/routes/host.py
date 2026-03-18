from fastapi import APIRouter, Body
from typing import Annotated
from ...models.game import CreateGame, Game, game_list
from ...models.player import Player, HostCreate, player_list
from ...state_machine import game_state

router = APIRouter()

@router.post("/create-game")
async def create(player: Annotated[HostCreate, Body()], game: Annotated[CreateGame, Body()]):
    new_game = game_state.create_game(player.username, game)
    return new_game

