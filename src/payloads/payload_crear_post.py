

def get_create_post_payload(
    subreddit: str = None,
    title: str = None,
    text: str = "Contenido de ejemplo",
    api_type: str = "json"
) -> dict:
    """
    Retorna el payload para crear un post en Reddit, permitiendo omitir campos opcionalmente.
    :param subreddit: Nombre del subreddit o perfil (ej: u_usuario)
    :param title: Título del post
    :param text: Texto del post
    :param api_type: Tipo de respuesta esperada por Reddit API (default 'json')
    :return: Diccionario con el payload
    """
    payload = {
        'kind': 'self',  # siempre es self por defecto (texto)
        'text': text
    }

    if api_type is not None:
        payload['api_type'] = api_type
    if subreddit is not None:
        payload['sr'] = subreddit
    if title is not None:
        payload['title'] = title

    return payload

