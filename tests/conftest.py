import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancies_dict():
    vacs = [
        {
            "id": "123321",
            "title": "Программист_1",
            "url": "https://test_1",
            "requirement": "Требования_1",
            "description": "Обязанности_1",
            "area": "Город_1",
            "salary": 10000,
        },
        {
            "id": "123321",
            "name": "Программист_2",
            "url": "https://test_2",
            "requirement": "Требования_2",
            "description": "Обязанности_2",
            "area": "Город_2",
            "salary": 15000,
        },
    ]

    return vacs


@pytest.fixture
def vacancies_objects():
    vacs = [
        Vacancy("123321", "Программист_1", "https://test_1", "Требования_1", "Обязанности_1", "Город_1", 10000),
        Vacancy("123322", "Программист_2", "https://test_2", "Требования_2", "Обязанности_2", "Город_2", 15000),
        Vacancy("123323", "Программист_3", "https://test_3", "Требования_3", "Обязанности_3", "Город_3", 20000),
        Vacancy("123324", "Программист_4", "https://test_4", "Требования_4", "Обязанности_4", "Город_4", 0),
    ]

    return vacs


@pytest.fixture
def file_name():
    return "test_file_vacancy.json"
