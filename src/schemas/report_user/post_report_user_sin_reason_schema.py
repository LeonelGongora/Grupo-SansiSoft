schema_report_user_sin_razon = {
  "type": "object",
  "properties": {
    "user": {
      "type": "string"
    },
    "reason": {
      "type": "string"
    },
    "details": {
      "type": "object",
      "description": "Optional additional details about the report",
      "additionalProperties": True
    }
  },
  "required": [
    "user",
  ]
}