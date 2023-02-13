from .queries import srch, get
from importlib.resources import read_text

class AnilistQuery():
	   
    def __init__(self):        
        self.anime = read_text(srch, "anime.graphql")
        self.manga = read_text(srch, "manga.graphql")
        self.character = read_text(srch, "character.graphql")
        self.anime_with_id = read_text(get, "anime.graphql")
        self.manga_with_id = read_text(get, "manga.graphql")
        self.character_with_id = read_text(get, "character.graphql")
    
    def get_search_variables(
        self, 
        search: str, 
        page: int
    ):
        variables = {
            "search": search,
            "page": 1,
            "perPage": page
        }
        
        return variables
    
    def get_id_variables(
        self, 
        id: int, 
        page: int
    ):
        variables = {
            "id": id,
            "page": 1,
            "perPage": page
        }
        
        return variables
