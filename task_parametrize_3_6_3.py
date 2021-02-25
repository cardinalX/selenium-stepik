import time
import math
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture()
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    driver.quit()


class TestFeedbackCorrect:
    secret_message = ''
    link = "https://stepik.org/lesson/"
    end_link = "/step/1"
    lesson = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]
    
    @pytest.mark.parametrize("lesson", lesson)
    def test_feedback_1(self, driver, lesson):
        
        driver.get(self.link + lesson + self.end_link)

        textarea = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.CLASS_NAME, "string-quiz__textarea"))
        )
        textarea.send_keys(str(math.log(int(time.time()))))

        driver.find_element_by_class_name("submit-submission").click()
        
        feedback_result_element = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")),"feedback_result_hint not found"
        )

        # try:
        #     feedback_result_element = driver.find_element_by_class_name("smart-hints__hint")
        #     WebDriverWait(driver, 5).until(EC.presence_of_element_located(feedback_result_element))
        # except NoSuchElementException:
        #     feedback_result_element = None
        feedback_is_correct = feedback_result_element.text == "Correct!"
        if not feedback_is_correct:
            self.secret_message += feedback_result_element.text
            print(self.secret_message)
        assert feedback_is_correct, f"Опциональный фидбек о результате решения '{feedback_result_element.text}', expected 'Correct!'"
        