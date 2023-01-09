#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


n = int(input("Введите число: "))
a = 2
factor_list = []
N = n
while a <= n:
    if n % a == 0:
        factor_list.append(a)
        n //= a
        a = 2
    else:
        a += 1
print(f"Простые множители числа {N}: {factor_list}")

