from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import date
from horoscope import Class_Zodiac


zodiac_dict = {
    'aries': 
        {'element':'fire',
        'description':'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).'},
    'taurus':
        {'element':'earth',
        'description':'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).'},
    'gemini':
        {'element':'air',
        'description':'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).'},
    'cancer':
        {'element':'water',
        'description':'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).'},        
    'leo':
        {'element':'fire',
        'description':'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).'},
    'virgo':
        {'element':'earth',
        'description':'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).'},
    'libra':
        {'element':'air',
        'description':'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).'},
    'scorpio':
        {'element':'water',
        'description':'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).'},
    'sagittarius':
        {'element':'fire',
        'description':'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).'},
    'capricorn':
        {'element':'earth',
        'description':'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).'},
    'aquarius':
        {'element':'air',
        'description':'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).'},
    'pisces':
        {'element':'water',
        'description':'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'}
}

zodiac_name_list = list(zodiac_dict)


def sign_info_number(request, sign_number: int):
    if sign_number > len(zodiac_dict):
        return HttpResponseNotFound(f'unknown zodiac sign number - {sign_number}')

    zodiac_name = zodiac_name_list[sign_number-1]
    redirect_url = reverse('horoscope-name', args=(zodiac_name,))
    return HttpResponseRedirect(redirect_url)
    

def sign_info(request, sign: str):
    zodiac = zodiac_dict.get(sign)
    description = zodiac['description']
    if zodiac:
        return HttpResponse(f'<h2>{description}</h2>')
    else:
        return HttpResponseNotFound(f'unknown zodiac sign - {sign}')


def index(request):
    content = []
    for sign in zodiac_name_list:
        content.append(f'<h2><li><a href="{sign}">{sign}</a></li></h2>')

    return HttpResponse(content)


def type(request):
    content = []
    for sign in zodiac_dict:        
        element = zodiac_dict[sign]['element']

        if f'<h2><li><a href="{element}">{element}</a></li></h2>' not in content:
            content.append(f'<h2><li><a href="{element}">{element}</a></li></h2>')
        
    return HttpResponse(content)


def elemental(request, element: str):
    bufer_list, content = [], []

    if element == 'fire':
        for el in zodiac_dict:
            if zodiac_dict[el]['element'] == element:
                bufer_list.append(el)
    
    elif element == 'earth':
        for el in zodiac_dict:
            if zodiac_dict[el]['element'] == element:
                bufer_list.append(el)

    elif element == 'air':
        for el in zodiac_dict:
            if zodiac_dict[el]['element'] == element:
                bufer_list.append(el)

    elif element == 'water':
        for el in zodiac_dict:
            if zodiac_dict[el]['element'] == element:
                bufer_list.append(el)

    else:
        return HttpResponse(f'<h2>not elemental {element}</h2>')        
    
    for sign in bufer_list:        
        content.append(f'<h2><li><a href="//127.0.0.1:8000/horoscope/{sign}/">{sign}</a></li></h2>')

    return HttpResponse(content)


def get_info_by_date(request, month, day):
    input_date = date(2023, month, day)
    
    if input_date >= Class_Zodiac.Aries.date and input_date < Class_Zodiac.Taurus.date:

        zodiac_name = Class_Zodiac.zodiac_list[0]
        redirect_url = reverse('horoscope-name', args=(zodiac_name,))
        return HttpResponseRedirect(redirect_url)  

    else:
        return HttpResponse('NO')
