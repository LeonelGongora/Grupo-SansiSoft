\


import logging


def assert_comentario_creado(json_resp):
    assert "body" in json_resp,"No se encontró el campo 'body' en la respuesta"
    logging.info("Comentario creado exitosamente con el texto: %s", json_resp["body"])


def assert_comentario_post_invalido(respuesta):
    assert respuesta.status_code in [403, 404], f"Se esperaba código 403 o 404, pero fue {respuesta.status_code}" 
    logging.info("No se creó ningún comentario con un id de post inválido.")

def assert_comentario_vacio_espacios(response):
    assert response.status_code == 200, f"Se esperaba HTTP 200, pero se obtuvo {response.status_code}"
    json_resp = response.json()
    assert "json" in json_resp, "La respuesta no contiene el campo 'json'"
    assert "errors" in json_resp["json"], "La respuesta no contiene el campo 'errors'"
    errores = json_resp["json"]["errors"]
    assert errores, "El campo 'errors' está vacío"
    logging.info("No se permite crear comentarios vacíos o con solo espacios en blanco.")


def assert_comentario_sin_token(response):
    assert response.status_code == 200, f"Se esperaba código 200, pero fue {response.status_code}"
    json_resp = response.json()
    assert "json" in json_resp, "La respuesta no contiene el campo 'json'"
    assert "errors" in json_resp["json"], "La respuesta no contiene el campo 'errors'"
    errores = json_resp["json"]["errors"]
    assert errores, "El campo 'errors' está vacío"
    logging.info("No se permite crear comentarios sin token de autenticación.")


def assert_comentario_token_caducado(response):
    assert response.status_code in [401,404], f"Se esperaba código 401 o 404, pero fue {response.status_code}"
    json_resp = response.json()
    assert "json" in json_resp, "La respuesta no contiene el campo 'json'"
    assert "errors" in json_resp["json"], "La respuesta no contiene el campo 'errors'"
    errores = json_resp["json"]["errors"]
    assert errores, "El campo 'errors' está vacío"
    logging.info("No se permite crear comentarios con token no valido o caducado")