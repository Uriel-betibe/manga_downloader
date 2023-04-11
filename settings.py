def load_user_mp(ids):
    with open("ressource/ids.txt", "r") as f:
       for line in f:
           ids.append(line.split(":")[1])
ID = []
load_user_mp(ID)
PROVIDER = "https://manganato.com/"

user = ID[0]
mp = ID[1]

MANGAFILE = "ressource/mangas.txt"
IDS = "ressource/ids.txt"
