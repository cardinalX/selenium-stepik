from selenium import webdriver
import time
import unittest

class TestRegInfoForm(unittest.TestCase):
    def test_reg_info1(self):
        try: 
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # код, который заполняет обязательные поля
            inputFirstName = browser.find_element_by_css_selector('input.first:required')
            inputFirstName.send_keys("inputFirstName Reg Info")
            inputSecondName = browser.find_element_by_css_selector('input.second:required')
            inputSecondName.send_keys("inputSecondName Reg Info")
            inputEmail = browser.find_element_by_css_selector('input.third:required')
            inputEmail.send_keys("inputEmail Reg Info")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_reg_info2(self):
        try: 
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # код, который заполняет обязательные поля
            inputFirstName = browser.find_element_by_css_selector('input.first:required')
            inputFirstName.send_keys("inputFirstName Reg Info")
            inputSecondName = browser.find_element_by_css_selector('input.second:required')
            inputSecondName.send_keys("inputSecondName Reg Info")
            inputEmail = browser.find_element_by_css_selector('input.third:required')
            inputEmail.send_keys("inputEmail Reg Info")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

if __name__ == "__main__":
    unittest.main()