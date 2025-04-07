from lib2to3.fixes.fix_input import context

from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    context = {
        'vk': 'https://vk.com/tatarintsk'
    }
    return render(request, 'main/contacts.html', context)

