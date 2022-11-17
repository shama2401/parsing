#Из Dictionary №1:
#Добавьте в меню 
#напитки как ключ "drinks", 
#А список всех доступных напитков: ['Coca-Cola', 'Sprite', 'Fanta'] как его значение.
'''
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta'] 
print(menu)
'''
#PROBLEM 2:
#Создайте пустой словарь.
#Запустите цикл который 3 раза спросит его имя и его пароль.
#Записывайте имя пользователя как ключ, а пароль как его значение.
'''
a={}
c=0
while c<3:
    login=input('Введите имя:') 
    password=input('Введите пароль:')
    a[login]=password
    c+=1
    print(a)
    a.update()
'''

#PROBLEM 3:
#Создайте Dictionary с 5 элементами где ключи это их имена, а значение их профессия.
#С помощь цикла for пройти вывести на экран строку:
'''
"Здравствуйте <Имя>  Прекрасная профессия <Профессия>"
a={'maks': 'pevec',
   'luis':'pilot',
   'dima':'povar',
   'victor':'bankir',
   'beka':'it'}
for k,v in a.items():
     print(f'Здравствуйте {k}  Прекрасная профессия {v}')
'''
#PROBLEM 4:
#Из Dictionary №1:
#Добавьте в меню 
#'besh_barmak' который стоит  130 сом.
#Оказалось лагман слишком дешевый. Обновите цену на 135
#Ваш повар отвратительно готовит борщ, поэтому хотите удалить это блюдо.
#Удалить borsh
'''
menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
menu['besh_barmak']='130'
menu.update({'lagman':135})
menu.pop('borsh')
print(menu)
'''

#PROBLEM 5:
#Есть список Южноамериканских стран
#в котором Суринам встречается два раза. Необходимо написать программу,
#которая удалит дублирующуюся запись, и возвратит в результате словарь {'номер': 'страна'}.
'''
south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
a=set(south_american_countries)
num={}
for i in range(len(a)):
    num[i]=south_american_countries[i]
print(num)
'''
