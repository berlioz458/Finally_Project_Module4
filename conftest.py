import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# обработчик языка из командной строки
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    # тут мы берем и при помощи метода add_experimental_option задаем язык пользователя из опшена который писали в
    # консоли
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(30)
    yield browser
    print("\nquit browser..")
    browser.quit()
