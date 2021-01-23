'''
HT #13 - термін виконання - 20.01.2021 (наступна середа).
Перепишіть програму-банкомат на використання бази даних для збереження всих даних. 
Використовувати БД sqlite3 та натівний Python.
'''

import sqlite3 
import json
import os
import random
 
def check_user():
    tries = 0
    while tries < 3:
        atm_database = 'ATM_database.db'
        with sqlite3.connect(atm_database) as db:
            cursor = db.cursor()
        username = input("Введіть ім'я користувача: ")
        password = input('Введіть пароль: ')
        find_user = ('SELECT * FROM users WHERE username = ?')
        cursor.execute(find_user, [username])
        result_find_user = cursor.fetchone()
        find_password = ('SELECT * FROM users WHERE password = ?')
        cursor.execute(find_password, [password])
        result_find_password = cursor.fetchone()
        if  result_find_user:  # перевірка login user
            result_find_user = result_find_user[0]
            if  result_find_password:  # перевірка пароля user
                result_find_password = result_find_password[0]
                print("Ви ввійшли до банківської системи!\n")
                if username == 'admin':
                    atm_collection(username)  # перехід в режим інкасації
                return username # повернення до меню користувача банкомату
            else:
                print('Ви ввели невірний пароль !')
                tries += 1
        else:
            print("Будь ласка, введіть коректне ім'я!")
            tries += 1
    print('Вибачне, але Ви тричі ввели невірні данні.\n Ваша картка буде заблокована!')
    return False
 
 
def atm_collection(user):
    while True:
        selection = int(input('''Введіть дію: 
    1. Переглянути залишок коштів у банкоматі
    2. Поповнити банкомат
    3. Вихід
 
 Ваш вибір: '''))
        if selection == 1:
            print('Перегляд балансу банкомату.')
            operation = "check balance ATM"
            print(f'Всього в банкоматі {check_balance_ATM(operation)} грн.\n')
        elif selection == 2:
            print('Поповнення банкомату.')
            # operation = "load ATM"
            load_atm(user)
        elif selection == 3:
            print('Вихід!')
            print('Дякуємо за Ваш вибір!')
            break
        else:
            print('Неправильний вибір! Повторіть спробу!')
    else:
        print('Програма "Банкомат" завершила свою роботу!')
 
 
def get_money(money):  # находження минимальної можливої суми для видачі грошей за допомогою алгоритму динамічного програмування
    lst_banknotes = [1000, 500, 200, 100, 50, 20]
    INF = 10 ** 10
    F = [INF] * (money + 1)
    F [0] = 0
    for k in range(1, money + 1):
        for i in range(len(lst_banknotes)):
            if k - lst_banknotes[i] >= 0 and F[k - lst_banknotes[i]] < F[k]:
                F[k] = F[k - lst_banknotes[i]]
        F[k] += 1
    result_banknotes = []
    k = money
    while k != 0:
        for i in range(len(lst_banknotes)):
            if k-lst_banknotes[i] >= 0 and F[k] == F[k - lst_banknotes[i]] + 1:
                result_banknotes.append(lst_banknotes[i])
                k -= lst_banknotes[i]
    return result_banknotes
 
 
def check_enough_banknotes_atm(money):  # перевірка достатньої кількості номіналів банкнот у банкоматі, наприк. money = 660
    lst_banknotes =  get_money(money)  # виклик get_money наприк. [500, 100, 20, 20, 20]
    dict_number_banknotes = {str(i): lst_banknotes.count(i) for i in lst_banknotes}  # наприк. {'100': 1, '20': 3, '500': 1}
    user = 'admin'
    user_file = user + "_balance.json"  # завантаження кількості всього наявних банкнот
    with open(user_file, "r") as f:
        dict_admin_balance =  json.load(f)  # наприк. {"20": 60, "50": 50, "100": 50, "200": 50, "500": 50, "1000": 50}
    result_dict = {key: dict_admin_balance[key]-dict_number_banknotes[key] for key in dict_admin_balance if key in dict_number_banknotes}  # перевірка на залишення в банкоматі коштів при знятті грошей, наприк. {'20': 0, '100': 49, '500': 49}
    return all(value >= 0 for value in result_dict.values())
 
 
def check_balance_ATM(operation):
    user = 'admin'
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        admin_balance =  json.load(f)
    all_money = (sum(int(bancknote) * value for bancknote, value in admin_balance.items()))  
    if operation == "check balance ATM":  # вивід наявних блокнот  у банкоматі
        print(f'Всього у банкоматі: {all_money} грн.', '\n')
        print('У банкоматі знаходиться: ')
        for bancknote, value in admin_balance.items():
            print(f"Банкнот {bancknote} грн. - {value} шт.")
        add_transaction(user, operation, all_money)  # допис у файл транзакції admin
    return all_money  # функція повертає всі наявні кошти у банкоматі
 
 
