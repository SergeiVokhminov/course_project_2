from src.vacancy import Vacancy


def test_vacancy_init():
    vacs = Vacancy("122343", "Разработчик", "https://test", "Требования", "Обязанности", "Город", 10000)
    assert vacs.id == "122343"
    assert vacs.name == "Разработчик"
    assert vacs.url == "https://test"
    assert vacs.requirement == "Требования"
    assert vacs.description == "Обязанности"
    assert vacs.area == "Город"
    assert vacs.salary == 10000


def test_cast_to_object_list_empty_list():
    vacs = Vacancy.cast_to_object_list([])
    assert vacs == []


def test_vacancy_str():
    vac = Vacancy("122343", "Программист", "https://test", "Требования", "Обязанности", "Город", 10000)
    assert str(vac) == (
        "id - 122343,\nНазвание - Программист,\nСсылка - https://test,\nТребование - Требования,\n"
        "Описание - Обязанности,\nМестоположение - Город,\nЗарплата - 10000\n"
    )


def test_vacancy_str_salary_0():
    vac = Vacancy("122343", "Программист", "https://test", "Требования", "Обязанности", "Город", 0)
    assert str(vac) == (
        "id - 122343,\nНазвание - Программист,\nСсылка - https://test,\nТребование - Требования,\n"
        "Описание - Обязанности,\nМестоположение - Город,\nЗарплата - 0\n"
    )


def test_vacancy_eq(vacancies_objects):
    vac = Vacancy("123321", "Программист_1", "https://test_1", "Требования_1", "Обязанности_1", "Город_1", 10000)
    assert vacancies_objects[0] != vacancies_objects[1]
    assert vacancies_objects[0] == vac


def test_vacancy_lt(vacancies_objects):
    assert vacancies_objects[1] > vacancies_objects[0]
    assert vacancies_objects[0] < vacancies_objects[2]


def test_vacancy_le(vacancies_objects):
    assert vacancies_objects[0] >= vacancies_objects[3]
    assert vacancies_objects[1] <= vacancies_objects[2]
