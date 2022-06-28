import requests

# response = requests.get("http://api.open-notify.org/astros.json")

# json = response.json()

# print("The people currently in space are:")
# for x in json["people"]:
#     print(x["name"])


# api = "https://pokeapi.co/api/v2/pokemon/pikachu"

# pokemon = requests.get(api)

# poke_json = pokemon.json()

# print(poke_json["name"])


# # counter = 0
# while (counter < 100):
#     counter += 1
#     api = "https://pokeapi.co/api/v2/pokemon/" + str(counter)
#     pokemon = requests.get(api)
#     poke_json = pokemon.json()
#     print(counter, "is the pokemon:", poke_json["name"])


api = "https://dog.ceo/api/breeds/image/random"

something = requests.get(api)

json = something.json()

print (json['message'])