def filter_vacancies(vacancies, filter_words):
    """
    Функция получает список объектов класса Vacancy, возвращает
    отфильтрованный список, содержащий слова filter_words
    :param vacancies: список с объектами класса Vacancy
    :param filter_words: список со словами для поиска
    :return: список объектов, содержащих в описании хотя бы одно слово
    """
    filtered_vacancies = []
    for vacancy in vacancies:
        for word in filter_words:
            if word.lower() in vacancy.description.lower():
                filtered_vacancies.append(vacancy)
                break
    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
    return filtered_vacancies


def sort_vacancies(filtered_vacancies):
    """
    Сортирует список объектов класса Vacancy по минимальной зарплате,
    в порядке ее уменьшения. Вакансии без данных по зарплате попадают
    в конец списка
    :param filtered_vacancies: список с объектами класса Vacancy
    :return: отсортированный по минимальной зарплате список объектов
    """
    sort_vacancies = sorted(filtered_vacancies, key=lambda x: x.salary_min, reverse=True)
    return sort_vacancies


def get_top_vacancies(sorted_vacancies, top_n):
    """
    Возвращает top_n объектов класса Vacancy
    :param sorted_vacancies: список с объектами класса Vacancy
    :param top_n: количество возвращаемых вакансий
    :return: возвращает первые top_n объектов класса Vacancy
    """
    top_vacancies = sorted_vacancies[:top_n]
    return top_vacancies


def print_vacancies(top_vacancies):
    """
    Выводит на экран str метод для объектов класса Vacancy
    :param top_vacancies: список с объектами класса Vacancy
    :return:
    """
    for item in top_vacancies:
        print(item)
