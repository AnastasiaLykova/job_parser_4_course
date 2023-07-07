import json
import os
from abc import ABC, abstractmethod
import requests
from src.vacancy import Vacancy


class JobSearchAPI(ABC):
    """
    Класс для обращения к сайтам по API
    """
    @abstractmethod
    def get_vacancies(self, text_for_search: str, page, per_page):
        pass


class HeadHunterAPI(JobSearchAPI):
    """
    Класс для обращения к сайту HH
    """
    def get_vacancies(self, keyword: str, page=0, per_page=5):
        """
        Обращается к сайту HH,
        после получения ответа запускает инициализацию
        объектов Vacancy
        :param keyword: слово-запрос
        :param page: количество страниц
        :param per_page: количество вакансий на странице
        :return:
        """
        url = "https://api.hh.ru/vacancies"
        headers = {"User-Agent": "Anastasia Lykova"}
        for number in range(0, page+1):
            params = {"text": keyword, "area": 113, "page": number, "per_page": per_page}
            response = requests.get(url, params=params, headers=headers)
            response = response.content.decode()
            json_hh = json.loads(response)
            Vacancy.init_vacancy_hh(json_hh)


class SuperJobAPI(JobSearchAPI):
    """
    Класс для обращения к сайту SuperJob
    """
    def get_vacancies(self, keyword: str, page=0, per_page=5):
        """
        Обращается к сайту SuperJob,
        после получения ответа запускает инициализацию
        объектов Vacancy
        :param keyword: слово-запрос
        :param page: количество страниц
        :param per_page: количество вакансий на странице
        :return:
        """
        api_key: str = os.getenv('API_KEY_SJ')
        headers = {"X-Api-App-Id": api_key}
        url = "https://api.superjob.ru/2.0/vacancies"
        for number in range(0, page + 1):
            params = {"keyword": keyword, "page": number, "count": per_page, "app_key": api_key}
            response = requests.get(url, params=params, headers=headers)
            response = response.content.decode()
            json_sj = json.loads(response)
            Vacancy.init_vacancy_sj(json_sj)
