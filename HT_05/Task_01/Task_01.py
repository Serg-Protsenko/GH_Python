'''
Для самостійного вивчення: модуль json та робота з JSON файлами в Python
1. Програма-банкомат.
   Створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - 
        зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
      - потім - елементарне меню типа:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив :)
'''

import json
import os

def check_user():
    tries = 0
    while tries < 3:
        file_json = "users.json"
        
        with open(file_json, "r") as f:
            users_data = json.load(f)
        
        username = input("Введіть ім'я користувача: ")
        password = input('Введіть пароль: ')
        if  any(i.get('username') == username for i in users_data):
            if any(i.get('password') == password for i in users_data):
                print("Ви ввійшли до банківської системи!\n")
                return username
            else:
                print('Ви ввели невірний пароль !')
                tries += 1
        else:
            print("Будь ласка, введіть коректне ім'я!")
            tries += 1

    print('Вибачне, але Ви тричі ввели невірні данні.\n Ваша картка буде заблокована!')
    return False


def add_transaction(user, operation, money):
    transaction_file = str(user) + "_transactions.json"

    if os.path.isfile(transaction_file):
        with open(transaction_file, "r",encoding="utf-8") as f:
            info = json.load(f)
            number_transaction = info[-1]["Transaction"] + 1
    else:
         number_transaction = 1

    if operation == "deposite":
        money = "+" + str(money)
    elif operation == "withdraw":
        money = "-" + str(money)

    user_info = {"Transaction":number_transaction,
              "Operation":operation,
              "Balance":money}

    if os.path.isfile(transaction_file):
        with open(transaction_file, "r",encoding="utf-8") as f:
            info = json.load(f)

        info.append(user_info)
        with open(transaction_file, "w",encoding="utf-8") as f:
            json.dump(info, f, indent=4, ensure_ascii=False)

    else:
        with open(transaction_file, "w", encoding="utf-8") as f:
            lst = []
            lst.append(user_info)
            json.dump(lst, f, indent=4, ensure_ascii=False)
    return


def check_balance(user, operation):
    user_file = str(user) + "_balance.json"
    with open(user_file, "r") as f:
        balance =  json.load(f)
    
    money = balance["account"]    
    if operation == "deposite" or operation == "withdraw":
        return money
    else:
        add_transaction(user, operation, money)
    return money


def deposite(user, money):
    user_file = str(user) + "_balance.json"
    with open(user_file, "r") as f:
        balance =  json.load(f)
    balance["account"] += money

    with open(user_file, "w") as f:
        json.dump(balance, f)
    
    with open(user_file, "r") as f:
        balance =  json.load(f)
    operation = "deposite"
    add_transaction(user, operation, money)
    return balance["account"]


def withdraw(user, money):
    user_file = str(user) + "_balance.json"
    with open(user_file, "r") as f:
        balance =  json.load(f)
    if balance["account"] - money >= 0:
        balance["account"] -= money

        with open(user_file, "w") as f:
            json.dump(balance, f)

        with open(user_file, "r") as f:
            balance =  json.load(f)
        operation = "withdraw"
        add_transaction(user, operation, money)
        return True



def start():
    user =  check_user()
    if user:
        while True:
            selection = int(input('''Введіть дію: 
    1. Продивитись баланс
    2. Поповнити баланс
    3. Зняти кошти
    4. Вихід

 Ваш вибір: '''))
            if selection == 1:
                print('Перегляд балансу.')
                operation = "check balance"
                print(f'На Вашому рахунку {check_balance(user, operation)} грн.\n')

            elif selection == 2:
                print('Поповнення балансу.')
                money = input('Введіть суму поповнення: ')
                if money.isdigit():
                    money = int(money)
                    print(f'На Вашому рахуноку {deposite(user, money)} грн., його поповнено на суму {money} грн.\n')
                else:
                    print('Будь ласка, введіть лише цифрове значення!\n')           
                
            elif selection == 3:
                print('Зняття коштів.')
                operation = "withdraw"
                money = input('Введіть необхідну суму: ')
                if money.isdigit():
                    money = int(money)
                    if withdraw(user, money):
                        print(f'На Вашому рахуноку {check_balance(user, operation)} грн., з нього знято {money} грн.\n')
                    else:
                        print('На Вашому рахунку недостатньо коштів!\n')                    
                else:
                    print('Будь ласка, введіть лише цифрове значення!\n')        

            elif selection == 4:
                print('Вихід!')
                print('Дякуємо за Ваш вибір!')
                print('Програма "Банкомат" завершила свою роботу!')
                break
            
            else:
                print('Неправильний вибір! Повторіть спробу!')    
        
    else:
        print('Програма "Банкомат" завершила свою роботу!')
   
start()