from src.vacancy_api import HeadHunterApi


def test_head_hunter_api():
    hh_api = HeadHunterApi()
    assert hh_api.url == "https://api.hh.ru/vacancies"
    vacs = hh_api.load_vacancies("python")
    assert len(vacs) == 1000