def check_banknote(user, banknote):  # перевіряє та повертає кількість банкнот зазначеного номіналу
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        admin_balance =  json.load(f)
    banknote = str(banknote)  # в json ключі str типу
    return admin_balance[banknote]
 
 
def add_cash_to_atm(user, banknote, number):
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        admin_balance =  json.load(f)
    banknote = str(banknote)  # в json ключі str типу даних
    admin_balance[banknote] += number
    with open(user_file, "w") as f:
        json.dump(admin_balance, f)
    with open(user_file, "r") as f:
        balance =  json.load(f)
    operation = "load ATM"
    banknote = int(banknote)  # для арифметичних дій треба числовий тип даних
    money = banknote * number  # сумма поповнення вказаного номіналу
    add_transaction(user, operation, money)
    print(f'В банкомат завантажено {number} банкнот  по {banknote} грн. Всього завантажено {money} грн.\n')
 
 
def load_atm(user):
    banknote = input('Введіть номінал поповнення 20, 50, 100, 200, 500 чи 1000 грн.: ')
    if banknote.isdigit():
        banknote = int(banknote)
        if banknote in [20, 50, 100, 200, 500, 1000]:
            number = input('Введіть кількість банкнот поповнення: ')
            if number.isdigit():
                number = int(number)
                if 0 < number < 100:
                    banknotes_in_atm  = check_banknote(user, banknote)
                    if number + banknotes_in_atm <= 100:
                        add_cash_to_atm(user, banknote, number)  # виклик функції внесення грошей 
                    else:
                         print(f'В банкоматі банкнота {banknote} грн. у кількості {banknotes_in_atm} шт. \n\
Можна цю банкноту покласти у кількості {100 - banknotes_in_atm} шт.')
                else:
                    print('В банкомат можна завантажити від 1 до 100 банкнот. Ввведіть коректну кількість.')        
            else:
                print('Будь ласка, введіть лише цифрове значення!\n')
        else:
            print('Банкомат не підтримує даний номінал!')
    else:
        print('Будь ласка, введіть лише цифрове значення!\n')        
 
 
