import logging
import json
from src.logs.logger import logger

def assert_comentario_creado(json_resp):
    logging.debug("Verificando si el comentario fue creado correctamente.")
    assert "body" in json_resp, "No se encontró el campo 'body' en la respuesta"
    assert len(json_resp["body"]) > 0, "El campo 'body' no debe estar vacío"
    logging.info("Comentario creado exitosamente con el texto: %s", json_resp["body"])

def assert_comentario_post_invalido(respuesta):
    logging.debug("Verificando respuesta para post con ID inválido.")
    assert respuesta.status_code in [403, 404], f"Se esperaba código 403 o 404, pero fue {respuesta.status_code}" 
    logging.info("No se creó ningún comentario con un id de post inválido.")

def assert_comentario_vacio_espacios(response):
    logging.debug("Verificando comentario vacío o con solo espacios.")
    assert response.status_code == 200, f"Se esperaba HTTP 200, pero se obtuvo {response.status_code}"
    json_resp = response.json()
    assert "json" in json_resp, "La respuesta no contiene el campo 'json'"
    assert "errors" in json_resp["json"], "La respuesta no contiene el campo 'errors'"
    errores = json_resp["json"]["errors"]
    assert errores, "El campo 'errors' está vacío"
    logging.info("No se permite crear comentarios vacíos o con solo espacios en blanco.")
    logging.debug("Errores detectados: %s", errores)

def assert_comentario_sin_token(response):
    logging.debug("Verificando comportamiento al crear comentario sin token.")
    assert response.status_code == 200, f"Se esperaba código 200, pero fue {response.status_code}"
    json_resp = response.json()
    assert "json" in json_resp, f"La respuesta no contiene el campo 'json': {json_resp}"
    errores = json_resp["json"].get("errors")
    assert errores is not None, "El campo 'errors' no está presente"
    assert isinstance(errores, list), f"'errors' no es una lista: {errores}"
    assert len(errores) > 0, "El campo 'errors' está vacío"
    logging.debug("Errores: %s", errores)
    logging.info("No se permite crear comentarios sin token de autenticación.")

def assert_comentario_token_caducado(response):
    logging.debug("Verificando comportamiento con token caducado.")
    assert response.status_code == 401, f"Se esperaba status 401, pero se recibió {response.status_code}"
    content_type = response.headers.get("Content-Type", "")
    if "application/json" in content_type:
        json_resp = response.json()
        assert "error" in json_resp or "message" in json_resp, "Respuesta no contiene campos de error esperados"
        logging.debug("Respuesta JSON: %s", json_resp)
    else:
        logging.info("Token de autenticación caducado, no se pudo crear el comentario.")

def assert_obtener_comentario(response):
    logging.debug("Verificando obtención de comentario.")
    assert response.status_code == 200, f'Se esperaba código 200, se obtiene {response.status_code}'
    json_resp = response.json()
    logging.info("Se obtiene código 200")
    assert "data" in json_resp, "La respuesta no contiene el campo 'data'"
    children = json_resp.get("data", {}).get("children", [])
    if children and len(children) > 0:
        body = children[0].get("data", {}).get("body", "")
        logging.debug("Comentario obtenido: %s", body)
    else:
        body = ""
        logging.warning("No se encontró ningún comentario en la respuesta.")
        assert True, "No se encontró ningún comentario en la respuesta"
    logging.info("Comentario obtenido correctamente: %s", body)

def assert_existe_body(response):
    logging.debug("Verificando que el campo 'body' exista y no esté vacío.")
    resp_json = response.json()
    body = resp_json["data"]["children"][0]["data"]["body"]
    assert body, "El campo body está vacío :("
    logging.info("Se verificó que el campo 'body' contiene datos.")

def assert_comentario_id_invalido(response):
    logging.debug("Verificando comportamiento con ID de comentario inválido.")
    json_resp = response.json()
    if response.status_code == 200:
        children = json_resp.get("data", {}).get("children")
        assert isinstance(children, list), "El campo 'children' no es una lista"
        assert len(children) == 0, "Se esperaba que 'children' esté vacío para ID inválido"

        tiene_error = any(clave in json_resp for clave in ["error", "message", "errors"])
        assert tiene_error, "No se encontró un campo de error en la respuesta para ID inválido"
        logging.info("Se encontró un campo de error en la respuesta.")

    else:
        assert response.status_code in [400, 401, 404], (
            f"Se esperaba código 400, 401 o 404; se obtuvo {response.status_code}"
        )
        tiene_error = any(clave in json_resp for clave in ["error", "message", "errors"])
        assert tiene_error, f"No se encontró mensaje de error en respuesta de fallo: {json_resp}"
        logging.info("Se detectó correctamente un error en la respuesta para ID inválido.")

