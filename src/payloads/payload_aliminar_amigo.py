def crear_payload_eliminar_amigo(id = None):
    if id is None:
        return {}
    return {
        "id": id
    }
