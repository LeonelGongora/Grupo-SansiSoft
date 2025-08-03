error_schema = {
    "type": "object",
    "properties": {
        "error": {"type": "integer"},
        "message": {"type": "string"},
        "reason": {"type": "string"}
    },
    "required": ["error", "message"]
}