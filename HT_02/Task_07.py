'''
7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
'''

def simple_calculator(first_num, second_num, operation):
    if operation == '+':                                        
        return print(f'Result of addition is {first_num + second_num}.')    
    elif operation == '-':
        return print(f'Result of substraction is {first_num - second_num}.') 
    elif operation == '/':
        return print(f'Result of division is {first_num / second_num}.') 
    elif operation == '*':
        return print(f'Result of multiplication is {first_num * second_num}.')
    else:
        return print('Please, enter right sign: +, -, /, *.')    

first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
operation = input('Enter operation (+, -, /, *): ')
simple_calculator(first_num, second_num, operation)