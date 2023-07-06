import json


class Vacancy:
    """
    Класс для создания объектов-вакансий
    """
    vacancy_obj_list = []

    def __init__(self, name, url, salary_min=0, salary_max=0, description=None, website=None):
        """
        :param name: название профессии
        :param url: веб адрес вакансии
        :param salary_min: минимальная зарплата
        :param salary_max: максимальная зарплата
        :param description: описание необходимых навыков
        :param website: сайт, с которого получена вакансия HH или SuperJob
        """
        self.name = name
        self.url = url
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.description = description
        self.website = website

    @classmethod
    def init_vacancy_from_json(cls, path):
        """
        Инициализация объектов из JSON файла
        :param path: путь к JSON файлу
        :return:
        """
        with open(path, "r", encoding="utf-8") as file:
            temp = json.load(file)
            for item in temp:
                name = item['name']
                url = item['url']
                salary_min = item['salary_min']
                salary_max = item['salary_max']
                description = item['description']
                website = item['website']
                vacancy = cls(name, url, salary_min, salary_max, description, website)
                cls.vacancy_obj_list.append(vacancy)

    @classmethod
    def init_vacancy_hh(cls, json_hh):
        """
        Инициализация объектов из JSON файла, полученного с HH
        :param json_hh: JSON файл
        :return:
        """
        for i in json_hh['items']:
            name = i['name']
            url = i['alternate_url']
            if i['salary'] is None:
                salary_min = 0
                salary_max = 0
            else:
                if i['salary']['from'] is None:
                    salary_min = 0
                else:
                    salary_min = i['salary']['from']
                if i['salary']['to'] is None:
                    salary_max = 0
                else:
                    salary_max = i['salary']['to']
            if i['snippet']:
                description = i['snippet']['requirement'][:170]
            else:
                description = None
            vacancy = cls(name, url, salary_min, salary_max, description, "HH")
            cls.vacancy_obj_list.append(vacancy)

    @classmethod
    def init_vacancy_sj(cls, json_sj):
        """
        Инициализация объектов из JSON файла, полученного с SuperJob
        :param json_sj: JSON файл
        :return:
        """
        for i in json_sj['objects']:
            name = i['profession']
            url = i['link']
            salary_min = i['payment_from']
            salary_max = i['payment_to']
            description = i['candidat'][:170]
            vacancy = cls(name, url, salary_min, salary_max, description, "SJ")
            cls.vacancy_obj_list.append(vacancy)

    def __str__(self):
        return f'{self.website}, {self.name}, {self.url}, {self.salary_min}, {self.salary_max}, {self.description}'

    def __lt__(self, other):
        """ метод для операции сравнения «меньше» """
        if issubclass(other.__class__, self.__class__):
            return self.salary_min < other.salary_min
        else:
            raise ValueError('Сравнивать можно только объекты Vacancy и дочерние от них.')

    def __le__(self, other):
        """  метод для операции сравнения «меньше или равно»"""
        if issubclass(other.__class__, self.__class__):
            return self.salary_min <= other.salary_min
        else:
            raise ValueError('Сравнивать можно только объекты Vacancy и дочерние от них.')

    def __gt__(self, other):
        """ метод для операции сравнения «больше» """
        if issubclass(other.__class__, self.__class__):
            return self.salary_min > other.salary_min
        else:
            raise ValueError('Сравнивать можно только объекты Vacancy и дочерние от них.')

    def __ge__(self, other):
        """ метод для операции сравнения «больше или равно» """
        if issubclass(other.__class__, self.__class__):
            return self.salary_min <= other.salary_min
        else:
            raise ValueError('Сравнивать можно только объекты Vacancy и дочерние от них.')

    def __eq__(self, other):
        """  определяет поведение оператора «равенства» """
        if issubclass(other.__class__, self.__class__):
            return self.salary_min == other.salary_min
        else:
            raise ValueError('Сравнивать можно только объекты Vacancy и дочерние от них.')
