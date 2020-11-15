'''
1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і 
вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.
'''

def square(a):
    return a*4 , a*a, round(a * 2**0.5, 2)

a = float(input('Enter a length of the side of the square: '))
print(f'The perimeter, the area and the diagonal of the square with side {a} are {square(a)}.')