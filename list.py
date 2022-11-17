#1Создать Лист и заполнить его 5 РАЗНЫМИ ТИПАМИ ДАННЫХ.
'''
list = [3, True, 'Витя', 2.0,10000,{6:7}] 
'''

#2Взять Лист №1 и посчитать сколько раз там встречается имя "Jack"
'''
names = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON', 'JHON',  'JIMMY', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON',]
for i in names:
    print(i)
print(names.count('JACK'))
'''

#3Удалить из Листа №1 все чётные индексы до 10.
'''
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
i = 0
while i <10:
    if i % 2==0:
        names.pop(i)
    if i % 2==1:
        names.pop(i)
    i+=1
print (names)
'''
#4Создать пустой лист.
#Добавить в него сначала Ваше Имя, Год Рождения, любимый Язык Программирования
'''
a=[]
a.append('jack')
a.append('1991')
a.append('python')
print(a)
'''
#5.Создать Лист из 5 разных имён.
#.Создать пустую строку и через .join() соеденить пустую строку и все имена в списке.
'''
names = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON']
list=''.join(names)
print(list)
'''
