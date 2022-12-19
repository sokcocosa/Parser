import Prepod_lesson
import Group_lesson
from bs4 import BeautifulSoup

with open('Raspisanie.html') as file:
    source = file.read()
soup = BeautifulSoup(source, 'html.parser')

variable = int(input('Вы хотите узнать расписание группы или преподователя?(1 или 2): '))
if variable == 1:
    group = input('Введите навзание группы (вида ИС-31к): ') + '_'
    Group_lesson.day_week_group('Понедельник', group)
    Group_lesson.day_week_group('Вторник', group)
    Group_lesson.day_week_group('Среда', group)
    Group_lesson.day_week_group('Четверг', group)
    Group_lesson.day_week_group('Пятница', group)
    Group_lesson.day_week_group('Суббота', group)
    if 'Воскресенье' in soup.text:
        Group_lesson.day_week_group('Воскресенье', group)
    Group_lesson.print_lessons()
elif variable == 2:
    prepod = input('Введите фамилию и 2 инициала преподавателя(Иванов И.И.): ')
    Prepod_lesson.day_week_prepod('Понедельник', prepod)
    Prepod_lesson.day_week_prepod('Вторник', prepod)
    Prepod_lesson.day_week_prepod('Среда', prepod)
    Prepod_lesson.day_week_prepod('Четверг', prepod)
    Prepod_lesson.day_week_prepod('Пятница', prepod)
    Prepod_lesson.day_week_prepod('Суббота', prepod)
    if 'Воскресенье' in soup.text:
        Prepod_lesson.day_week_prepod('Воскресенье', prepod)
    Prepod_lesson.print_lessons()
