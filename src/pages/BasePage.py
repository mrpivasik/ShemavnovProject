from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def easy_find_element(self, locator: tuple, wait_time=20):
        element = WebDriverWait(self.browser, wait_time)\
            .until(EC.presence_of_element_located(locator))

        return element
