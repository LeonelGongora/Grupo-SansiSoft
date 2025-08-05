def crear_payload_añadir_amigo(username = None):
    if username is None:
        return {}
    return {
        "name": username
    }
