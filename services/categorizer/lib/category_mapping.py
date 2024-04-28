mapping = {
    'Документы': 0,
    'Организация уроков': 1,
    'Оценки': 2,
    'Перевод/ запись в группу': 3,
    'Портал': 4,
    'Практические работы': 5,
    'Программа обучения': 6,
    'Расписание': 7,
    'Требования ПО': 8,
    'Трудоустройство': 9
}


def map_category_to_int(category):
    try:
        return mapping[category]
    except KeyError:
        print("Invalid category")
        return 0
