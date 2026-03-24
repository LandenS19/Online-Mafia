from ..models.game import Game, game_list
from ..models.player import Player, player_list

def get_player_by_id(user_id: int) -> Player:
    for player in player_list:
        if player.user_id == user_id:
            return player
    return {"error": "Player not found"}

def get_game_by_id(game_id: int):
    for game in game_list:
        if game.game_id == game_id:
            return game
    return {"error": "Game not found"}