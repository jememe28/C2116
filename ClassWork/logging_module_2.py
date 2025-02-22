import logging

logging.basicConfig(level=logging.ERROR, filename="error_log.log", filemode="a", format='%(asctime)s - %(levelname)s - %(message)s')

try:
    result = 10 / 0
except Exception as e:
    logging.error(f'Виникла помилка: {e}', exc_info=True)