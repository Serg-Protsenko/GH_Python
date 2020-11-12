'''
2. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе 
всі високосні роки в цьому проміжку (границі включно).
'''

start_year = int(input('Enter first year: '))
last_year = int(input('Enter last year: '))
for i in range(start_year, last_year + 1):
    if (i%4==0 and i%100!=0) or i%400==0:
        print(i) 