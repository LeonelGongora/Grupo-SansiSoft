from urllib import response


def assert_comentario_creado(json_resp,respuesta):
    assert "json" in json_resp
    assert "data" in json_resp["json"]
    assert "things" in json_resp["json"]["data"]
    assert len(json_resp["json"]["data"]["things"]) > 0
    comentario_data = json_resp["json"]["data"]["things"][0]["data"]
    assert "body" in comentario_data, "No se encontró el campo 'body' en la respuesta"
    print("✅ Comentario creado correctamente.")


def assert_comentario_post_invalido(respuesta):
    assert respuesta.status_code in [403, 404], f"Se esperaba código 403 o 404, pero fue {respuesta.status_code}" 
    print("✅ No se creo ningun comentario con un id de post invalido")

def assert_comentario_vacio_espacios(response):
    assert response.status_code == 200, f"Se esperaba HTTP 200, pero se obtuvo {response.status_code}"
    json_resp = response.json()
    assert "json" in json_resp, "La respuesta no contiene el campo 'json'"
    assert "errors" in json_resp["json"], "La respuesta no contiene el campo 'errors'"
    errores = json_resp["json"]["errors"]
    assert errores, "El campo 'errors' está vacío"
    print("✅ No se permite crear comentarios vacíos o con solo espacios en blanco.")