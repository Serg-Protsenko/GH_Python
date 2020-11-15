'''
5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа 
Фібоначчі, що не перевищують його.
'''
def Fibonacci(number):
    fibo_list = []
    a, b = 0, 1
    while b <= number:
        fibo_list.append(b)
        a, b = b, a + b
    return fibo_list
number = int(input('Enter number: '))
print(Fibonacci(number))