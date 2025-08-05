# src/logs/logger.py
import logging

# Crear y configurar el logger
logger = logging.getLogger("reddit_tests")
logger.setLevel(logging.DEBUG)

# Formato de los logs
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Handler para archivo
file_handler = logging.FileHandler("test_logs.log", mode='w')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# (Opcional) Handler para consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
