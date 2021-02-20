import os
import time
import math

from selenium import webdriver
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Код, который заполняет обязательные поля
    button = browser.find_element_by_css_selector("button.btn")
    
    inputFirstName = browser.find_element_by_name("firstname")
    inputFirstName.send_keys("Mike")
    inputLastName = browser.find_element_by_name("lastname")
    inputLastName.send_keys("Petrov")
    inputLastName = browser.find_element_by_name("email")
    inputLastName.send_keys("emailya.com")

    fileElement = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'empty.txt')
    fileElement.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()