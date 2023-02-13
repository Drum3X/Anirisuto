


# Installing
```sh
apt install git 
apt install python3
apt install python3-pip
git clone https://github.com/Drum3X/Simple-Python-Anilist-Api.git
pip3 install -r requirements.txt
```

# How To Use

# Sync Import
```py
from <api file name> import SyncClient
```

# Async Import
```py
from <api file name> import AsyncClient
```

# Functions
```py
client = SyncClient()

client.get_anime(search = "Youkoso Jitsuryoku", page = 1) #page is result number
client.get_manga(search = "Youkoso Jitsuryoku", page = 1)
client.get_character(search = "Arisu Sakayanagi", page = 1)

client.get_anime_with_id(id = 98659)
client.get_manga_with_id(id = 96798)
client.get_character_with_id(id = 124691)
```
