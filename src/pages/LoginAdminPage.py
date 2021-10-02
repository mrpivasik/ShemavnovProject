from src.pages.BasePage import BasePage
from src.locators import LoginAdminPageLocators


class LoginAdminPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def fill_login_form_and_login(self, username, password):
        admin_username = self.easy_find_element(LoginAdminPageLocators.USERNAME_LOCATOR)
        admin_username.send_keys(username)
        admin_pass = self.easy_find_element(LoginAdminPageLocators.PASSWORD_LOCATOR)
        admin_pass.send_keys(password)
        login_button = self.easy_find_element(LoginAdminPageLocators.BUTTON_LOCATOR)
        login_button.click()

    def login_again(self):
        log_in_again = self.easy_find_element(LoginAdminPageLocators.LOGIN_AGAIN_LOCATOR)
        log_in_again.click()
