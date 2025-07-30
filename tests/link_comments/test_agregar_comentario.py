from src.redditApi.reddit_api import comentar_en_post
from src.assertions.comment_assertions import assert_comentario_creado
import pytest


THING_ID_POST = "t3_1mazjyd"  # Reemplaza con un post real

@pytest.mark.functional
@pytest.mark.smoke
def test_agregar_comentario_exitoso():
    respuesta = comentar_en_post(THING_ID_POST, "3ero Comentario de prueba desde test 🚀")
    assert_comentario_creado(respuesta)