#ID : US001
#Título:Obtener los datos de celular con id de 10
#Descripción
#El usuario de poder obtener los datos de celulares con su nombre,"id","name","data": , "Capacity":, "Screen size":
#ejem.
#{
#        "id": "5",
#         "name": "Samsung Galaxy Z Fold2",
#         "data": {
#             "price": 689.99,
#             "color": "Brown"
#         }
# Precondiciones
# El id del celular debe estar registrado
# ejem.10
# En caso de no estar creado
# 1ro se debe seleccionar con la llamada Post
# 2do  ingresar el url https://api.restful-api.dev/objects en el campo al lado de “Post”
# 3ro Estar en la seccion de “Body” con la opción de “raw”
# 4to  ingresar en el campo de abajo
# {"id": "10","name": "Apple iPad Mini 5th Gen", "data": { "Capacity": "64 GB", "Screen size": 7.9 }}
# 5to  presionar el botón de “send”
# Ambiente
# Tener acceso a https://api.restful-api.dev/objects?id=3&id=5&id=10
# Tener instalado Postman
# Pasos
# Ingresar a Postman
# Seleccionar la llamada “Get”
# Copiar el URL https://api.restful-api.dev/objects?id=3&id=5&id=10
# Pegar el URL en el campo alado de “Get”
# Presionar el botón Send
# Comparar la salida con los datos que se ingresaron anteriormente
# Resultado Esperado
# [
#     {
#         "id": "3",
#         "name": "Apple iPhone 12 Pro Max",
#         "data": {
#             "color": "Cloudy White",
#             "capacity GB": 512
#         }
#     },
#     {
#         "id": "5",
#         "name": "Samsung Galaxy Z Fold2",
#         "data": {
#             "price": 689.99,
#             "color": "Brown"
#         }
#     },
#     {
#         "id": "10",
#         "name": "Apple iPad Mini 5th Gen",
#         "data": {
#             "Capacity": "64 GB",
#             "Screen size": 7.9
#         }
#     }
# ]
#
# Evidencia
# cUrl:
# curl --location 'https://api.restful-api.dev/objects?id=3&id=5&id=10'
#
#
# Prioridad
# Low
# Post condición
# Eliminar el objeto creado en la precondición
