from src.vacancy import Vacancy
from src.vacancy_api import HeadHunterApi
from src.vacancy_file import JobFile


def get_vacancies_by_salary_from(vacancies: list[Vacancy], salary_from: int) -> list[Vacancy]:
    """Возвращает список вакансий в заданном диапазоне зарплат."""

    return [vac for vac in vacancies if vac.salary >= salary_from]


def sort_vacancies_by_salary(vacancies: list[Vacancy]) -> list[Vacancy]:
    """Сортирует вакансии по зарплате."""

    return sorted(vacancies, key=lambda vacancy: vacancy.salary, reverse=True)


def get_top_vacancies(vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    """Возвращает топ N вакансий по зарплате."""
    sorted_vacancies = sort_vacancies_by_salary(vacancies)

    return sorted_vacancies[:top_n]


if __name__ == "__main__":
    hh_api = HeadHunterApi()
    vac = JobFile()
    load_vac = hh_api.load_vacancies("java")
    vac.save_vacancy_file(load_vac)
    jb = vac.read_new_vacancy_file()

    # print(sort_vacancies_by_salary(load_vac))
    # print(print_vacancy(load_vac))
    # print(load_vac_file)
    # print(get_vacancies_area(jb, "москва"))
