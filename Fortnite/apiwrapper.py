import requests

FNAPI = "https://easyfnapi.glitch.me"

def SetItem(self,Item):
    self.id = Item["id"]
    self.type = Item["type"]
    self.backendType = Item["backendType"]
    self.rarity = Item["rarity"]
    self.backendRarity = Item["backendRarity"]
    self.Names = Item["Names"]
    self.shortDescriptions = Item["shortDescriptions"]
    self.descriptions = Item["descriptions"]
    self.sets = Item["sets"]
    self.series = Item["series"]
    self.backendSeries = Item["backendSeries"]
    self.images = Item["images"]
    self.variants = Item["variants"]
    self.gameplayTags = Item["gameplayTags"]
    self.displayAssetPath = Item["displayAssetPath"]
    self.definition = Item["definition"]
    self.builtInEmoteId = Item["builtInEmoteId"]
    self.requiredItemId = Item["requiredItemId"]
    self.path = Item["path"]
    self.lastUpdate = Item["lastUpdate"]
    self.added = Item["added"]

def getCosmetic(self,params):
    if "NameorId" in params:
        params["name"] = params["NameorId"]
        Cosmetic = requests.get(f"{FNAPI}", params=params).json()
        if "status" in Cosmetic:
            params["id"] = params["NameorId"]
            Cosmetic = requests.get(f"{FNAPI}", params=params).json()
            if "status" in Cosmetic:
                self.status = 404
                return
        else:
            self.status = 200
    else:
        Cosmetic = requests.get(f"{FNAPI}", params=params).json()
        if "status" in Cosmetic:
            self.status = 404
            return
        else:
            self.status = 200
    
    SetItem(self,Cosmetic)

class FortniteAPI:
    class GetSkin:
        def __init__(self,**kwargs):
            params = {"backendType" : "AthenaCharacter"}
            for key, value in kwargs.items():
                params[key] = value

            getCosmetic(self,params)

    class GetBackpack:
        def __init__(self,**kwargs):
            params = {"backendType" : "AthenaBackpack"}
            for key, value in kwargs.items():
                params[key] = value

            getCosmetic(self,params)

    class GetPickaxe:
        def __init__(self,**kwargs):
            params = {"backendType" : "AthenaPickaxe"}
            for key, value in kwargs.items():
                params[key] = value

            getCosmetic(self,params)

    class GetEmote:
        def __init__(self,**kwargs):
            params = {"backendType" : "AthenaDance"}
            for key, value in kwargs.items():
                params[key] = value

            getCosmetic(self,params)

    class GetEmoji:
        def __init__(self,**kwargs):
            params = {"backendType" : "AthenaEmoji"}
            for key, value in kwargs.items():
                params[key] = value

            getCosmetic(self,params)