# Pruebas Automatizadas para la API de Reddit

## Descripción de la Aplicación

La plataforma **Reddit** es una red social en la que los usuarios pueden crear publicaciones, votar, comentar y participar en comunidades (subreddits) sobre una amplia variedad de temas.

Este repositorio contiene un conjunto de **pruebas automatizadas** para validar el comportamiento de la API de Reddit utilizando Postman y Pytest.

---

## Tipos de Pruebas Incluidas

- **Exploratorias**:
  - Colecciones de pruebas disponibles en el archivo [`colecciones_postman.json`](./colecciones_postman.json).
- **Smoke Tests**:
- Validan que los endpoints más importantes estén funcionando correctamente.
- **Pruebas Funcionales**:
  - Verifican que cada funcionalidad de la API cumpla con los requerimientos esperados.
- **Pruebas de Regresión**:
  - Aseguran que nuevas modificaciones no afecten funcionalidades ya implementadas.

---

## Funcionalidades Probadas

### Subreddits

- Crear un nuevo subreddit.
- Obtener información de un subreddit existente.

### Feeds Personalizados

- Obtener lista de moderadores de un subreddit.
- Suscribirse a un subreddit.

### Publicaciones y Comentarios

- Crear una nueva publicación.
- Obtener información de un post específico.
- Comentar en un post.
- Obtener información de un comentario.

### Usuarios

- Añadir un amigo.
- Eliminar un amigo.
- Reportar a un usuario.
- Obtener información de un usuario.

---

## Cómo Ejecutar las Pruebas

1. Clona el repositorio:
   ```bash
   git clone https://github.com/usuario/tu-repositorio.git
   cd tu-repositorio
