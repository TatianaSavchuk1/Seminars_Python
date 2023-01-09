# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = input('введите точность d: ')
accuracy = len(d) - 2
print(accuracy)
import math
pi = round(math.pi, int(accuracy))
print(pi)

