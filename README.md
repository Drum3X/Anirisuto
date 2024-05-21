# Anirisuto
A wrapper for anilist

## Installing
```sh
pip install Anirisuto
```

## How To Use

## Sync Import
```py
from Anirisuto import SyncClient
```

## Async Import
```py
from Anirisuto import AsyncClient
```

## Use
```py
client = SyncClient()

client.get_anime(search = "Youkoso Jitsuryoku", page = 1) #page is result number
client.get_manga(search = "Youkoso Jitsuryoku", page = 1)
client.get_character(search = "Arisu Sakayanagi", page = 1)

client.get_anime_with_id(id = 98659)
client.get_manga_with_id(id = 96798)
client.get_character_with_id(id = 124691)
```
