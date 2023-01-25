# Пора учить английский язык", - сказал себе Степа и решил написать программу для изучения английского языка. 
# Программа получает на вход слово на английском языке и несколько его переводов на русском языке. Составьте словарь, 
# в котором ключ - это английское слово, а значение - это список русских слов. 
# В этой задаче нужно использовать строчный метод split().

number = int(input('number of words: '))
dictionary = {}

for i in range(number):
    word = input('enter the word: ')
    translations = input('enter the list of translations: ').split()
    dictionary[word] = translations
    
print(dictionary)
