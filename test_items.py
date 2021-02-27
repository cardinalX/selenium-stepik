import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class TestPythonAnywhereParametrize:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    def test_feedback_1(self, browser):
        
        browser.get(self.link)

        # Проверяем, что страница товара на сайте содержит кнопку добавления в корзину.
        # можно искать через presence_, но тогда, если кнопка чем-то перекрыта, об этом не узнаем.
        button_add_to_basket = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket")), 
            "Button add to basket at page of catalog item not found!"
        )
        