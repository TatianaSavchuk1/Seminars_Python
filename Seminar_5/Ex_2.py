# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def rle_encode(string):
    encoding = ''
    count = 1
    i = 0
    string = string + '0'

    while i+1 < len(string):

        if string[i] == string[i + 1]:
            count += 1
            i += 1
        
        elif string[i] != string[i + 1]:    
            encoding += str(count) + string[i]
            count = 1
            i += 1
    return encoding

string = input('enter the symbols: ')
print(rle_encode(string))
    


