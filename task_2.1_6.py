from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("arm")
    print("value of people radio: ", people_checked)
    print(type(people_checked) is str)
    assert people_checked is not None, "People radio is not selected by default"

    # Отправляем заполненную форму
    #button = browser.find_element_by_css_selector("button.btn")
    #button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
