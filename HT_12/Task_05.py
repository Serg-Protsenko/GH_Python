'''
5. Створити пустий клас, який називається Thing. Потім створіть об'єкт example 
цього класу. Виведіть типи зазначених об'єктів.
'''

class Thing(object):
    pass
 
example = Thing()
print(f'Type of class: {type(Thing())}')
print(f'Type of object: {type(example)}')