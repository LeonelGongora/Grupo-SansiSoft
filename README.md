# Pruebas Automatizadas para la API de Reddit

## Descripción de la Aplicación

La plataforma **Reddit** es una red social en la que los usuarios pueden crear publicaciones, votar, comentar y participar en comunidades (subreddits) sobre una amplia variedad de temas.

Este repositorio contiene un conjunto de **pruebas automatizadas** para validar el comportamiento de la API de Reddit utilizando Pytest.

---

## Tipos de Pruebas Incluidas

- **Exploratorias**:
  - Colecciones de pruebas disponibles en el archivo `colecciones_postman.json`.
- **Smoke Tests**:
- Comprenden los test cases que prueban el happy path.
- **Pruebas Funcionales**:
  - Verifican que cada funcionalidad de la API cumpla con los requerimientos esperados, basandose en la documentacion.
- **Pruebas de Regresión**:
  - Comprende todas las pruebas realizadas.

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
   git clone --branch development https://github.com/LeonelGongora/Grupo-SansiSoft.git
   ```
   
2. Crear entorno virtual
   ```bash
   python -m venv .venv
   ```

3. Acceder al entorno virtual
   ```bash
   .\.venv\Scripts\Activate.ps1
   ```
   
4. Instalar los modulos requeridos con requirements.txt
   ```bash
   pip install -r requirements.txt
   ```

5. Ejecuta las pruebas de Pytest en la raiz del proyecto :
   ```bash
   pytest
    ```
