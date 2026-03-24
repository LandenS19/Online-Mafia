from pydantic import BaseModel

class PlayerCreate(BaseModel):
    username: str
    game_id: int

class HostCreate(BaseModel):
    username: str

class Player(BaseModel):
    username: str
    status : str
    user_id : int
    game_id : int | None = None
    is_host : bool = False

class StartGameRequest(BaseModel):
    user_id: str
    game_id: int

player_list : list[Player]= []