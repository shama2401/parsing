#1Сгенерируйте список чисел от 1 до 255 при это числа 15. 24. 81. 132. 196 и 214 запрещены

'''

a=[x for x in range(1,255) if  x!=15 and x!=24 and x!=81 and x!=132 and x!=196 and x!=214 ]
print(a)

'''

#2Сгенерируйте список с матрицой внутри с размерностью 6х6
'''
a=[
     [0,0,0,0,0,0],
     [1,1,1,1,1,1],
     [2,2,2,2,2,2],
     [3,3,3,3,3,3],
     [4,4,4,4,4,4],
     [5,5,5,5,5,5],
     [6,6,6,6,6,6],
  ]

b=[j for i in a for j in i]
print(b)
'''

#Спросите пользователя логин и пароль 6 раз и сгенерируйте словарь с логинами в качестве ключа и паролями в качестве значения
'''
z={login:password for password in range(6) for login in [input('Введитк логин:')] for password in [input('Введите пароль:')]}
print(z)
'''

#1 сгенерируйте отсартированный по алфавиту этот список с этими данными

'''
names = ['Kairat', 'Erlan', 'Dastan', 'Artur', 'Bahtoolot', 'Azat', 'Bakyt']
z= sorted([x for x in names])
print(z)
'''