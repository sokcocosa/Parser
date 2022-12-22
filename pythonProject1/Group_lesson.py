from bs4 import BeautifulSoup
import re

with open('Raspisanie.html') as file:
    source = file.read()
soup = BeautifulSoup(source, 'html.parser')


class Group_lesson(object):
    lessons = []

    def __init__(self, days, data, para, prepod, group, subject, type_occupation, place_classes):
        self.days = days
        self.data = data
        self.para = para
        self.prepod = prepod
        self.group = group
        self.subject = subject
        self.type_occupation = type_occupation
        self.place_classes = place_classes
        Group_lesson.lessons.append(self)

    def __str__(self):
        return f'День недели: {self.days}; Дата: {self.data}; Пара: {self.para}; Преподаватель: {self.prepod}; Группа: {self.group}; Предмет: {self.subject}; Вид занятия: {self.type_occupation}; Место проведения: {self.place_classes}.'


def prepare(value: str) -> str:
    regexps = [
        r', ?(доц|проф) ?\.',
        r'ст\.пр\.',
        r'\([^)]+\)',
        r'[а-яА-Я]\.[а-я.\-]+н\.'
    ]
    for regexp in regexps:
        value = re.sub(regexp, '', value)
    return value


def day_week(days1):
    data = soup.find('td', day=days1)
    n = soup.find_all('td', day=days1)
    for i in n:
        if 'День самостоятельной работы ' not in i and 'Пересдачи ' not in i and (i.text.split()[-1].isdigit() or i.text.split()[-1] == 'УУНиТ' or '116' in i):
            par = i.get("para").split()
            name = i.text.strip()
            prepods = re.findall(r'([А-Я][^ ]+ [А-Я]\.[А-Я]\.)', name)
            prepod = str(prepods).split("'")[1]
            place_classes = i.text.split()[-1]
            line = re.sub('ст.пр.', '', i.text)
            if 'лек.' in line:
                type_occupation = 'Лекция'
                subject = line.split(', лек.')[0]
            elif ' лаб.' in line:
                type_occupation = 'Лабораторная работа'
                subject = line.split(', лаб.')[0]
            elif 'зачет.' in line:
                type_occupation = 'Зачет'
                subject = line.split(', зачет.')[0]
            elif 'экзамен.' in line:
                type_occupation = 'Экзамен'
                subject = line.split(', экзамен.')[0]
            elif 'пр.' in line:
                type_occupation = 'Практика'
                subject = line.split(', пр.')[0]
            else:
                type_occupation = 'Не указано'
                subject = line.split(str(prepod))[0]

            if 'ЭИОС НФ УУНиТ' in i.text:
                n1 = Group_lesson(days1, data.get("data"), par[0], prepods, i.get("id"), subject, type_occupation,
                                  'ЭИОС НФ УУНиТ')
            elif 'Спортивный зал № 116' in i.text:
                n1 = Group_lesson(days1, data.get("data"), par[0], prepods, i.get("id"), subject, type_occupation,
                                  'Спортивный зал № 116')
            else:
                n1 = Group_lesson(days1, data.get("data"), par[0], prepods, i.get("id"), subject, type_occupation,
                                  place_classes)


def get_lesson_group(group1):
    for i in Group_lesson.lessons:
        if group1 == str(i.group):
            print(i)


def get_lesson_prepod(prepod):
    for i in Group_lesson.lessons:
        if prepod in i.prepod:
            print(i)


def get_all_lessons():
    for i in Group_lesson.lessons:
        print(i)
