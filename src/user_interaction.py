from src.job_search_api import HeadHunterAPI, SuperJobAPI
from src.vacancy import Vacancy
from src.vacancy_to_file import JSONSaver
from src.vacancy_selection import filter_vacancies, sort_vacancies, get_top_vacancies, print_vacancies


def user_interaction_filtration(obj_list):
    """
    Функция содержит фильтрацию уже полученных вакансий,
    использует объекты Vacancy
    :param obj_list: список объектов Vacancy
    :return:
    """
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = filter_vacancies(obj_list, filter_words)
    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


def user_interaction():
    """
    Функция для работы с пользователем
    :return:
    """
    search_query = input("Введите поисковый запрос: ")
    page = int(input("Введите количество страниц: ")) - 1
    per_page = int(input("Введите количество вакансий на странице: "))
    user_path = input("Введите название файла JSON: ").strip(".,:;-!?") + '.json'

    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    hh_api.get_vacancies(search_query, page, per_page)
    superjob_api.get_vacancies(search_query, page, per_page)

    json_saver = JSONSaver(user_path)
    json_saver.add_vacancy(Vacancy.vacancy_obj_list)

    obj_list = Vacancy.vacancy_obj_list
    user_interaction_filtration(obj_list)


def user_interaction_from_file():
    """
    Функция для работы с пользователем и объектами из файла JSON
    :return:
    """
    user_path = input("Введите название файла JSON: ").strip(".,:;-!?") + '.json'

    JSONSaver(user_path)
    Vacancy.init_vacancy_from_json(user_path)
    obj_list = Vacancy.vacancy_obj_list
    user_interaction_filtration(obj_list)
