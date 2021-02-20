import time
import math
import pyperclip

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    assert price
    browser.find_element(By.ID, "book").click()

    # Код, который заполняет обязательные поля
    # считываем значение Х
    xValue = browser.find_element_by_id("input_value").text
    # Заполняем
    inputAnswer = browser.find_element_by_id("answer")
    inputAnswer.send_keys(calc(xValue))

    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    button.click()
    stepikAnswer = browser.switch_to.alert.text.split(": ")[-1]
    pyperclip.copy(stepikAnswer)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    browser.quit()