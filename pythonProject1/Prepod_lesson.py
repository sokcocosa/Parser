import re
from bs4 import BeautifulSoup

with open('Raspisanie.html') as file:
    source = file.read()
soup = BeautifulSoup(source, 'html.parser')


class Prepod_lesson(object):
    lessons = []

    def __init__(self, days, data, para, start, end, prepod, group, sabject, type_occupation, place_classes):
        self.days = days
        self.data = data
        self.para = para
        self.start = start
        self.end = end
        self.prepod = prepod
        self.group = group
        self.sabject = sabject
        self.type_occupation = type_occupation
        self.place_classes = place_classes


'''        Prepod_lesson.lessons.append(self)'''

"""    def __str__(self):
        return f'{self.days} {self.data} {self.para} {self.start} {self.end} {self.group} {self.sabject} {self.type_occupation} {self.place_classes}'
"""


def day_week_prepod(days1, prepod):
    data = soup.find('td', day=days1)
    n = soup.find_all(day=days1, text=re.compile(prepod))
    for i in n:
        par = i.get("para").split()
        par1 = par[-1].split('-')
        group = i.get("id")
        if 'лек.' in i.text:
            type_occupation = 'Лекция'
            subject = i.text.split(', лек.')[0]
        elif ' лаб.' in i.text:
            type_occupation = 'Лабораторная работа'
            subject = i.text.split(', лаб.')[0]
        elif 'зачет.' in i.text:
            type_occupation = 'Зачет'
            subject = i.text.split(', зачет.')[0]
        elif 'экзамен.' in i.text:
            type_occupation = 'Экзамен'
            subject = i.text.split(', экзамен.')[0]
        elif 'пр.' in i.text:
            type_occupation = 'Практика'
            subject = i.text.split(', пр.')[0]
        elif ',' not in i.text:
            type_occupation = 'Не указано'
            subject = i.text.split(prepod)[0]
        else:
            type_occupation = i.text.split(',')[1]
            subject = i.text.split(',')[0]
        if 'ЭИОС НФ УУНиТ' in i.text:
            Prepod_lesson.lessons.append({
                'day': days1,
                'date': data.get("data"),
                'para': par[0],
                'start': par1[0],
                'end': par1[1],
                'prepod': prepod,
                'group': group,
                'subject': subject,
                'type_occupation': type_occupation,
                'place_classes': 'ЭИОС НФ УУНиТ'
            })

        else:
            Prepod_lesson.lessons.append({
                'day': days1,
                'date': data.get("data"),
                'para': par[0],
                'start': par1[0],
                'end': par1[1],
                'prepod': prepod,
                'group': group,
                'subject': subject,
                'type_occupation': type_occupation,
                'place_classes': i.text.split()[-1]
            })


def print_lessons():
    for i in Prepod_lesson.lessons:
        print(i)
