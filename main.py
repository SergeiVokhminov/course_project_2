from src.vacancy import Vacancy
from src.vacancy_api import HeadHunterApi
from src.vacancy_file import JobFile
from src.vacancy_filter import get_top_vacancies, sort_vacancies_by_salary, get_vacancies_by_salary_from


def main() -> None:
    """
    Функция соединяет работу всех реализованных функций.
    :return: Результат работы реализованных функций.
    """

    #  Приветствие пользователя
    print("Привет. Я помогу тебе найти вакансии на HH.ru!")
    #  Получение от пользователя слова для поиска
    user_input = input("Введите ключевое слово для поиска: \n").lower()

    #  Создание экземпляра класса для работы с API сайта с вакансиями
    #  Получение вакансий с сайта HH
    hh_api = HeadHunterApi()
    vacancies = hh_api.load_vacancies(user_input)
    # print(vacancies)

    # Сохранение данных в JSON-файл
    save_vac = JobFile()
    save_vac.save_vacancy_file(vacancies)

    # Преобразование набора данных из JSON в список объектов
    # new_file = JobFile()
    vac_list = save_vac.read_new_vacancy_file()
    # print(vac_list)

    print(f"Найдено - {len(vacancies)} вакансий")

    print(
        """Могу предложить следующие манипуляции с полученными данными.
          1: Вывести весь результат.
          2: Отфильтровать по названию города и вывести на экран.
          3: Вывести на экран вакансии от указанной зарплаты.
          3: Отсортировать вакансии по убыванию зарплаты и вывести на экран.
          4: Вывести на экран топ N вакансий.
          0: Выйти из программы."""
    )

    while True:
        user_answer = input("Введите цифру: \n")
        if user_answer in ("1", "2", "3", "4", "0"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод.")

    menu = {
        "1": "Вывести весь результат.",
        "2": "Отфильтровать по названию города и вывести на экран.",
        "3": "Вывести на экран вакансии от указанной зарплаты.",
        "4": "Отсортировать вакансии по убыванию зарплаты и вывести на экран.",
        "5": "Вывести топ N вакансий.",
        "0": "Выйти из программы.",
    }

    print(f"Для обработки выбрано: {menu.get(user_answer)}\n")

    if user_answer == "1":
        for item in Vacancy.cast_to_object_list(vacancies):
            print(item)

    elif user_answer == "2":
        vacancy_city = input("Введите город России для поиска:\n").lower()
        for vac in save_vac.get_vacancy_by_vacancy_name(vacancy_city):
            print(vac)

    elif user_answer == "3":
        try:
            salary_from = int(input("Укажите нижний порог зарплаты (целое число от 0):\n"))
        except ValueError:
            print("Некорректный ввод. Нижний порог не указан")
            salary_from = 0
        vacs_objects = Vacancy.cast_to_object_list(vacancies)
        for vac in get_vacancies_by_salary_from(vacs_objects, salary_from):
            print(vac)
            print()

    elif user_answer == "4":
        # user_answer = input("Введите да или нет: \n").lower()
        new_list_1 = Vacancy.cast_to_object_list(vacancies)
        for i in sort_vacancies_by_salary(new_list_1):
            if i.salary != 0:
                print(i)

    elif user_answer == "5":
        try:
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        except ValueError:
            print("Количество вакансий должно быть целым числом")
            print("По умолчанию будет выведено 5 вакансий\n")
            top_n = 5

        if top_n > len(vacancies):
            top_n = len(vacancies) - 1

        vacs_objects = Vacancy.cast_to_object_list(vacancies)

        for vac in get_top_vacancies(vacs_objects, top_n):
            print(vac)
            print()

    elif user_answer == "0":
        save_vac.delete_file()
        print("Работа программы завершена.")


if __name__ == "__main__":
    main()
