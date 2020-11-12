'''
4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати 
якийсь результат. Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, 
обробляє повернутий ними результат та також повертає результат. Таким чином ми будемо 
викликати 1 функцiю, а вона в своєму тiлi ще 3
'''

def your_language(language):
    if language.lower() == 'python':
        return language.upper() + ' :) !!!'
    else:
        return language.lower() + ' :( !'

def your_name(name):
    return name.capitalize()

def your_surname(surname):
    return surname.upper()

def greeting():
    language = your_language(input('Enter your programming language: '))
    name = your_name(input('Enter your name '))
    surname = your_surname(input('Enter your surname '))
    return f'Hello {name} {surname} your favorite programming language is {language}'

print(greeting())