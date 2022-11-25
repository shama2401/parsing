
#1Напишите код где есть TypeError,IndexError,NameError
'''
a=1
b='1'm
try:
    a/b
except TypeError as zde:  
    print('no')

c=[1,2,3,4]
try:
    print(c[4])
except IndexError as zde:
    print('not')

try:
    print(d)
except NameError as zde:
    print('good')
'''
#2Возьмите код #1 и создайте для него try... except... Создайте несколько except выражений для разных типов ошибок.
'''
at = 10

i = 15

wo = 20

try:
    for e in range(-at, at):
        print(wo / e)
        if at > '5':
            print(at > 5)
except ValueError:
    print("Преобразование прошло неудачно")
except ZeroDivisionError:
    print("Попытка деления числа на ноль")
except BaseException:
    print("Общее исключение")
print("Завершение программы")
'''
'''
#3Перенесите к себе код #2 и исправьте все ошибки, сделайте так чтобы работал. Если не знаете как исправить ошибку создайте для неё except выражение.

#Code #2:
try:
    lst = []
    for i in range(10):
        lst.append(i)
    a = list(reversed(lst))
    sls_obj = slice(0,8)
    print(a[sls_obj])
except AttributeError as f:
    print(f)
except NameError as n:
    print(n)
except TypeError as vu:
    print(vu)
'''

#4Перенесите к себе код #3 и исправьте все ошибки, сделайте так чтобы код работал.
# Если не знаете как исправить ошибку создайте для неё except выражение.


'''
a = 0
b = 1
numbers = []
while b > a:
    numbers.append(b)
    b += 1
    print(numbers)
    break
'''