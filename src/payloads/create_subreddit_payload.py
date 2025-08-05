def get_create_subreddit_payload(name, description="Este es un subreddit de prueba", subreddit_type="public", lang="en"):
    return {
        "name": name,
        "title": name,
        "public_description": description,
        "description": description,
        "sr": name,
        "type": subreddit_type,
        "lang": lang,
        "link_type": "any",
        "submit_text": "Bienvenido a este subreddit",
        "wiki_edit_age": 0,
        "wiki_edit_karma": 0,
        "api_type": "json"
    }
