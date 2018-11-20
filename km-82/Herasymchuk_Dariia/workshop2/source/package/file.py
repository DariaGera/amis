smth = [
    {
        'name': 'Bob',
        'age': 20,
        'marks': {
            'Math': 98,
            'Python': 100
        }
    },

    {
        'name': 'Boba',
        'age': 19,
        'marks': {
            'Physics': 98
        }
    },

    {
        'name': 'Boban',
        'age': 22,
        'marks': {
        }
    }
]

i = 0
max_age = smth[i]['age']


def maxAge(smth):
    global i  # глобальна змінна, яка існує і поза функцією
    global max_age  # глобальна змінна

    if i == len(smth) - 1:  # елементи списку
        print(max_age)
        return 0
    else:
        i = i + 1

    if max_age < smth[i]['age']:  # йде порівнювання
        max_age = smth[i]['age']
        maxAge(smth)
    else:
        maxAge(smth)


maxAge(smth)


def addMark(smth, name, disc, mark):
    for i in (0, len(smth)):
        student['name'] == name:
        student['mark'][disc] = mark


return addMark(smth, 'Boban', 'Math', 75)
print(smth)


def getNames(smth):
    a = []  # створюємо порожній список для подальшої роботи
    for i in range(0, len(smth)):
        a.append(smth[i]['name'])  # добавляє в кінець списку
    return a


print(getNames(smth))


