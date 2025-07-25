import requests

def test_002_Obtener_informacion_del_objeto_con_id_inexistente():
    url = "https://fakestoreapi.com/products/"
    id_inexistente = "9-/adsas/"
    respuesta = requests.get(url + id_inexistente)

    assert respuesta.status_code == 404

#Prioridad media
#Categoria funcional