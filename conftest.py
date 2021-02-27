import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# supported_browsers = {
#     'chrome': webdriver.Chrome,
#     'firefox': webdriver.Firefox
# }


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or en")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    supported_languages = [
        "ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it",
        "ko", "nl", "pl", "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-hans"
        ]

    if user_language not in supported_languages: 
        raise pytest.UsageError(f"--language {user_language} not valid; available values is: {supported_languages}")

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    # # "лучше попробовать и получить ошибку, чем каждый раз спрашивать разрешение", 
    # # поэтому более предпочтительный подход с использованием исключений.
    # try: 
    #     browser = supported_browsers[browser_name]()
    # except KeyError:
    #     joined_browsers = ', '.join(supported_browsers.keys())
    #     raise pytest.UsageError(f"--browser_name is invalid, supported browsers: {joined_browsers}")

    # if browser_name in supported_browsers:
    #     browser = supported_browsers.get(browser_name)()
    #     print(f"\nstart {browser_name} browser for test..")
    # else:
    #     joined_browsers = ', '.join(supported_browsers.keys())
    #     raise pytest.UsageError(f"--browser_name is invalid, supported browsers: {joined_browsers}")

    yield browser
    print("\nquit browser..")
    browser.quit()