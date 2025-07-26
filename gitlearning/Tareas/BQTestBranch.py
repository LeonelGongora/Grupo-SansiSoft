import requests
#import pytest


#titulo: Verificar que muestra la puublicación del ID espcifico
    #def test_001_obtenerListaPublicaciones():

#Descripcion : Verificar que se muestre la información de la publicacion con ID 1

#Ambiente
url = "https://jsonplaceholder.typicode.com/posts/23"

#Prioridad alta
#Pre condiciones
#- Tener acceso al URL
#- Contar con el programa de Postman
#- Contar con un lector de codigo


 #Pasos
 #1. Selecciona la opcion GET
 #2. Ingresar el enlace 
 #3. Obtener el codigo en python mediante el postMan
payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
assert response.status_code == 200
print(response.text)

#Resultado Esperado

# Se muestra la información de la publicación del ID 23