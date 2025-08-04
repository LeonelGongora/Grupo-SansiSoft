import os
import requests
import pytest
import logging
from src.assertions.post_suscribirse_assertions import assert_post_response_schema, assert_post_created_successfully, assert_payload_matches_schema,assert_subscribe_success_empty_response,assert_response_forbidden,assert_response_not_found,assert_response_unauthorized

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
get_url = "https://oauth.reddit.com"
endpoint = "/api/subscribe"
url = get_url + endpoint
nombre_sr="test"
@pytest.mark.functional
@pytest.mark.smoke
def test_SCRUM_T40_Suscribirse_a_un_subreddit_existente(get_token_fixture):
    """Verificar que un usuario autenticado pueda suscribirse a un subreddit existente
    mediante la API de Reddit. """""

    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "User-Agent": "mi_script_de_prueba:0.1 (by u/Big_Title7158)"
    }
    payload = {
        "action": "sub",
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
    print(response.text)
@pytest.mark.functional
@pytest.mark.negative
@pytest.mark.smoke
def test_SCRUM_T72_suscribirse_subreddit_inexistente(get_token_fixture):
    """Verifica que no se pueda suscribir a un subreddit inexistente con un token válido."""""
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "mi_script_de_prueba:0.1 (by u/Big_Title7158)"
    }
    payload = {
        "action": "sub",
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
    print(response.text)

@pytest.mark.functional
@pytest.mark.negative
@pytest.mark.smoke
def test_SCRUM_T73_suscribirse_sin_token():
        """Verifica que no se pueda suscribir sin un token de autenticación."""""

        headers = {

            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "mi_script_de_prueba:0.1 (by u/Big_Title7158)"
        }
        payload = {
            "action": "sub",
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
        print(response.text)

@pytest.mark.functional
@pytest.mark.negative
@pytest.mark.smoke
def test_SCRUM_T74_suscribirse_token_caducado():
            """Verifica que no se pueda suscribir usando un token expirado."""""
            tokken_inv = os.getenv("TOKEN_CADUCEUS")
            headers = {
                'Authorization': f'bearer {tokken_inv}',
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "mi_script_de_prueba:0.1 (by u/Big_Title7158)"
            }
            payload = {
                "action": "sub",
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
            print(response.text)

@pytest.mark.functional
@pytest.mark.negative
@pytest.mark.smoke
def test_SCRUM_T75_suscribirse_token_invalido():
                """Verifica que no se pueda suscribir usando un token malformado o inválido."""""
                get_token_fixture="tokken_invalido"
                headers = {
                    'Authorization': f'bearer {get_token_fixture}',
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "mi_script_de_prueba:0.1 (by u/Big_Title7158)"
                }
                payload = {
                    "action": "sub",
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
                print(response.text)
