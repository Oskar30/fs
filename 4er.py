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

fire_list, earth_list, air_list, water_list = [], [], [], []

print(fire_list, earth_list, air_list, water_list)






'''
https://www.youtube.com/watch?v=scugUPvlylM&list=PLQAt0m1f9OHvGM7Y7jAQP8TKbBd3up4K2&index=22
https://www.homeenglish.ru/OtherGoroscop.htm
'''


'''
git clone (paste url from git)
git pull (download in local pc)
git status
git add name.file |or| add -A (all files)
git commit -m "write comment" (if problem ~~~ no comment: esc -> :wq)
git push

git (help)
git checkout master



DJ-60
# 1
1) python -m venv my_project - create Virtual ENVironment
2) in the root create requirements.txt writing need librarys to the file
3) activate venv:
	venv\Scripts\activate (activate.bat) - Windows;	
	source venv/bin/activate - Linux, MacOS.

	IF NOT START, perhaps because of the script execution policy. (https://learn.microsoft.com/ru-ru/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3)
	PowerShell under admin:
		Set-ExecutionPolicy RemoteSigned 		

	deactivate (deactivate.bat)
4) pip install -r requirements.txt
5) pip freeze
6) django-admin startproject shop .
7) python manage.py startapp main (app_name)
8) in settings.py add app_name in INSTALLED_APPS #33 string
9) python manage.py makemigrations #create db
10) python manage.py migrate #apply migrats
11) python manage.py runserver
12) 	# models.py - object in db
	# views.py - handler/worker page
	# urls.py - registr urls in site
	# 
13) python manage.py createsuperuser # from admin panel
14) python manage.py shell # comand str 
15) add in db new object:
	from main.models import Product
	>>> product = Product(name = 'Redmi Note 11', description = 'Бюджетный смартфон', price = 15000)
	>>> product.save()
			OR ONE MORE METHOD ORM:
	>>> Product.objects.create(name = 'OnePlus 8', description = 'more android', price =20000)
Product.objects.all() # show all product
exit()
16) 
'''