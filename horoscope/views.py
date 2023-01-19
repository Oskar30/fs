from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

zodiac_name_list = list(zodiac_dict)

def sign_info_number(request, sign_number: int):
    if sign_number > len(zodiac_dict):
        return HttpResponseNotFound(f'unknown zodiac sign number - {sign_number}')

    zodiac_name = zodiac_name_list[sign_number-1]
    redirect_url = reverse('horoscope-name', args=(zodiac_name,))
    return HttpResponseRedirect(redirect_url)
    

def sign_info(request, sign: str):
    description = zodiac_dict.get(sign)
    print(len(zodiac_dict))
    if description:
        return HttpResponse(f'<h2>{description}</h2>')    
    else:
        return HttpResponseNotFound(f'unknown zodiac sign - {sign}')

def index(request):
    cont = []
    for sign in zodiac_name_list:
        cont.append(f'<h2><li>{sign}</li></h2>')

    return HttpResponse(cont) 