import pytest
import allure
from selenium import webdriver
from src.pages.Application import Application


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def app(browser):
    return Application(browser)


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
