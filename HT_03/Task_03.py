'''
3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, 
и яка вертатиме True, якщо це число просте, и False - якщо ні.
'''

def is_prime(number):
    if number == 1:
            return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

for i  in range(1, 11):
    print(f'{i} is prime: {is_prime(i)}.')