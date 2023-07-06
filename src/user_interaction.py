from src.job_search_api import HeadHunterAPI, SuperJobAPI
from src.vacancy import Vacancy
from src.vacancy_to_file import JSONSaver
from src.vacancy_selection import filter_vacancies, sort_vacancies, get_top_vacancies, print_vacancies


def user_interaction():
    """
    Функция для работы с пользователем
    :return:
    """
    search_query = input("Введите поисковый запрос: ")
    page = int(input("Введите количество страниц, первая нулевая: "))
    per_page = int(input("Введите количество вакансий на странице: "))
    user_path = input("Введите название файла JSON: ") + '.json'

    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    hh_api.get_vacancies(search_query, page, per_page)
    superjob_api.get_vacancies(search_query, page, per_page)

    json_saver = JSONSaver(user_path)
    json_saver.add_vacancy(Vacancy.vacancy_obj_list)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = filter_vacancies(Vacancy.vacancy_obj_list, filter_words)
    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)
