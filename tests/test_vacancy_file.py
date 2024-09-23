from src.vacancy_file import JobFile


def test_vacancy_file_init(file_name):
    """Тестирование инициализации"""
    assert JobFile(file_name).filename == "test_file_vacancy.json"
