# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

num_of_elements = int(input('Введите количество элементов списка: '))
list_1 = []
for elem in range(num_of_elements):
    list_1.append(random.randint(-5, 20))
print(list_1)

list_2 = []
min_ = int(input('Задайте минимум диапазона: '))
max_ = int(input('Задайте максимум для диапазона: '))

for elem in range(len(list_1)):
    if list_1[elem] >= min_ and list_1[elem] <= max_:
        list_2.append(elem)
print(list_2)

