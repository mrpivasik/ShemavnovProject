import time
from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from src.locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.url = "http://localhost:8000/"

    def open_admin_panel(self):
        admin_button = self.easy_find_element(MainPageLocators.ADMIN_LOGIN_BUTTON)
        admin_button.click()

    def get_first_image(self):
        time.sleep(2)
        first_image = self.easy_find_element(MainPageLocators.FIRST_IMAGE_LOCATOR).get_attribute("src")
        return first_image

    def check_missing_image(self, img):
        time.sleep(2)
        assert len(self.browser.find_elements(By.XPATH, f"//img[@src='{img}']")) == 0, \
            "Missing image stayed on the page"
