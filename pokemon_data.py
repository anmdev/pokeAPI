from pokemon_response import PokeAPI

datos_pokemon = PokeAPI().obtener_pokemon('Scizor')
print(datos_pokemon['name'])