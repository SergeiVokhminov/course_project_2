from src.vacancy import Vacancy
from src.vacancy_filter import get_top_vacancies, get_vacancies_by_salary_from, sort_vacancies_by_salary


def test_get_vacancies_by_salary_from(vacancies_objects):
    assert get_vacancies_by_salary_from(vacancies_objects, 500000) == []
    assert get_vacancies_by_salary_from(vacancies_objects, 20000) == [
        Vacancy("123323", "Программист_3", "https://test_3", "Требования_3", "Обязанности_3", "Город_3", 20000)
    ]


def test_get_vacancies_by_salary_from_empty_list(vacancies_objects):
    assert get_vacancies_by_salary_from([], 1000000) == []


def test_get_vacancies_by_salary_from_0(vacancies_objects):
    assert get_vacancies_by_salary_from(vacancies_objects, 0) == vacancies_objects


def test_sort_vacancies_by_salary(vacancies_objects):
    res = sort_vacancies_by_salary(vacancies_objects)
    assert res[0].area == "Город_3"
    assert res[3].area == "Город_4"


def test_sort_vacancies_by_salary_empty_list():
    res = sort_vacancies_by_salary([])
    assert res == []


def test_get_top_vacancies(vacancies_objects):
    res = get_top_vacancies(vacancies_objects, 2)
    assert res == [
        Vacancy("123323", "Программист_3", "https://test_3", "Требования_3", "Обязанности_3", "Город_3", 20000),
        Vacancy("123322", "Программист_2", "https://test_2", "Требования_2", "Обязанности_2", "Город_2", 15000),
    ]


def test_get_top_vacancies_empty_list():
    res = get_top_vacancies([], 2)
    assert res == []


def test_get_top_vacancies_top_n_0(vacancies_objects):
    res = get_top_vacancies(vacancies_objects, 0)
    assert res == []
