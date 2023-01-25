# Пользователь вводит число K - количество фруктов. Затем он вводит K фруктов в формате: название фрукта и его количество. 
# Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение.

number = int(input('enter the number of fruits: '))
fruit_dictionary = {}

for i in range(number):
    fruit = input('enter the fruit: ')
    fruits_amount = input('enter amount of fruits: ')
    fruit_dictionary[fruit] = fruits_amount
    
print(fruit_dictionary)

