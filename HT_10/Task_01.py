'''
НТ #10
За допомогою Selenium зайти на сайт ОЛХ, ввести в пошук будь-який запит, дочекатись отримання результатів 
і зберегти скріншот сторінки.
'''

from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.olx.ua/")
my_search = driver.find_element_by_id('headerSearch')
my_search.send_keys('Гінко білоба')
my_search.send_keys(Keys.ENTER)
sleep(3)
driver.get_screenshot_as_file('my_search.jpg')
driver.quit()
