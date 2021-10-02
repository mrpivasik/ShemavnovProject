from src.pages.AdminPage import AdminPage
from src.pages.LoginAdminPage import LoginAdminPage
from src.pages.MainPage import MainPage
from src.pages.BasePage import BasePage


class Application(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def login_page(self):
        return LoginAdminPage(self.browser)

    def main_page(self):
        return MainPage(self.browser)

    def admin_page(self):
        return AdminPage(self.browser)
