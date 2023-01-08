# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

a = (input('введите числа: ')).split()

for i in range(len(a)):
    a[i] = float(a[i])
    a[i] = round(a[i] - int(a[i]), 2)
if 0.0 in a:
    a.remove(0.0)
    
print(max(a) - min(a))


#a = input('введите вещественные числа: ').split()
# b = []
# c = []

# for i in range(len(a)):
#     if '.' not in a[i]:
#         continue 
#     b.append(a[i].split('.'))
# for i in range(len(b)):
#     b[i][0] = '0'
#     c.append(b[i][0] + '.' + b[i][1])
# for i in range(len(c)):
#     c[i] = float(c[i])

# print(max(c) - min(c))

    