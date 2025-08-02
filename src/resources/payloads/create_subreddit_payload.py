def get_create_subreddit_payload(
    name,
    title=None,
    description="Subreddit de prueba automatizada",
    public_description="Descripción pública por defecto",
    subreddit_type="public"
):
    if not title:
        title = name
    return {
        "name": name,
        "title": title,
        "description": description,
        "public_description": public_description,
        "type": subreddit_type,
        "lang": "es",
        "over_18": False,
        "wikimode": "disabled",
        "allow_images": True,
        "allow_videos": True,
        "allow_post_crossposts": True
    }
