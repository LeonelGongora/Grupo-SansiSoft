
def crear_payload_comentario(thing_id, texto):
    return {
        "api_type": "json",
        "thing_id": thing_id,       # fullname del post o comentario
        "text": texto,
        "return_rtjson": True       
    }