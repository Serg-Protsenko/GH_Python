'''
1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - 
   необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, 
       інакше (<silent> == <False>) - породжується виключення LoginException
'''
class LoginException(Exception):
    pass

def login(username, password, silent=False):
    login_list = [{'Vasya':'12345678'}, {'Petya':'123123'}, {'Jackson':'qwerty12'}, {'Simon':'123abs'}, {'Olya':'_tyta1234'}]
    if silent:
        if any(i.get(username) == password for i in login_list):
            return True
        else:
            return False
    else:
        raise LoginException('Something wrong with You access!!!')

username = input('Enter username: ')
password = input('Enter password: ')
silent = input('Enter silent: ')

print(f'Your login/password: {login(username, password, silent)}')