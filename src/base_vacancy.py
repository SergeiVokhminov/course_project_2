from abc import ABC, abstractmethod

# from src.vacancy import Vacancy


class Parser(ABC):
    """Абстрактный класс по работе с API сервисом."""

    @abstractmethod
    def load_vacancies(self, keyword: str) -> list[dict]:
        pass


class ReadWriteFile(ABC):
    """Абстрактный класс по чтению/записи файла."""

    @abstractmethod
    def read_new_vacancy_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass
