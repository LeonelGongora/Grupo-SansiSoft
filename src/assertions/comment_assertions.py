from urllib import response


def assert_comentario_creado(response):
    assert response.status_code == 200, f"Status code inesperado: {response.status_code}"
    json_resp = response.json()
     #print("Respuesta JSON:", json_resp)
    # Validaciones básicas que indican que es un comentario
    assert "body" in json_resp, "No se encontró el campo 'body' en la respuesta"
    assert "id" in json_resp, "No se encontró el campo 'id' en la respuesta"
    assert "author" in json_resp, "No se encontró el campo 'author' en la respuesta"
    assert json_resp["body"].strip() != "", "El cuerpo del comentario está vacío"
    
    print("✅ Comentario creado correctamente.")


def assert_comentario_post_invalido(respuesta):
   
    assert respuesta.status_code in [403, 404], f"Se esperaba código 403 o 404, pero fue {respuesta.status_code}" 
  