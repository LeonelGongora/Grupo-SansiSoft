import requests
import requests.auth
import time

# Credenciales y configuración
client_id = "FG0BSiRZUdDsGeUqeefoMQ"
client_secret = "E4KXH6-Pz-ER1dYZvCBcYyJ0McwZzg"
username = "BrandonSt2025"
password = "ContraseniaDiplo123#"
user_agent = "testscript by u/BrandonSt2025"

# Autenticación básica
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

# Datos para obtener el token
data = {
    "grant_type": "password",
    "username": username,
    "password": password
}

headers = {"User-Agent": user_agent}

# Solicitar token
res = requests.post(
    "https://www.reddit.com/api/v1/access_token",
    auth=auth,
    data=data,
    headers=headers
)

# Validar respuesta
if res.status_code != 200:
    print("Error al obtener token:", res.status_code, res.text)
    exit()

# Procesar token
response_json = res.json()
token = response_json.get("access_token")
expires_in = response_json.get("expires_in")  # duración en segundos
hora_expira = time.time() + expires_in

print(f"✅ Token obtenido correctamente :)")
print(f"⏳ Expira en: {expires_in} segundos (~{expires_in//60} minutos)")

# Usar token para consultar tu perfil
headers["Authorization"] = f"bearer {token}"
me = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
if me.status_code == 200:
    print("👤 Información del usuario:")
    print(me.json().get("name", "Nombre de usuario no disponible"))
else:
    print("❌ Error al consultar información del usuario:", me.status_code)




