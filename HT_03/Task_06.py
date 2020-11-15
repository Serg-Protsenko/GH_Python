'''
6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити 
його на 100, якщо дорівнює 0, не змінювати.
'''

def check_number(number):
    if number == 0:
        return int(number)
    elif number > 0:
        return number * number
    else:
        return number + 100

print(check_number(float(input('Enter a number: '))))