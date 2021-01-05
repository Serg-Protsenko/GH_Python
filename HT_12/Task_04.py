'''
4. Створіть клас в якому буде атребут який буде рахувати кількість створених 
екземплярів класів.
'''

class Start(object):
    counter = 0
    def __init__(self):
        Start.counter += 1
 
go_one = Start()
go_two = Start()
 
print(f'Creaded - {Start.counter} objects.')