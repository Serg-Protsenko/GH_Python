'''
1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
   - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
   - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
   - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )
'''
 
class Calc(object):
    '''Simple class calculator'''
    last_result = None
 
    def add(self, first_num, second_num):
        '''Addition two numbers'''
        self.last_result = first_num + second_num
        return self.last_result
 
    def subtract(self, first_num, second_num):
        '''Substraction two numbers'''
        self.last_result = first_num - second_num
        return self.last_result
 
    def multiply(self, first_num, second_num):
        '''Multiplication two numbers'''
        self.last_result = first_num * second_num
        return self.last_result
 
    def division(self, first_num, second_num):
        '''Division two numbers and check division by zero'''
        if second_num == 0:
            print('Division by zero!')
        else:
            self.last_result = first_num / second_num
            return self.last_result
 
A = Calc()
print(A.last_result)
A.add(1, 1)
print(A.last_result)
A.subtract(9, 4)
print(A.last_result)
A.multiply(3, 7)
print(A.last_result)
A.division(9, 3)
print(A.last_result)
A.division(9, 0)
print(A.last_result)