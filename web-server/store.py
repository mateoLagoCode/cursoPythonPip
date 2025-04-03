import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') # Obtengo el contenido de esta api
    print(r.status_code) # Me da el codigo del estado de la conexion
    print(r.text) # Me da todo el contenido de la api en forma de texto
    print(type(r.text)) # Me da todo el tipo de dato 

    categories = r.json() # Creamos una variable en donde al GET lo transformamos en un json

    # Hacemos una iteracion para conseguir los nombres de la categorias
    for category in categories:
        print(category['name'])

