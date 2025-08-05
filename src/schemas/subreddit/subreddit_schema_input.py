# Schema de entrada para crear un subreddit
input_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "title": {"type": "string"},
        "public_description": {"type": "string"},
        "description": {"type": "string"},
        "lang": {"type": "string"},
        "type": {"type": "string"},
        "link_type": {"type": "string"},
        "api_type": {"type": "string"}
    },
    "required": ["name", "title", "api_type"]
}
