#  Основные настройки
import logging
import os

#  Корневая директория проекта
ROOT_DIR = os.path.dirname(__file__)

#  Путь до XLSX-файла
PATH_TO_FILE = os.path.join(ROOT_DIR, "data", "vacancies.json")

#  Путь к создаваемому файлу
NEW_PATH_TO_FILE = os.path.join(ROOT_DIR, "data")


#  Настройки для логгера
def setup_logger(name: str, log_file: str) -> logging.Logger:
    """Настойка логгера, включает метку времени,
    название модуля, уровень серьезности и сообщение,
    описывающее событие или ошибку, которая произошла."""
    logger = logging.getLogger(name)
    file_handler = logging.FileHandler(log_file, "w", encoding="UTF-8")
    file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger


if __name__ == "__main__":
    print(ROOT_DIR)
    print()
    print(PATH_TO_FILE)
    print()
    print(NEW_PATH_TO_FILE)
