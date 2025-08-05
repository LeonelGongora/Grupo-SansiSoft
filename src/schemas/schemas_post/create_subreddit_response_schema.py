import json
import os

def get_schema():
    ruta = os.path.join(os.path.dirname(__file__), "create_subreddit_response_schema.json")
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)
