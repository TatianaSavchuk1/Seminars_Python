import datetime

def log_cash (mod):
    with open('data.txt', 'a', encoding = 'utf-8') as file:
        file.write(f'Тип и время записи: {mod}. {datetime.datetime.now()}\n')