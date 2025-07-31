from src.redditApi.reddit_api import comentar_en_post
from src.assertions.comment_assertions import assert_comentario_creado

THING_ID_POST = "t3_1mazjyd"  

def 001_test_agregar_comentario_exitoso():
    respuesta = comentar_en_post(THING_ID_POST, "3ero Comentario de prueba desde test 🚀")
    assert_comentario_creado(respuesta)