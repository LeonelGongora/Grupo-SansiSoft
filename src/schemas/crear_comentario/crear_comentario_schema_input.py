input_schema ={
  "type": "object",
  "properties": {
    "api_type": {
      "type": "string"
    },
    "thing_id": {
      "type": "string"
    },
    "text": {
      "type": "string"
    },
    "return_rtjson": {
      "type": "boolean"
    }
  },
  "required": [
    "api_type",
    "thing_id",
    "text",
    "return_rtjson"
  ]
}