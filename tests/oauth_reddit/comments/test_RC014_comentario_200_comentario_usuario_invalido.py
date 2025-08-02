from src.redditApi.reddit_api import comentar_en_post
import pytest
import logging

THING_ID_POST = "t3_1mazjyd"

@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.regression
def test_RC014_codigo_200_comentario_usuario_valido():
    datos_entrada = {
        "thing_id": THING_ID_POST,
        "text": "Comentario para verificar código 200",
        "api_type": "json",
        "return_rtjson": True
    }
    logging.info("Intentando crear comentario para verificar código 200 con id: %s", THING_ID_POST)
    respuesta = comentar_en_post(datos_entrada["thing_id"], datos_entrada["text"])
    logging.info("Validando que el código HTTP sea 200")
    assert respuesta.status_code == 200, f"Esperado código 200, obtenido {respuesta.status_code}"
    logging.info("✅ Código 200 recibido correctamente al comentar con usuario válido.")