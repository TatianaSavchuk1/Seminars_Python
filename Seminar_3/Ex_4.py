# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a = int(input('введите число: '))
binary_list = []
while a > 1:
    binary_list.append(a % 2)
    a = a // 2
binary_list.append(1)
binary_list.reverse()
print(f'Ваше число в двоичной системе: ', *binary_list)