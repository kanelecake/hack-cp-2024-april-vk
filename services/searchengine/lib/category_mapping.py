mapping = {
    0: 'Документы',
    1: 'Организация уроков',
    2: 'Оценки',
    3: 'Перевод/ запись в группу',
    4: 'Портал',
    5: 'Практические работы',
    6: 'Программа обучения',
    7: 'Расписание',
    8: 'Требования ПО',
    9: 'Трудоустройство',
}


def map_category_to_string(category):
    try:
        return mapping[category]
    except KeyError:
        print("Invalid category")
        return 0
