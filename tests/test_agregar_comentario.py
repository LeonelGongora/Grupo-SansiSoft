from src.redditApi.reddit_api import comentar_en_post
from src.assertions.comment_assertions import assert_comentario_creado
from src.schemas.crear_comentario.crear_comentario_schema_output import output_schema
from src.schemas.crear_comentario.crear_comentario_schema_input import input_schema
import jsonschema

THING_ID_POST = "t3_1mazjyd"
def test_agregar_comentario_exitoso():
    datos_entrada = {
        "thing_id": THING_ID_POST,
        "text": "3ero Comentario de prueba desde test 🚀",
        "api_type":"json",
        "return_rtjson": True

    }
    jsonschema.validate(instance=datos_entrada, schema=input_schema)
    respuesta = comentar_en_post(datos_entrada["thing_id"], datos_entrada["text"])
    json_data = respuesta.json()
    jsonschema.validate(instance=json_data, schema=output_schema)
    assert_comentario_creado(respuesta)