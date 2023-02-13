from .query import AnilistQuery
from requests import post

class SyncClient(AnilistQuery):
    def __init__(self):
        super().__init__()
        self.url = "https://graphql.anilist.co"
            
    def get_data(
        self,         
        query: str, 
        variables: dict,
    ):                
              								        
        data = post(self.url, json = {'query': query, 'variables': variables}).json()                             
        return data
        
    def get_anime_with_id(
        self, 
        id: int, 
    ):
        
        data = self.get_data(self.anime_with_id, self.get_id_variables(id))
        
        if "errors" in data.keys():
            return data["errors"][0]["message"]
            
        result = data["data"]["Page"]["media"]
        if result == []:
            return None
            
        return result
        
    def get_manga_with_id(
        self, 
        id: str, 
    ):
        
        data = self.get_data(self.manga_with_id, self.get_id_variables(id))
        
        if "errors" in data.keys():
            return data["errors"][0]["message"]
            
        result = data["data"]["Page"]["media"]
        if result == []:
            return None
            
        return result
        
    def get_character_with_id(
        self, 
        id: int,
    ):
        
        data = self.get_data(self.character_with_id, self.get_id_variables(id))
        
        if "errors" in data.keys():
            return data["errors"][0]["message"]
            
        result = data["data"]["Page"]["characters"]
        if result == []:
            return None
            
        return result
      
    def get_anime(
        self, 
        search: str, 
        page: int = 1
    ):
        
        data = self.get_data(self.anime, self.get_search_variables(search, page))
        
        if "errors" in data.keys():
            return data["errors"][0]["message"]
            
        result = data["data"]["Page"]["media"]
        if result == []:
            return None
            
        return result
       
    def get_manga(
        self, 
        search: str, 
        page: int = 1
    ):
        
        data = self.get_data(self.manga, self.get_search_variables(search, page))
        
        if "errors" in data.keys():
            return data["errors"][0]["message"]
            
        result = data["data"]["Page"]["media"]
        if result == []:
            return None
            
        return result
        
    def get_character(
        self, 
        search: str, 
        page: int = 1
    ):
        
        data = self.get_data(self.character, self.get_search_variables(search, page))
        
        if "errors" in data.keys():
            return data["errors"][0]["message"]
            
        result = data["data"]["Page"]["characters"]
        if result == []:
            return None
            
        return result
