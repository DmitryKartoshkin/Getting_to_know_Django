from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M:%S')
    time = f'Текущее время: {current_time}'
    return render(request, 'app/time.html', context={'time': time})


def workdir_view(request):
    path = '.'
    workdir = sorted(os.listdir(path))
    return render(request, 'app/workdir.html', context={'workdir': workdir})

