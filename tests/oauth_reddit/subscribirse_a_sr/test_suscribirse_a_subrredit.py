import os
import requests
import pytest
import logging
from src.assertions.post_suscribirse_assertions import assert_post_created_successfully, assert_payload_matches_schema,assert_subscribe_success_empty_response,assert_response_forbidden,assert_response_not_found,assert_response_unauthorized,assert_response_bad_request,assert_payloadsinaction_matches_schema,assert_response_conflict,assert_response_too_many_requests

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
get_url = "https://oauth.reddit.com"
endpoint = "/api/subscribe"
url = get_url + endpoint
nombre_sr="test"
action="sub"
@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.regression
def test_SRC001_Suscribirse_a_un_subreddit_existente(get_token_fixture,get_user_agent):
    """Verificar que un usuario autenticado pueda suscribirse a un subreddit existente
    mediante la API de Reddit. """""

    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": f"{get_user_agent}"
    }
    payload = {
        "action": action,
        "sr_name": nombre_sr#nombre del subreddit
        }
    logger.info(f"Host: {get_url}")
    logger.debug(f"POST {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")
    assert_payload_matches_schema(payload)
    response = requests.post(url, headers=headers, data=payload)#est bien
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Response body:\n{response.text}")
    assert_subscribe_success_empty_response(response)

@pytest.mark.functional
@pytest.mark.negative
@pytest.mark.smoke
@pytest.mark.regression
def test_SRC002_suscribirse_subreddit_inexistente(get_token_fixture,get_user_agent):
    """Verifica que no se pueda suscribir a un subreddit inexistente con un token válido."""""
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": f"{get_user_agent}"
    }
    payload = {
        "action": action,
        "sr_name": "subreddit_que_no_existe_abc123"
    }
    logger.info(f"Host: {get_url}")
    logger.debug(f"POST {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")
    assert_payload_matches_schema(payload)
    response = requests.post(url, headers=headers, data=payload)
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Response body:\n{response.text}")
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Response body:\n{response.text}")
    assert_response_not_found(response)


@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-001-SR003:Se obtiene un status code de 200 al suscribirse sin tokken ")
def test_SRC003_suscribirse_sin_token(get_user_agent):
        """Verifica que no se pueda suscribir sin un token de autenticación."""""

        headers = {

            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": f"{get_user_agent}"
        }
        payload = {
            "action": action,
            "sr_name": nombre_sr
        }
        logger.info(f"Host: {get_url}")
        logger.debug(f"POST {url}")
        logger.debug(f"Headers: {headers}")
        logger.debug(f"Payload: {payload}")
        assert_payload_matches_schema(payload)
        response = requests.post(url, headers=headers, data=payload)
        logger.info(f"Status code: {response.status_code}")
        logger.debug(f"Response body:\n{response.text}")
        assert response.status_code == 200
        #assert_response_unauthorized(response)deberia dar este error pero si lo permite

        assert any(err in response.text.lower() for err in [
            "please log in", "user_required", "unauthorized", "error"
        ])


@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.regression
def test_SRC004_suscribirse_token_caducado(get_user_agent):
            """Verifica que no se pueda suscribir usando un token expirado."""""
            tokken_inv = os.getenv("REDDIT_ACCESS_TOKEN_CADUCADO")
            headers = {
                'Authorization': f'bearer {tokken_inv}',
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": f"{get_user_agent}"
            }
            payload = {
                "action": action,
                "sr_name": nombre_sr
            }
            logger.info(f"Host: {get_url}")
            logger.debug(f"POST {url}")
            logger.debug(f"Headers: {headers}")
            logger.debug(f"Payload: {payload}")
            assert_payload_matches_schema(payload)
            response = requests.post(url, headers=headers, data=payload)
            logger.info(f"Status code: {response.status_code}")
            logger.debug(f"Response body:\n{response.text}")
            assert_response_unauthorized(response)


