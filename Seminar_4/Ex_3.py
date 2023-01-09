#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
some_list = []
new_list = []

for i in range(0, 10):
    some_list.append(randint(1, 10))
print(some_list)

for i in some_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)





