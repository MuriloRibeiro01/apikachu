# The requests is like the virtual waiter
import requests

# The json library will show pretty results :)
import json


# Defines the pokemon's name that we want to get
pokemon_name = input("Qual Pokémon você quer buscar? ").lower() # .lower() to make it lowercase.

# This is the "address" of the "server" and the specific "request".
# It's what we call "endpoint" of the API.
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

print(f"Buscando informações do {pokemon_name.capitalize()}...")

# Here the request is made (the GET request) to the URL.
# Our waiter on the way to the server
response = requests.get(url)

# Verifies if the 'requests' have got the data or a bad new
# The 'status.code' 200 means "Ok, all right".
if response.status_code == 200:
    print("Pokemon encontrado com sucesso! 🎉\n")

    # The data will come as a JSON archive. It will turn the API in a Python dictionary.
    data = response.json()

    # Get the infos from the Pokemon
    print(f"Nome: {data['name'].capitalize()}")
    print(f"Nº na Pokédex: {data['id']}")
    print(f"Altura: {data['height'] * 10} cm") # Convert to centimeters
    print(f"Peso: {data['weight'] / 10} kg") # Converto do kilos

    # The skills are a list
    # Goes trough the entire list
    abilities = [ability['ability']['name'] for ability in data ['abilities']]
    print(f"Habilidades: {', '.join(abilities)}")

elif response.status_code == 404:
    print(f"Não encontrei o Pokémon '{pokemon_name}'. Tem certeza que o nome está correto?")

else:
    print(f"Algo inesperado aconteceu. Código do erro: {response.status_code}")