import logging

logging.basicConfig(level=logging.INFO, filename="program_log.log", filemode="w", format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('Програма успішно запущена')