def add_transaction(user, operation, money):
    user_account = user + '_transactions'
    atm_database = 'ATM_database.db'
    with sqlite3.connect(atm_database) as db:
        cursor = db.cursor()
    # Create a table for user inside 'ATM_database.db' with create some fields: Transaction Operation Balance
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {user_account} (
        Transactions INTEGER PRIMARY KEY AUTOINCREMENT,
        Operation    CHAR    NOT NULL,
        Balance      TEXT    NOT NULL
        );''')
    db.commit ()
    # check user operation
    if operation == "deposite":
        money = "+" + str(money)
    elif operation == "withdraw":
        money = "-" + str(money)
    # work for dict of user_info
    user_info = {'Operation':operation, 'Balance':money}
    user_sql = (f"INSERT INTO {user_account} VALUES (NULL, :Operation, :Balance)")
    cursor.execute(user_sql, user_info)
    db.commit ()
    # # work for list of user_info
    # user_info = [operation, money]  
    # user_sql = f"INSERT INTO {user_account} VALUES (NULL, ?, ?);"
    # cursor.execute(user_sql, user_info)
    # db.commit ()
    return
 
 
def check_balance(user, operation):
    atm_database = 'ATM_database.db'
    with sqlite3.connect(atm_database) as db:
        cursor = db.cursor()
    find_balance = ('SELECT account FROM users_balances WHERE username = ?')
    cursor.execute(find_balance, [user])
    balance = cursor.fetchone()
    money = balance[0]  
    if operation == "deposite" or operation == "withdraw" or operation == "user bonus":
        return money
    else:
        add_transaction(user, operation, money)
    return money
 
 
def deposite(user, money):
    operation = "deposite"
    atm_database = 'ATM_database.db'
    with sqlite3.connect(atm_database) as db:
        cursor = db.cursor()
    find_balance = ('SELECT account FROM users_balances WHERE username = ?')
    cursor.execute(find_balance, [user])
    balance = cursor.fetchone()
    balance = balance[0]
    balance += money  # add money to user account
    update_balance = ('UPDATE users_balances SET account = ? WHERE username = ?')
    cursor.execute(update_balance, [balance, user])
    db.commit()
    add_transaction(user, operation, money)
    return balance
 
 
def withdraw(user, money):  
    operation = "withdraw"

    atm_database = 'ATM_database.db'
    with sqlite3.connect(atm_database) as db:
        cursor = db.cursor()
    find_balance = ('SELECT account FROM users_balances WHERE username = ?')
    cursor.execute(find_balance, [user])
    balance = cursor.fetchone()
    balance = balance[0]
    balance -= money  # списання коштів рахунку user
    update_balance = ('UPDATE users_balances SET account = ? WHERE username = ?')
    cursor.execute(update_balance, [balance, user])
    db.commit()
    add_transaction(user, operation, money)  # запис транзакції user

    lst_banknotes =  get_money(money)  # списання коштів рахунку самого банкомату, користувач admin, частково повторює функцію check_enough_banknotes_atm(money)
    dict_number_banknotes = {str(i): lst_banknotes.count(i) for i in lst_banknotes}
    user = 'admin'
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        dict_admin_balance =  json.load(f)
    result_dict = {key: dict_admin_balance[key]-dict_number_banknotes[key] for key in dict_admin_balance if key in dict_number_banknotes}
    dict_admin_balance.update(result_dict)  # оновлення рахунку admin
    dict_digit = {int(k):v for k, v in dict_admin_balance.items()}  # сортування словника банкнот admin за зростанням для впорядкованого відображення у admin_balance.json
    dict_digit_sorted = dict(sorted(dict_digit.items()))
    dict_admin_balance_str = {str(k):v for k, v in dict_digit_sorted.items()}
    with open(user_file, "w") as f:  # оновлення файлу admin_balance.json
        json.dump(dict_admin_balance_str, f)
    add_transaction(user, operation, money)  # запис транзакції admin(ATM)
    return 
 
 
def bonus_plus(user):
    operation = "user bonus"
    atm_database = 'ATM_database.db'
    with sqlite3.connect(atm_database) as db:
        cursor = db.cursor()
    find_balance = ('SELECT account FROM users_balances WHERE username = ?')
    cursor.execute(find_balance, [user])
    balance = cursor.fetchone()
    balance = balance[0]
    bonus = int(balance * 0.1)
    balance += bonus  # add bonus to user balance
    update_balance = ('UPDATE users_balances SET account = ? WHERE username = ?')  # update user balance account
    cursor.execute(update_balance, [balance, user])
    db.commit()
    add_transaction(user, operation, bonus)
    return bonus
 
 
def start():
    user =  check_user()
    if user and user != 'admin': # перевірка, що user валідний та не admin
        bonus = random.choices([1,0],[0.1,0.9])[0]  # бонусна опція реалізується через функцію choices модуль random з вірогідністю 10%(0.1) для 1(успіх) та 90%(0.9) для 0(невдача)
        if bonus:
            operation = "user bonus"
            print(f'Вам нараховано бонус {bonus_plus(user)} грн. - 10% від Ваших коштів.\nНа Вашому рахунку {check_balance(user, operation)} грн.\n')
            
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
                    if money in [1000, 500, 200, 100, 50, 20]:
                        print(f'На Вашому рахуноку {deposite(user, money)} грн., його поповнено на суму {money} грн.\n')
                    else:
                        print('Банкомат приймає лише номінали 20, 50, 100, 200, 500 або 1000 грн.!\n')
                else:
                    print('Будь ласка, введіть лише цифрове значення!\n')    
 
            elif selection == 3:
                print('Зняття коштів.')
                operation = "withdraw"
                money = input('Введіть необхідну суму: ')
                if money.isdigit():
                    money = int(money)
                    if money != 0 and money % 10 == 0 and money not in [10, 30]:  # перевірка на можливість видачі введеної суми, а також щоб не зациклювалася функція get_money
                        if check_balance(user, operation) - money >= 0:  # перевірка чи затребувана сума коштів не перевищує баланс user
                            if check_balance_ATM(operation) - money >= 0:  # перевірка чи затребувана сума коштів не перевищує баланс банкомату
                                if check_enough_banknotes_atm(money):  # перевірка достатньої кількості номіналів банкнот у банкоматі
                                    withdraw(user, money)
                                    print(f'На Вашому рахуноку {check_balance(user, operation)} грн., з нього знято {money} грн.')
                                    print('Купюрами: ', *get_money(money), 'грн.\n')
                                else:
                                    print('У банкоматі немає банкнот для видачі зазначену суму!')
                            else:
                                print('На даний момент у банкоматі недостатньо коштів для видачі вказаної суми!\n')                
                        else:
                            print('На Вашому рахунку недостатньо коштів!\n')
                    else:
                        print(f'Введенної суми, {money} грн., банкомат не може видати наявними номіналами 20, 50, 100, 200, 500 і 1000 грн!')                   
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