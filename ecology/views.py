from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import *
from .work import *

regular_menu = ['Главная страница', 'Охрана окружающей среды', 'Эксплуатация', 'Охрана труда', 'Пожарная безопасность']
section_menu = [
    {'title': "Движение отходов", 'url_name': 'accounting'},
    {'title': "Просмотр и редактирование", 'url_name': 'review'},
    {'title': "Отчеты", 'url_name': 'reports'},
]


def home(request):
    waste = Waste_types.actual.all()
    waste_stok = Waste_types.objects.filter(code='1471501')
    data = get_stok('Е.А.Богомья')
    actual_collection = Waste_collection.actual.filter()

    context = {
        'title': 'Экология',
        'menu1': regular_menu,
        'menu2': section_menu,
        'waste': waste,
        'wa': waste_stok,
        'data': data,
        'collection': actual_collection,
    }
    return render(request, 'ecology/home.html', context=context)


def accounting(request):
    context = {
        'title': 'Движение отходов',
        'menu1': regular_menu,
        'menu2': section_menu,
    }
    return render(request, 'ecology/accounting.html', context=context)


def review(request):
    return HttpResponse('<h1>Просмотр и редактирование</h1>')


def reports(request):
    return HttpResponse('<h1>Отчеты</h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена!</h1>")
