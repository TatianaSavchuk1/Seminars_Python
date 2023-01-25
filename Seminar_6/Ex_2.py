# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Найдите самого младшего из друзей и выведите его имя.
#  Ввод:
# >> 3 Количество друзей
# >> Иван
# >> 11
# >> Саша
# >> 12
# >> Леша
# >> 10
# Вывод:
# >> Леша

n = int(input('enter the number of friends: '))
friends = []

for i in range(n):
    name = input('enter the name: ')
    age = input('enter the age: ')
    friends.append(dict(name=name, age=age)) 

print(friends)

youngest = min(friends, key=lambda x: x['age'])
print(youngest['name'])