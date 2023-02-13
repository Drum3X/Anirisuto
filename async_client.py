import asyncio
from .query import AnilistQuery
from aiohttp import ClientSession

class AsyncClient(AnilistQuery):
    def __init__(self):
        super().__init__()
        self.url = "https://graphql.anilist.co"
            
    async def get_data(
        self,         
        query: str, 
        variables: dict,
    ):                
              								
        async with ClientSession() as cs:
            async with cs.post(self.url, json = {'query': query, 'variables': variables}) as result:
                data = await result.json()
                
        return data
        
    async def get_anime_with_id(
        self, 
        id: int, 
        page: int = 1
    ):
        
        data = await self.get_data(self.anime_with_id, self.get_id_variables(id, page))
        
        if "errors" in data.keys():
            return data["errors"][0]["message"]
            
        result = data["data"]["Page"]["media"]
        if result == []:
            return None
            
        return result
        
    async def get_manga_with_id(
        self, 
        id: str, 
        page: 
        int = 1
    ):
        
        data = await self.get_data(self.manga_with_id, self.get_id_variables(id, page))
        
        if "errors" in data.keys():
            return data["errors"][0]["message"]
            
        result = data["data"]["Page"]["media"]
        if result == []:
            return None
            
        return result
        
    async def get_character_with_id(
        self, 
        id: int, 
        page: int = 1
    ):
        
        data = await self.get_data(self.character_with_id, self.get_id_variables(id, page))
        
        if "errors" in data.keys():
            return data["errors"][0]["message"]
            
        result = data["data"]["Page"]["characters"]
        if result == []:
            return None
            
        return result
      
    async def get_anime(
        self, 
        search: str, 
        page: int = 1
    ):
        
        data = await self.get_data(self.anime, self.get_search_variables(search, page))
        
        if "errors" in data.keys():
            return data["errors"][0]["message"]
            
        result = data["data"]["Page"]["media"]
        if result == []:
            return None
            
        return result
       
    async def get_manga(
        self, 
        search: str, 
        page: int = 1
    ):
        
        data = await self.get_data(self.manga, self.get_search_variables(search, page))
        
        if "errors" in data.keys():
            return data["errors"][0]["message"]
            
        result = data["data"]["Page"]["media"]
        if result == []:
            return None
            
        return result
        
    async def get_character(
        self, 
        search: str, 
        page: int = 1
    ):
        
        data = await self.get_data(self.character, self.get_search_variables(search, page))
        
        if "errors" in data.keys():
            return data["errors"][0]["message"]
            
        result = data["data"]["Page"]["characters"]
        if result == []:
            return None
            
        return result
