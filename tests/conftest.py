import pytest
import allure
import psycopg2
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.pages.Application import Application


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.implicitly_wait(20)
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def app(browser):
    return Application(browser)


@pytest.fixture(scope="session")
def db_connection():
    conn = psycopg2.connect(dbname='postgres', user='postgres',
                            password='postgres', host='localhost')
    cursor = conn.cursor()
    yield cursor
    cursor.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        try:
            if 'browser' in item.fixturenames:
                browser = item.funcargs['browser']
            else:
                print('Does not have browser fixture')
                return
            allure.attach(browser.get_screenshot_as_png(), "Screenshot",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f'Failed to make screensot: {e}')
