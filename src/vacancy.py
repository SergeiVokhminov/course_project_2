from typing import Any


class Vacancy:
    """Класс для представления вакансий"""

    __slots__ = ("id", "name", "url", "requirement", "description", "area", "salary")

    def __init__(
        self, id: str, name: str, url: str, requirement: str, description: str, area: str, salary: int | float
    ):
        self.id = id
        self.name = name
        self.url = url
        self.requirement = requirement
        self.description = description
        self.area = area
        self.salary = self.__salary_validation(salary)

    @staticmethod
    def __salary_validation(salary: int | float | None) -> int | float | None:
        """Валидация зарплаты"""
        if salary:
            return salary
        return 0

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list["Vacancy"]:
        """Возвращает список экземпляров Vacancy из списка словарей"""
        return [cls(**vac) for vac in vacancies]

    def __str__(self) -> Any:
        id = f"id - {self.id}"
        name = f"Название - {self.name}"
        url = f"Ссылка - {self.url}"
        requirement = f"Требование - {self.requirement}"
        description = f"Описание - {self.description}"
        area = f"Местоположение - {self.area}"
        salary = f"Зарплата - {self.salary}"
        return f"{id},\n{name},\n{url},\n{requirement},\n{description},\n{area},\n{salary}\n"

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def to_dict(self) -> dict:
        """Возвращает словарь с данными о вакансии из экземпляра класса Vacancy"""
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "requirement": self.requirement,
            "description": self.description,
            "area": self.area,
            "salary": self.salary,
        }


if __name__ == "__main__":
    vaca = Vacancy(
        "1245464352", "Python Developer", "hh.ru", "Опыт работы от 3 лет...", "Удаленная работа", "СПб", 170000
    )
    vaca_2 = Vacancy("1245464350", "Python", "hh_1.ru", "Опыт работы от 5 лет...", "Удаленная работа", "СПб", 100000)
    vac_list = [vaca, vaca_2]
    # print(sorted(vac_list))
    print(vac_list)
    print()
    print(vaca.to_dict())
    print()
    print(vaca)
