import json
import os
from abc import ABC

from typing import Any
from config import NEW_PATH_TO_FILE, PATH_TO_FILE
from src.base_vacancy import ReadWriteFile
from src.vacancy import Vacancy
from src.vacancy_api import HeadHunterApi


class JobFile(ReadWriteFile, ABC):
    """Класс по работе с JSON-файлами."""

    filename: str

    def __init__(self, filename: str = "vacan.json"):
        self.filename = filename
        self.path_file = os.path.join(NEW_PATH_TO_FILE, filename)

    @staticmethod
    def read_file() -> Any:
        """Читает данные из стандартного JSON-файла."""
        try:
            with open(PATH_TO_FILE, "r", encoding="UTF-8") as f:
                try:
                    # my_logger.info("Открытие файла")
                    data_file = json.load(f)
                    return data_file
                except json.JSONDecodeError:
                    # my_logger.error("Возникла ошибка при обработке файла! Неверный формат файла")
                    return []
        except FileNotFoundError:
            # my_logger.error("Файл не найден")
            return []

    def save_vacancy_file(self, vacancies: list[dict]) -> None:
        """Сохраняет данные в JSON-файл."""
        with open(self.path_file, "w", encoding="UTF-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def read_new_vacancy_file(self):
        """Читает данные из нового JSON-файла."""
        # print(self.path_file)
        with open(self.path_file, encoding="UTF-8") as f:
            data_file_new = json.load(f)
            return data_file_new

    def delete_file(self) -> None:
        """Удаление данных из нового JSON-файла."""
        open(self.path_file, "w").close()

    def get_vacancy_by_vacancy_name(self, word: str) -> list[Vacancy]:
        """Возвращает список вакансий по ключевому слову в названии вакансии."""
        found_vacancies = []

        for vac in self.read_new_vacancy_file():
            if word in vac.get("area").lower():
                found_vacancies.append(vac)

        return Vacancy.cast_to_object_list(found_vacancies)


if __name__ == "__main__":
    user_file = JobFile.read_file()
    print(user_file)
    print(len(user_file))
    print()
    us = HeadHunterApi()
    vacancies = us.load_vacancies("python")
    # print(vacancies)
    new_vac = JobFile()
    read_new_file = new_vac.read_new_vacancy_file()
    print(read_new_file)
