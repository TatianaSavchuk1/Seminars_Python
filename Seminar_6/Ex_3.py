# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Выведите средний возраст всех друзей и самое длинное имя.


n = int(input('enter the number of friends: '))
friends = []
sum = 0
midage = 0
longest_name = float('-inf')


for i in range(n):
    name = input('enter the name: ')
    age = int(input('enter the age: '))
    friends.append(dict(name=name, age=age))
    sum = sum + age

for person in friends:
     if len(person['name']) > longest_name:
        longest_name = len(person['name'])

midage = sum/n

print(friends)
print(f'middle age is ',round(midage))
print(longest_name)


