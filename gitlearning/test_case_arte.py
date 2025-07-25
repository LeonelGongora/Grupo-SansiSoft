import requests
import pytest

#prioridad 
#medio
@pytest.mark.smoke

#titulo
def ID_JES001_10():
    #""El usuario debe obtener una lista de obras de arte publicadas en colección publica digital.""
    
    #ambiente
    url="https://api.artic.edu/docs/#quick-start"
    list_url = url + "obras de arte"
    
    response= requests.get(list_url)
    
    assert response.status_code == 200