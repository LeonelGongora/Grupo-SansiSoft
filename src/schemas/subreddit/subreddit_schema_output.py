output_schema = {
    "type": "object",
    "properties": {
        "json": {
            "type": "object",
            "properties": {
                "errors": {
                    "type": "array"
                },
                "data": {
                    "type": "object"
                }
            },
            "required": ["errors"],  # <--- Solo exigimos 'errors', no 'data'
        }
    },
    "required": ["json"]
}
