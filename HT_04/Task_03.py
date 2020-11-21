'''
3. На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
'''

login_list = [{'Vasya':'12345678'}, {'Welcome':'!A_as123123'}, {'Jackson':'qwerty_12'}, {'Simon':'123abs'}, {'Olya_Krasa':'_Tyta1234'}, {'Li':'1312322ddd'}]

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

for dic in login_list:
    for key in dic:
        print(f'Name: {key}')
        print(f'Password: {dic[key]}')
        try:
            if validate(key, dic[key]):
                print(f'Status: OK')
        except Exception as e:
            print(f'Status: {e}')
        print('-----')
