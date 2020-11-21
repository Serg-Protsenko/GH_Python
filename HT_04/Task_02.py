'''
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :) 
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
'''

def validate(username, password):
    special_symbol =['$', '@', '#', '%', '!', '_', '&', '?']
    if len(username) < 3 :
        raise Exception('Username is too short!')
    elif len(username) > 50:
        raise Exception('Username is too long!')
    elif len(password) < 8:
        raise Exception('Password is too short!')
    elif not any(i.isnumeric() for i in password):
        raise Exception('Password should have at least one digit!')
    elif not any(i.isalpha() for i in password):
        raise Exception('Password should have at least one letter!')
    elif not any(i.isupper() for i in password):
        raise Exception('Password should have at least one uppercase letter!')
    elif not any(i in special_symbol for i in password):
        raise Exception("Password should have at least one of the symbols '$', '@', '#', '%', '!', '_', '&', '?")
    
    return True
    
    
username = input("Enter username: ")
password = input('Enter password: ')
try:
    valid =  validate(username, password)
    print(f'Your login is {valid}')
   
except Exception as e:
    print(e)