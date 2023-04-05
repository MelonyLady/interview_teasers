import random
import requests


def get_pokemon_with_id(id):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    pokemon = response.json()
    return {
        'Name': pokemon['name'].capitalize(),
        'Height': pokemon['height'],
        'Weight': pokemon['weight'],
    }


if __name__ == '__main__':
    print(get_pokemon_with_id(1))
