from ..models.game import CreateGame, Game, game_list, public_game_list
from ..models.player import Player, player_list

def create_game(host_username: str, game: CreateGame) -> Game:
    # Create a host player
    host_player = Player(
        username=host_username,
        status="joined",
        user_id=len(player_list) + 1,
        game_id=game.game_id,
        is_host=True
    )
    # Create a new game with the host player
    g = Game(
        game_id=game.game_id,
        host=host_player
    )
    # Add the host and game to global lists
    player_list.append(host_player)
    game_list.append(g)
    public_game_list.append(game)

    return g