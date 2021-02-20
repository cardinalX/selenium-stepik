from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Код, который заполняет обязательные поля
    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    sum = int(num1.text) + int(num2.text)
    select = Select(browser.find_element_by_id("dropdown"))
    #select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
