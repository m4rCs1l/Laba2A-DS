import random

def mk_group():
    global gender, eye_color, hair_color, animals, hobbies, age, names
    group = {}

    for name in names:
        if ('Анастасия' in name) or ('Екатерина' in name) or ('Елена' in name) or ('Яна' in name) or ('Анна' in name) or ('Саина' in name) or ('Наталья' in name) or ('Мария' in name):
            group[name] = ['девочка', random.choice(eye_color), random.choice(hair_color), random.choice(animals), random.choice(hobbies), random.choice(age)]
        else:
            group[name] = ['мальчик', random.choice(eye_color), random.choice(hair_color), random.choice(animals), random.choice(hobbies), random.choice(age)]

    for name1 in names:
        a = group.get(name1)
        for name2 in names:
            b = group.get(name2)
            if name1 != name2 and a == b:
                mk_group()
    return group

gender = ['мальчик', 'девочка']
eye_color = ['карие', 'голубые', 'зеленые', 'серые']
hair_color = ['блонд', 'светлые', 'темные', 'черные']
animals = ['кошки', 'не любит животных', 'морские свинки', 'собаки']
hobbies = ['рисовать', 'читать', 'боксировать', 'смотреть фильмы', 'путешествовать', 'играть на гитаре', 'кататься на велосипеде', 'петь', 'играть на фортепиално', 'фотографировать', 'играть в баскетбол', 'программировать']
age = ['17', '18', '19']
names = ['Бакланова Анастасия', 'Белоконь Иван', 'Волкович Кирилл', 'Гневашев Андрей', 'Горлов Андрей', 'Гусева Екатерина', 'Долгов Константин', 'Драчева Елена', 'Еремеев Арсений', 'Зорина Яна', 'Иванова Анна', 'Калинин Артур', 'Копытко Александр', 'Королева Анастасия', 'Крылов Дан', 'Ложкин Максим', 'Максимов Арсений', 'Николаева Саина', 'Панин Михаил', 'Погорелов Сергей', 'Райнус Анастасия', 'Сергеев Артём', 'Суслопаров Виталий', 'Таргович Наталья', 'Теребов Максим', 'Улитина Мария', 'Ульянова Екатерина', 'Фаед Зиад', 'Юриков Святослав']




group = mk_group()
print(group)

character = []
print('Начнем игру! Загадайте своего одногруппника!')

for gen in gender:
    flag = input(f'Пол загаданного одногруппника - {gen} (да/нет): ').lower().strip()
    if flag == 'да':
        character.append(gen)
        break

for eye in eye_color:
    flag = input(f'Цвет глаз загаданного одногруппника - {eye} (да/нет): ').lower().strip()
    if flag == 'да':
        character.append(eye)
        break

for col in hair_color:
    flag = input(f'Цвет волос загаданного одногруппника - {col} (да/нет): ').lower().strip()
    if flag == 'да':
        character.append(col)
        break

for an in animals:
    flag = input(f'Отношение к животным (любит ... / не любит животных) - {an} (да/нет): ').lower().strip()
    if flag == 'да':
        character.append(an)
        break

for hobbie in hobbies:
    flag = input(f'Хобби студента - {hobbie} (да/нет): ').lower().strip()
    if flag == 'да':
        character.append(hobbie)
        break

for ag in age:
    flag = input(f'Студенту {ag} лет (да/нет): ').lower().strip()
    if flag == 'да':
        character.append(ag)
        break

for name in names:
    if group.get(name) == character:
        break

print(f'Вы загадали одногруппника: {name}')

