'''
#1 Из множества 
#№ 1 - удалите все числа 6.
dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
dates_of_birth.remove(6)
print(dates_of_birth)
'''
'''
#2 Создайте SET состоящий из 3 вложенных SET.
d = set()
a =frozenset({'banana'})
b =frozenset({'kokos'})
c =frozenset({'apple'})
d.update(a,b,c)
print(d)
'''
'''
#3 Во множестве №3 найдите объекты которых нет во множестве №2
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_3 = farm_2.difference(farm_1)
print(farm_3)
'''
'''
#4 Создайте SET из 5 элементов. Потом добавьте в SET ещё один элемент.
#А затем удалите через .pop() элемент и посмотрите что же вы удалили.
a = {'man', 'woman', 'rafa', 'samsy', 'kans'}
a.add('gik')
print(a)
a.pop()
print(a)
'''
'''
#5 Создайте цикл который справшивает у пользователя 10 чисел и добавьте их в SET.

#Сделайте так чтобы эти данные уже никто не смог поменять позже.
nums = set()
for i in range(10):
	num = int(input('Введите число:  '))
	nums.add(num)
	t = tuple(nums)
print(t)
'''
#6 Из Множество 2 и 3 
# Напишите код, который: Выведет новое множество, которое есть как в
# первой ферме, так и во второй.
# Выведет новое МНОЖЕСТВО, состоящее из животных,
# которые есть в первой ферме, но нет во второй.

farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_3 = farm_1.intersection(farm_2)
farm_4 = farm_1.difference(farm_2)
print(farm_3)
print(farm_4)
