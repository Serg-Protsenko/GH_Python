'''
2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів, які зберігатиме в відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
   - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.
'''
 
class Person(object):
    ''' class Person which describes person'''
 
    def __init__(self, *args):
        '''Parameters name and age'''
        self.name = args[0]
        self.age = args[1]
 
 
    def show_age(self):
        '''This method print age of person'''
        print(self.age)
 
 
    def print_name(self):
        '''This method print name of person'''
        print(self.name)
 
 
    def show_all_information(self):
        '''This method print all information about person'''
        print(f'All information about person is ')
        for k,v in self.__dict__.items():
            print(f'{k}: {v}')
        print()


Vasya = Person('Vasya', 21)
Olya = Person('Olya', 15)
 
Vasya.print_name()
Vasya.show_age()
 
Olya.print_name()
Olya.show_age()
 
Vasya.profession = 'Student'
Olya.profession = 'Schoolgirl'
 
Vasya.show_all_information()
Olya.show_all_information()