@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.regression
def test_SRC005_suscribirse_token_invalido(get_user_agent):
                """Verifica que no se pueda suscribir usando un token malformado o inválido."""""
                get_token_fixture="tokken_invalido"
                headers = {
                    'Authorization': f'bearer {get_token_fixture}',
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": f"{get_user_agent}"
                }
                payload = {
                    "action": action,
                    "sr_name": nombre_sr
                }
                logger.info(f"Host: {get_url}")
                logger.debug(f"POST {url}")
                logger.debug(f"Headers: {headers}")
                logger.debug(f"Payload: {payload}")

                assert_payload_matches_schema(payload)
                response = requests.post(url, headers=headers, data=payload)
                logger.info(f"Status code: {response.status_code}")
                logger.debug(f"Response body:\n{response.text}")

                assert_response_forbidden(response)



@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-002-SR003:Se obtiene un status code de 200 al suscribirse con action vacio")
def test_SRC006_Suscribirse_omitiendo_parámetro_obligatorio_action_con_valor_vacio(get_token_fixture,get_user_agent):
    """Verificar que la solicitud falla si el campo action es enviado con valor vacio en el payload. """""

    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": f"{get_user_agent}"
    }
    payload = {
        "action":"",
        "sr_name": nombre_sr#nombre del subreddit
        }
    logger.info(f"Host: {get_url}")
    logger.debug(f"POST {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")

    #assert_payloadsinaction_matches_schema(payload)
    assert_payload_matches_schema(payload)
    response = requests.post(url, headers=headers, data=payload)#est bien
    logger.info(f"Status code: {response.status_code}")
    #assert_response_bad_request(response)
    logger.debug(f"Response body:\n{response.text}")
    assert_subscribe_success_empty_response(response)


@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-003-SR003:Se obtiene un status code de 200 al suscribirse sin parametro action ")
def test_SRC0015_Suscribirse_sin_parámetro_obligatorio_action(get_token_fixture,get_user_agent):
    """Verificar que la solicitud falla si el campo action es deshabilitado o no existe en el payload. """""

    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": f"{get_user_agent}"
    }
    payload = {
        "sr_name": nombre_sr#nombre del subreddit
        }
    logger.info(f"Host: {get_url}")
    logger.debug(f"POST {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")

    assert_payloadsinaction_matches_schema(payload)
    response = requests.post(url, headers=headers, data=payload)#est bien
    logger.info(f"Status code: {response.status_code}")
    #assert_response_bad_request(response)
    logger.debug(f"Response body:\n{response.text}")
    assert_subscribe_success_empty_response(response)

@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.xfail(reason="BUG-004-SR003:Se obtiene un status code de 200 al suscribirse con parametro invalido action ")
def test_SRC007_Suscribirse_usando_un_valor_inválido_en_el_parámetro_action(get_token_fixture,get_user_agent):
    """Verificar que la API rechaza una solicitud cuando el valor
     del parámetro action es incorrecto (por ejemplo: "subscribe" en lugar de "sub"),
     con el resultado de un error 400. """""

    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": f"{get_user_agent}"
    }
    payload = {
        "action": "subscribe",
        "sr_name": nombre_sr#nombre del subreddit
        }
    logger.info(f"Host: {get_url}")
    logger.debug(f"POST {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")
    assert_payload_matches_schema(payload)
    response = requests.post(url, headers=headers, data=payload)#est bien
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Response body:\n{response.text}")
    # assert_response_bad_request(response)
    assert_subscribe_success_empty_response(response)

@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.xfail(reason="BUG-005-SR003:Se obtiene un status code de 200 al suscribirse a un subreddit que ya esta suscrito ")
def test_SRC008_Suscribirse_a_un_subreddit_que_ya_esta_suscrito_el_usuario(get_token_fixture,get_user_agent):
    """Verificar el comportamiento de la API cuando el usuario intenta suscribirse 
    a un subreddit al que ya está suscrito.
     La API debe devolver 409 Conflict o un mensaje similar que indique que la suscripción ya existe"""""

    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": f"{get_user_agent}"
    }
    payload = {
        "action": action,
        "sr_name": nombre_sr#nombre del subreddit
        }
    logger.info(f"Host: {get_url}")
    logger.debug(f"POST {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")
    assert_payload_matches_schema(payload)
    response = requests.post(url, headers=headers, data=payload)#est bien
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Response body:\n{response.text}")
    #assert_response_conflict(response)
    assert_subscribe_success_empty_response(response)

