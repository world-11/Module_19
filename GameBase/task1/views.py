# Create your views here.
def cart(request):
    title = 'Корзина'
    text8 = 'Извините, ваша корзина пуста'
    text9 = 'Вернулься обратно'
    adr1 = '/platform'
    context = {
        'title': title,
        'text8': text8,
        'text9': text9,
        'adr1': adr1
    }
    return render(request, 'cart.html', context)

"""
def games(request):
    title = 'Магазин игр'
    text0 = 'Игры:'
    text1 = ['PUBG: BUTTLEGROUND', 'Cyberpunk 2077', 'Red Dead Redeption 2']
    text4 = 'Купить'
    text5 = 'Вернуться обратно'
    adr1 = '/platform'
    context = {
        'title': title,
        'text0': text0,
        'text1': text1,
        'text4': text4,
        'text5': text5,
        'adr1': adr1
    }
    return render(request, 'games.html', context)
"""

def games(request):
    games = Game.objects.all().values()
    text = 'Купить'
    context = {
        'games': games,
        'text': text,
    }
    return render(request, 'games.html', context)


def platform(request):
    title = 'Видеоигры'
    text0 = 'Обзор популярных видеоигр'
    text1 = 'На главную'
    text2 = 'Магазин'
    text3 = 'Корзина'
    adr1 = '/platform'
    adr2 = '/platform/games/'
    adr3 = '/platform/cart/'
    context = {
        'title': title,
        'text0': text0,
        'text1': text1,
        'text2': text2,
        'text3': text3,
        'adr1': adr1,
        'adr2': adr2,
        'adr3': adr3
    }
    return render(request, 'platform.html', context)



from django.shortcuts import render
from .forms import UserRegister
from .models import *

# Create your views here.


def sign_up_by_html(request):
    users = Buyer.objects.all().values()
    name_users = []
    for i in range(len(users)):
        name_users.append(users[i]['name'])

    print(users)
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_ = request.POST.get('password_')
        age = request.POST.get('age')

        if password != password_:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'registration_page.html', info)
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
            return render(request, 'registration_page.html', info)
        if username in name_users:
            info['error'] = f'Пользователь {username} уже существует!'
            return render(request, 'registration_page.html', info)
        info['welcome'] = f'Приветствуем, {username}'
        Buyer.objects.create(name=username, balance=0, age=age)

    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    users = Buyer.objects.all().values()
    name_users = []
    for i in range(len(users)):
        name_users.append(users[i]['name'])
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_ = form.cleaned_data['password_']
            age = form.cleaned_data['age']
        if password != password_:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'registration_page.html', info)
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
            return render(request, 'registration_page.html', info)
        if username in name_users:
            info['error'] = f'Пользователь {username} уже существует!'
            return render(request, 'registration_page.html', info)
        info['welcome'] = f'Приветствуем, {username}'
        info['form'] = form
        Buyer.objects.create(name=username, balance=0, age=age)

    return render(request, 'registration_page.html', info)
