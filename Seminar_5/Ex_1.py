#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('enter some text: ').split()
final_text = list(filter(lambda word: 'а' not in word and 'б'not in word and 'в' not in word, text))
print(*final_text)