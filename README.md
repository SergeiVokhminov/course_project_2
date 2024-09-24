# Второй курсовой проект

## Описание.
Приложение для поиска вакансий на HH.ru

## Модули и функции реализованные в проекте.
1. bace_vacancy - реализованы абстрактные классы
2. vacancy - класс для представления вакансии
3. vacancy_api - класс по работе с API
4. vacancy_file - класс для работы с JSON-файлом
5. vacancy_filter - функции для обработки полученных данных

## Используемые зависимости.

- black==24.8.0
- certifi==2024.7.4
- charset-normalizer==3.3.2
- click==8.1.7
- coverage==7.6.1
- et-xmlfile==1.1.0
- flake8==7.1.1
- idna==3.7
- iniconfig==2.0.0
- isort==5.13.2
- mccabe==0.7.0
- mypy==1.11.1
- mypy-extensions==1.0.0
- numpy==2.0.1
- openpyxl==3.1.5
- packaging==24.1
- pandas==2.2.2
- pathspec==0.12.1
- platformdirs==4.2.2
- pluggy==1.5.0
- pycodestyle==2.12.1
- pyflakes==3.2.0
- pytest==8.3.2
- pytest-cov==5.0.0
- python-dateutil==2.9.0.post0
- python-dotenv==1.0.1
- pytz==2024.1
- requests==2.32.3
- six==1.16.0
- typing_extensions==4.12.2
- tzdata==2024.1
- urllib3==2.2.2

## Установка

1. Клонируйте репозиторий:
'''
git clone https://github.com/SergeiVokhminov/course_project_1.git
'''

2. Установите зависимости:
```
poetry install
```

## Тестирование:

1. в проекте используется фреймворк тестирования "pytest".
2. для запуска тестов выполните команду: "pytest"
3. для просмотра покрытия тестов, выполните команду: pytest --cov

## Использование модуля main.py:

1. Откройте модуль
2. Запустите if __name__ == "__main__"

## Документация

Для получения дополнительной информации обратитесь к [документации](README.md)