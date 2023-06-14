from pokemon_response import PokeAPI

data = PokeAPI().obtener_pokemon('Scizor')
print(data['name'])

for stat in data['stats']:
    print('{} : {}'.format(
        stat['stat']['name'], 
        stat['base_stat']))