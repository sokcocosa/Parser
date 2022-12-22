import Group_lesson

from bs4 import BeautifulSoup

with open('Raspisanie.html') as file:
    source = file.read()
soup = BeautifulSoup(source, 'html.parser')

Group_lesson.day_week('Понедельник')
Group_lesson.day_week('Вторник')
Group_lesson.day_week('Среда')
Group_lesson.day_week('Четверг')
Group_lesson.day_week('Пятница')
Group_lesson.day_week('Суббота')
if 'Воскресенье' in soup.text:
    Group_lesson.day_week('Воскресенье')

variable = int(input('Вы хотите узнать расписание группы, преподователя или всё расписание?(1, 2 или 3): '))
if variable == 1:
    group1 = input('Введите навзание группы (вида ИС-31к): ') + '_'
    Group_lesson.get_lesson_group(group1)
elif variable == 2:
    prepod = input('Введите фамилию и инициалы преподавателя (вида Мугаллимова Л.И.): ')
    Group_lesson.get_lesson_prepod(prepod)
elif variable == 3:
    Group_lesson.get_all_lessons()
