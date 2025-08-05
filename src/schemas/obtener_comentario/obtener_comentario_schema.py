obtener_comentario_schema = {
    "type": "object",
    "properties": {
        "kind": {"type": "string"},
        "data": {
            "type": "object",
            "properties": {
                "children": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "kind": {"type": "string"},
                            "data": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "string"},
                                    "body": {"type": "string"},
                                    "author": {"type": "string"},
                                    "created_utc": {"type": "number"},
                                    "score": {"type": "integer"},
                                    "subreddit": {"type": "string"}
                                },
                                "required": [
                                    "id", "body", "author", "created_utc", "score", "subreddit"
                                ]
                            }
                        },
                        "required": ["kind", "data"]
                    }
                }
            },
            "required": ["children"]
        }
    },
    "required": ["kind", "data"]
}