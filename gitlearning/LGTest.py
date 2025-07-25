import requests

def test_001_Obtener_informacion_del_objeto_con_id_7():
    # Descripcion: El objetivo es obtener la informacion del objeto que tiene el id 7 en el servidor.
    # La informacion sera obtenida a tra ves de un objeto JSON que contiene diferentes campos con sus
    # respectivos valores, algunos de estos campos son: titulo, precio, descripción, categoría,
    # url de imagen, y un objeto json anidado con campos propios.

    url = "https://fakestoreapi.com/products/"   #URl de la api sin parametros

    parametros = "7"  #Parametro(s)

    
    list_url = url + parametros #La url y los parametros se unen en una sola cadena
    
    response = requests.get(list_url)  # Se realiza la peticion HTTP GET a la API con la cadena completa

    data = response.json()  # Convertir la respuesta en un diccionario P

    assert "id" in data and data["id"] == int(parametros)  # Validar que el ID recibido coincida con el solicitado
    
    assert response.status_code == 200  # Se verifica que la respuesta tenga un codigo HTTP 200 (exito)
