import requests

from src.base_vacancy import Parser


class HeadHunterApi(Parser):
    """Класс для работы с API."""

    def __init__(self) -> None:
        """Инициализатор класса HeadHunterApi."""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 50}
        self.__vacancies: list[dict] = []

    @property
    def url(self) -> str:
        """Возвращает свойство url."""
        return self.__url

    def __api_connect(self) -> requests.Response:
        """Метод проверки подключения к API hh.ru"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code == 200:
            return response
        else:
            print("Ошибка при получении данных", response.status_code)

    def load_vacancies(self, keyword: str) -> list[dict]:
        """Метод получения вакансий по ключевому слову."""
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = self.__api_connect()
            if response:
                vacancies = response.json()["items"]
                self.__vacancies.extend(vacancies)
                self.__params["page"] += 1
                # return vacancies
            else:
                break

        vacancies_list = []

        if self.__vacancies:
            # получение списка словарей с ключами id, name, url, requirement, description, area, salary
            for vacancy in self.__vacancies:
                id = vacancy.get("id")
                name = vacancy.get("name")
                url = vacancy.get("alternate_url")
                requirement = vacancy.get("snippet").get("requirement")
                description = vacancy.get("snippet").get("responsibility")
                area = vacancy.get("area").get("name")
                # salary = vacancy.get("salary")

                if vacancy.get("salary"):
                    if vacancy.get("salary").get("to"):
                        salary = vacancy.get("salary").get("to")
                    elif vacancy.get("salary").get("from"):
                        salary = vacancy.get("salary").get("from")
                else:
                    salary = 0

                vacancies_list.append(
                    {
                        "id": id,
                        "name": name,
                        "url": url,
                        "requirement": requirement,
                        "description": description,
                        "area": area,
                        "salary": salary,
                    }
                )

        return vacancies_list


if __name__ == "__main__":
    hh_api = HeadHunterApi()
    print(hh_api.load_vacancies("python"))
    print(len(hh_api.load_vacancies("python")))
