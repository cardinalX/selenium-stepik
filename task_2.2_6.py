from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Код, который заполняет обязательные поля
    # считываем значение Х
    xValue = browser.find_element_by_id("input_value").text
    # скроллим
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script('return arguments[0].scrollIntoView({block: "center"});', button)
    # Заполняем
    checkBox = browser.find_element_by_id("robotCheckbox")
    checkBox.click()
    browser.find_element_by_css_selector('[for="robotsRule"]').click()
    inputAnswer = browser.find_element_by_id("answer")
    inputAnswer.send_keys(calc(xValue))

    # Отправляем заполненную форму
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
