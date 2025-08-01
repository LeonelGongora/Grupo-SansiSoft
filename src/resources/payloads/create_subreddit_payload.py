def get_create_subreddit_payload(name):
    return {
        "name": name.strip(),
        "title": "Subreddit de prueba para QA",
        "public_description": "Este es un subreddit de prueba automatizada",
        "type": "public",
        "link_type": "any",
        "lang": "es",
        "api_type": "json"
    }
