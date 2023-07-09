import json
from abc import ABC, abstractmethod


class FileSaver(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(FileSaver):
    """
    Класс для сохранения и работы с вакансиями из JSON файла
    """
    def __init__(self, path):
        """
        :param path: путь к JSON файлу
        """
        self.vacancy_list = []
        self.path = path

    def add_vacancy(self, vacancy_obj_list):
        """
        Сохраняет в JSON файл вакансии, исходя из списка объектов класса Vacancy,
        путь берется из созданного объекта JSONSaver
        :param vacancy_obj_list: список объектов класса Vacancy
        :return:
        """
        for vacancy_obj in vacancy_obj_list:
            vacancy_dict = {'name': vacancy_obj.name, 'url': vacancy_obj.url, 'salary_min': vacancy_obj.salary_min,
                            'salary_max': vacancy_obj.salary_max, 'description': vacancy_obj.description,
                            'website': vacancy_obj.website}
            self.vacancy_list.append(vacancy_dict)
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(self.vacancy_list, file, ensure_ascii=False, indent=4)

    def get_vacancies_by_salary(self, salary: int):
        """
        Выводит на экран вакансии с зарплатой, выше заданной
        :param salary: зарплата
        :return:
        """
        with open(self.path, "r", encoding="utf-8") as file:
            temp = json.load(file)
            for item in temp:
                if item['salary_min'] >= salary:
                    print(item['website'], item['name'], item['url'],
                          item['salary_min'], item['salary_max'], item['description'],)

    def delete_vacancy(self):
        """
        Очищает файл с вакансиями, путь берется из созданного объекта JSONSaver
        :return:
        """
        with open(self.path, "w", encoding="utf-8") as file:
            file.write('')
