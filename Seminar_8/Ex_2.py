# print (ord('э'), ord('ю'), ord('я'))
# print (chr(1094))
# print (ord('я') - 31)
# print(chr(1072))
# print(ord('А'), ord('Я'))

# Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром
# Цезаря и возвращает его. Шифр Цезаря заменяет каждую букву в тексте на букву, которая
# отстоит в алфавите на некоторое фиксированное число позиций.
# В функцию передается сообщение и сдвиг алфавита. Если сдвиг не указан, то пусть ваша
# функция кодирует сдвиг алфавита на 3 позиции:
# А→Г,А→Г,
# Б→Д,Б→Д,
# В→Е,В→Е,
# ……
# Э→А,Э→А,
# Ю→Б,Ю→Б,
# Я→ВЯ→В
# Все символы, кроме русских букв должны остаться неизменными. Маленькие буквы должны
# превращаться в маленькие, большие — в большие.
# Напишите также функцию декодирования decrypt_caesar(msg, shift), также
# использующую сдвиг по умолчанию. При написании функции декодирования используйте
# вашу функцию кодирования.

def encrypt_caesar(letter, shift): 
    if letter.isalpha():
        number = ord(letter) + shift
        if number > 1103:
            number -= 32
        return chr(number)
    return letter

def decrypt_caesar(letter, shift):
    if letter.isalpha():
        number = ord(letter) - shift
        if number < 1040:
            number += 32
        return chr(number)
    return letter
 

msg = "Да здравствует салат Цезарь!"
msg1 = 'Зг кзугефхецих фгогх Щикгуя!'
shift = 3

for letter in msg:
    print(encrypt_caesar(letter, shift), end='')

print('')

for letter in msg1:
    print(decrypt_caesar(letter, shift), end='')