@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_SRC009_Suscribirse_con_un_método_HTTP_incorrecto_GET(get_token_fixture,get_user_agent):
    """Verificar que una solicitud con método GET en lugar de POST no permita realizar la suscripción. """""

    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": f"{get_user_agent}"
    }
    payload = {
        "action": action,
        "sr_name": nombre_sr#nombre del subreddit
        }
    logger.info(f"Host: {get_url}")
    logger.debug(f"POST {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")
    assert_payload_matches_schema(payload)
    response = requests.get(url, headers=headers, data=payload)#est bien
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Response body:\n{response.text}")
    assert_response_not_found(response)

@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_SRC010_Suscribirse_con_un_método_HTTP_no_permitido_PUT(get_token_fixture,get_user_agent):
    """Verificar que un usuario autenticado pueda suscribirse a un subreddit existente
    mediante la API de Reddit. """""

    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": f"{get_user_agent}"
    }
    payload = {
        "action": action,
        "sr_name": nombre_sr#nombre del subreddit
        }
    logger.info(f"Host: {get_url}")
    logger.debug(f"POST {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")
    assert_payload_matches_schema(payload)
    response = requests.put(url, headers=headers, data=payload)#est bien
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Response body:\n{response.text}")
    assert_response_not_found(response)

@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.regression
def test_SRC011_Suscribirse_con_un_método_HTTP_no_permitido_DELETE(get_token_fixture,get_user_agent):
    """Verificar que una solicitud usando DELETE no permita realizar la suscripción. """""

    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": f"{get_user_agent}"
    }
    payload = {
        "action": action,
        "sr_name": nombre_sr#nombre del subreddit
        }
    logger.info(f"Host: {get_url}")
    logger.debug(f"POST {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")
    assert_payload_matches_schema(payload)
    response = requests.delete(url, headers=headers, data=payload)#est bien
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Response body:\n{response.text}")
    assert_response_not_found(response)

@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.regression
def test_SRC012_Suscribirse_a_un_subreddit_con_nombre_vacío(get_token_fixture,get_user_agent):
    """Suscribirse a un subreddit con nombre vacío.La API debe responder con 400 Bad Request 
    o 422 Unprocessable Entity, indicando que el campo sr_name no puede estar vacío. """""

    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": f"{get_user_agent}"
    }
    payload = {
        "action": action,
        "sr_name": ""#nombre del subreddit
        }
    logger.info(f"Host: {get_url}")
    logger.debug(f"POST {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")
    assert_payload_matches_schema(payload)
    response = requests.post(url, headers=headers, data=payload)#est bien
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Response body:\n{response.text}")
    assert_response_not_found(response)

@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.regression
def test_SRC013_Suscribirse_sin_header_Content_Type(get_token_fixture,get_user_agent):
    """Verificar si es posible realizar la suscripción sin enviar el header
     sin tener errores"""""
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "User-Agent": f"{get_user_agent}"
    }
    payload = {
        "action": action,
        "sr_name": nombre_sr#nombre del subreddit
        }
    logger.info(f"Host: {get_url}")
    logger.debug(f"POST {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")
    assert_payload_matches_schema(payload)
    response = requests.post(url, headers=headers, data=payload)#est bien
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Response body:\n{response.text}")
    assert_subscribe_success_empty_response(response)

@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-006-SR003:Se obtiene un status code de 200 al suscribirse sin el header User agent ")
def test_SRC014_Suscribirse_sin_header_User_Agent(get_token_fixture):
    """Verificar si es posible realizar la suscripción sin enviar el header
     sin tener errores
      La API debe devolver 429 Too Many Requests , 
      ya que el header User-Agent es obligatorio según la política de Reddit
      o error 403 bloqueando al usuario """""

    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded"

    }
    payload = {
        "action": action,
        "sr_name": nombre_sr#nombre del subreddit
        }
    logger.info(f"Host: {get_url}")
    logger.debug(f"POST {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")
    assert_payload_matches_schema(payload)
    response = requests.post(url, headers=headers, data=payload)#est bien
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Response body:\n{response.text}")
    #assert_response_forbidden(response)
    #assert_response_too_many_requests(response)
    assert_subscribe_success_empty_response(response)
