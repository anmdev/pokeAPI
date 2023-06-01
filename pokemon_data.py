import requests

class PokeAPI:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2"
    
    def _procesar_respuesta(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f'Error {response.status_code}')
            return None
    

    # Método para obtener datos según Pokemon
    def obtener_pokemon(self, nombre:str):
        url = f"{self.base_url}/pokemon/{nombre.lower()}"
        return self._procesar_respuesta(url)
    

    # Método para obtener datos según Grupo Huevo
    def obtener_grupo(self, nombre:str):
        url = f"{self.base_url}/pokemon-species/{nombre.lower()}"
        return self._procesar_respuesta(url)


    # Método para obtener datos según Tipo
    def obtener_tipo(self, id:int):
        url = f"{self.base_url}/type/{id}"
        return self._procesar_respuesta(url)
    

    # Método para obtener datos según Habilidad
    def obtener_habilidad(self, habilidad:str):
        url = f"{self.base_url}/ability/{habilidad.lower()}"
        return self._procesar_respuesta(url)


# --------------------------------------------------

# instancia
pokeapi = PokeAPI()
# datos_pokemon = pokeapi.obtener_pokemon('Scizor')
# print(datos_pokemon['name'])

grupo_huevo = pokeapi.obtener_grupo('scizor')
print(grupo_huevo['egg_groups'][0]['name'])