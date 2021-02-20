import time
import math
import pyperclip

from selenium import webdriver
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_class_name("btn-primary").click()
    browser.switch_to.window(browser.window_handles[1])

    # Код, который заполняет обязательные поля
    # считываем значение Х
    xValue = browser.find_element_by_id("input_value").text
    # Заполняем
    inputAnswer = browser.find_element_by_id("answer")
    inputAnswer.send_keys(calc(xValue))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    stepikAnswer = browser.switch_to.alert.text.split(": ")[-1]
    pyperclip.copy(stepikAnswer)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    print(stepikAnswer)