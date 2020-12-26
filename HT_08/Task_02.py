'''
Хей! Домашка №8:
 
2. https://www.olx.ua - написати скрейпер, який буде брати із https://www.olx.ua/sitemap.xml 
першу лінку, відкривати категорію і збирати ім'я і номер з кожної об'яви.
'''


import requests
from bs4 import BeautifulSoup
import fake_useragent
import csv
import os
import time
import re
 
html_start = 'https://www.olx.ua/sitemap.xml'
user = fake_useragent.UserAgent().random
HEADERS = {'user-agent': user}
data_file = 'data_olx.csv'


def write_csv(data, data_file):
    if os.path.isfile(data_file):
        with open(data_file, "a", newline="") as f:
            columns = ['Name', 'Phones']
            writer = csv.DictWriter(f, fieldnames=columns)
            # writer.writeheader()
            writer.writerow(data)
    else:
        with open(data_file, "w", newline="") as f:
            columns = ['Name', 'Phones']
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            writer.writerow(data)
    return


def get_html(url, headers):
    r = requests.get(url, headers)
    return r


responce_1 = get_html(html_start, headers= HEADERS)
soup_1 = BeautifulSoup(responce_1.text, 'lxml')
html_1 = soup_1.find('loc').text.strip()

responce_2 = get_html(html_1, headers= HEADERS)
soup_2 = BeautifulSoup(responce_2.text, 'lxml')
html_3 = soup_2.find_all('loc')[0].text.strip()  # шукаю товари в першій категорії
 
responce_3 = get_html(html_3, headers= HEADERS)
soup_3 = BeautifulSoup(responce_3.text, 'lxml')
final_html = soup_3.find_all('div', class_='offer-wrapper')


def get_content(html, headers):
    for i  in html:
        session = requests.Session()
        link = i.find('div', class_='space rel').find('a').get('href')
        response = session.get(link)
        token_re = r"var phoneToken = '(.*?)';"
        id_re = r"'id':'(.*?)',"
        try:
            token = re.findall(token_re, response.text)[0]
            site_id = re.findall(id_re, response.text)[0]
        except:
            continue
        session.headers = {
            'user-agent': user,
            'referer': f'{link}'
        }
        phone_number = f'https://www.olx.ua/ajax/misc/contact/phone/{site_id}/?pt={token}'
        phone_response = session.get(phone_number)
        phone_number_finale = phone_response.json()['value']
        if phone_number_finale[0] == '<':  # перевірка, коли телефонних номері >= 2 штук
            phone_str = BeautifulSoup(phone_number_finale, 'lxml')
            phones_lst = [span.text for span in phone_str.select("span")]
            phones = ', '.join(phones_lst)
        else:
            phones = phone_number_finale
        soup_name = BeautifulSoup(response.text, 'lxml')
        try:  # пропуск ітераціїї, коли ім'я не вказано
            name = soup_name.select_one('div[class*="offer-user__action"] a').text.strip()
        except:
            continue
        print(f'Name: {name}\nPhone: {phones}\n')
        data = {'Name':name, 'Phones':phones}
        data_file = 'data_olx.csv'
        write_csv(data, data_file)
        time.sleep(1)
    return


get_content(final_html, HEADERS)