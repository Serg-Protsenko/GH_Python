'''
3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), 
яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
'''

def season(month):
    if month in (12, 1, 2):
        return 'зима'
    elif month in (3, 4, 5):
        return 'весна'
    elif month in (6, 7, 8):
        return 'лiто'
    elif month in (9, 10, 11):
        return 'осiнь'

for i in range(1,13):
    print(f'Місяць {i} пора року {season(i)}')