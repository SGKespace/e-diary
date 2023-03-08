import random
from django.db import models
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation


def name_check():
    try:
        child = input("Введите ученика (формат: Фролов Иван [Отчество]): ")
        child_name = Schoolkid.objects.get(full_name__contains=child)
        return child_name
    except Schoolkid.DoesNotExist:
        raise Schoolkid.DoesNotExist("Ученик не найден, проверьте ввод")
    except Schoolkid.MultipleObjectsReturned:
        raise Schoolkid.MultipleObjectsReturned('Найдено несколько учеников, добавьте отчество')


def fix_marks():
    list_of_bad_mark = Mark.objects.filter(points__in=[2, 3], schoolkid_id=name_check())
    for current_bad_mark in list_of_bad_mark:
        current_bad_mark.points = 5
        current_bad_mark.save()
    print('Шалость удалась!')


def del_Chastisement():
    list_of_bad_chastisement = Chastisement.objects.filter(schoolkid_id=name_check())
    for current_bad_chastisement in list_of_bad_chastisement:
        current_bad_chastisement.delete()
    print('Шалость удалась!')


def create_commendation():
    comments = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!', 'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!', 'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!', 'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!', 'Здорово!', 'Это как раз то, что нужно!', 'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!', 'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!', 'Ты многое сделал, я это вижу!', 'Теперь у тебя точно все получится!']
    schoolkid = name_check()
    target_lesson = input("Введите предмет: ")
    hack_lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject__title=target_lesson).order_by('?').first()
    Commendation.objects.create(text=random.choice(comments), created=hack_lesson.date, schoolkid=schoolkid, subject=hack_lesson.subject, teacher=hack_lesson.teacher)
    print('Шалость удалась!')


