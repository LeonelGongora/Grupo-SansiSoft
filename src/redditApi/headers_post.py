def get_create_post_headers(
    token: str = None,
    user_agent: str = None,
    content_type: str = "application/x-www-form-urlencoded"
) -> dict:
    """
    Retorna un diccionario de headers para crear un post, permitiendo omitir campos opcionalmente.
    :param token: Token de autorización (Bearer token)
    :param user_agent: Cadena identificadora del cliente
    :param content_type: Tipo de contenido del body (por defecto: application/x-www-form-urlencoded)
    :return: Diccionario con los headers
    """
    headers = {}

    if token is not None:
        headers['Authorization'] = f"bearer {token}"
    if user_agent is not None:
        headers['User-Agent'] = user_agent
    if content_type is not None:
        headers['Content-Type'] = content_type

    return headers
