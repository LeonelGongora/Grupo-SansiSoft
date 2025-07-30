# configuration/config.py
import time
import requests
import requests.auth

class RedditAuthConfig:
    def __init__(self, refresh_buffer=300):
        self.client_id = "FG0BSiRZUdDsGeUqeefoMQ"
        self.client_secret = "E4KXH6-Pz-ER1dYZvCBcYyJ0McwZzg"
        self.username = "BrandonSt2025"
        self.password = "ContraseniaDiplo123#"
        self.user_agent = "testscript by u/BrandonSt2025"
        self._base_url = "https://oauth.reddit.com/"
        self._token_url = "https://www.reddit.com/api/v1/access_token"
        self._token = None
        self._token_expiry = 0
        self.refresh_buffer = refresh_buffer  # ⏱ margen configurable en segundos

    def _get_new_token(self):
        print("🔐 Solicitando nuevo token...")
        auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        data = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
            "scope": "identity submit read vote edit save modflair privatemessages"
        }
        headers = {"User-Agent": self.user_agent}
        response = requests.post(self._token_url, auth=auth, data=data, headers=headers)
        if response.status_code != 200:
            raise Exception(f"❌ Error al obtener token: {response.status_code} - {response.text}")
        
        json_data = response.json()
        self._token = json_data.get("access_token")
        expires_in = json_data.get("expires_in", 86400)
        self._token_expiry = time.time() + expires_in - self.refresh_buffer
        print(f"✅ Token actualizado correctamente. Expira en {expires_in} segundos (buffer de {self.refresh_buffer}s).")

    def get_token(self):
        if not self._token or time.time() > self._token_expiry:
            self._get_new_token()
        return self._token

    def get_headers(self):
        return {
            "Authorization": f"bearer {self.get_token()}",
            "User-Agent": self.user_agent
        }

    @property
    def BASE_URL(self):
        return self._base_url

    @property
    def ACCESS_TOKEN(self):
        return self.get_token()

# Instancia lista para usar
reddit_auth = RedditAuthConfig(refresh_buffer=300)  # ⏱ margen de 5 minutos

BASE_URL = reddit_auth.BASE_URL
ACCESS_TOKEN = reddit_auth.ACCESS_TOKEN
