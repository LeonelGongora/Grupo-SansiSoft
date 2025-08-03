# src/logs/logger.py
import logging

# Configurar el logger
logger = logging.getLogger("reddit_tests")
logger.setLevel(logging.DEBUG)  # Cambia a INFO o WARNING si no quieres tanto detalle

# Crear un handler para escribir en archivo
file_handler = logging.FileHandler("test_logs.log", mode='w')  # modo 'w' para sobrescribir en cada run
file_handler.setLevel(logging.DEBUG)

# Crear un formato de log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Agregar el handler al logger
logger.addHandler(file_handler)
