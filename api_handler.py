import requests
import pokebase as pb


def create_request(url, params=[], headers=[]):
    try:
        return requests.get(url, params=params, headers=headers)
    except BaseException:
        print(BaseException)
    return None


def dbygo_card():
    apireturn = create_request(r"https://db.ygorganization.com/data/card/15110")

    print(apireturn.json()["cardData"]["en"]["name"])
    # scribe.writeDebugLog(apireturn.text)
    return


def dbpoke():
    apireturn1 = pb.pokemon("gardevoir")
    print(apireturn1.__dir__())
    #apireturn=pb.SpriteResource('pokemon', apireturn1.height)
    #print(apireturn)