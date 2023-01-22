from datetime import date


class Zodiac:
    def __init__(self, name, element, description, date) -> None:
        self.name = name
        self.element = element
        self.description = description
        self.date = date

    def __str__(self) -> str:
        return self.name
        

Aries = Zodiac(
    'aries',
    'fire', 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)',
    date(2023, 3, 21))

Taurus = Zodiac(
    'taurus',
    'earth', 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)',
    date(2023, 4, 21))

Gemini = Zodiac(
    'gemini',
    'air', 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)',
    date(2023, 5, 22))

Cancer = Zodiac(
    'cancer',
    'water', 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)',
    date(2023, 6, 22))

Leo = Zodiac(
    'leo',
    'fire', 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)',
    date(2023, 7, 23))

Virgo = Zodiac(
    'virgo',
    'earth', 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)',
    date(2023, 8, 22))

Libra = Zodiac(
    'libra',
    'air', 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)',
    date(2023, 9, 24))

Scorpio = Zodiac(
    'scorpio',
    'water', 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)',
    date(2023, 10, 24))

Sagittarius = Zodiac(
    'sagittarius',
    'fire', 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)',
    date(2023, 11, 23))

Capricorn = Zodiac(
    'capricorn',
    'earth', 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января)',
    date(2023, 12, 23))   

Aquarius = Zodiac(
    'aquarius',
    'air', 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)',
    date(2023, 1, 21))

Pisces = Zodiac(
    'pisces',
    'water', 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)',
    date(2023, 2, 20))

zodiac_list =   [Aries, Taurus, Gemini, Cancer, Leo, Virgo,
                Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces]