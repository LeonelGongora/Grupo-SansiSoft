import requests
import pytest

def test_ID_JES001_10_Obtener_la_lista_de_obras_de_arte_publicadas():
    """El usuario debe obtener una lista de obras de arte publicadas en colección publica digital"""
    #Ambiente
url = "https://api.artic.edu/api/v1/artworks"

#pasos
#1. Sleccionar Get
list_url= url 
#2.Llamar el recuerso de obras
#3.click en el boton send 

response = requests.get(list_url)
assert response.status_code == 200