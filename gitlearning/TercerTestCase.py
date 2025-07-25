import requests

def test_003_Borrar_objeto_con_id_1_con_datos_invalidos():
    url = "https://fakestoreapi.com/products/"
    id_valido = "1"
    headers = {"Content-Type": "application/json"}
    datos = "{zasd':}" 

    response = requests.delete(url + id_valido, data=datos, headers=headers)

    assert response.status_code == 400

#Prioridad baja
#Categoria funcional