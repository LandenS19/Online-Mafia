from fastapi import APIRouter, Body
from typing import Annotated
from ...models.player import PlayerCreate, Player, player_list
from ...models.game import CreateGame, Game, game_list, public_game_list
router = APIRouter()

@router.get("/public-game-list")
async def get_public_games():
    return public_game_list

@router.get("/game-list")
async def get_games():
    return game_list

@router.post("/join-game")
async def join(player: Annotated[PlayerCreate, Body()]):
    for game in game_list:
        if game.game_id == player.game_id:
            p = Player(username=player.username, status="joined", 
                       user_id=len(player_list)+1, game_id=player.game_id)
            game.players.append(p)
            player_list.append(p)
            return player
    return {"error": "Game not found"}

@router.get("/players")
async def get_players():
    return {"players": player_list}