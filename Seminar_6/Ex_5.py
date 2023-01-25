# Создайте список из случайных чисел. Найдите количество различных элементов в нем.

from random import randint

some_list = [randint(1,10) for i in range(10)]
print(some_list)
count = 0
unique_array = []

for i in some_list:
    if i not in unique_array:
        count += 1
        unique_array.append(i)
print(f'количество различных элементов:',len(unique_array))

