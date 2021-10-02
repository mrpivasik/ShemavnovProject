from selenium.webdriver.common.by import By
from src.pages.BasePage import BasePage
from src.locators import AdminPageLocators


class AdminPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open_users_list(self):
        open_users_list = self.easy_find_element(AdminPageLocators.USERS_LIST_LOCATOR)
        open_users_list.click()

    def open_new_user_form(self):
        open_user_form = self.easy_find_element(AdminPageLocators.NEW_USER_FORM_LOCATOR)
        open_user_form.click()

    def fill_user_form(self, username, password):
        new_username = self.easy_find_element(AdminPageLocators.NEW_USERNAME_LOCATOR)
        new_username.send_keys(username)
        new_password = self.easy_find_element(AdminPageLocators.NEW_PASSWORD_LOCATOR)
        new_password.send_keys(password)
        confirm_password = self.easy_find_element(AdminPageLocators.CONFIRM_PASSWORD_LOCATOR)
        confirm_password.send_keys(password)
        save_button = self.easy_find_element(AdminPageLocators.SAVE_LOCATOR)
        save_button.click()

    def give_staff_permissions(self):
        staff_checkbox = self.easy_find_element(AdminPageLocators.STAFF_LOCATOR)
        staff_checkbox.click()
        super_user = self.easy_find_element(AdminPageLocators.SUPERUSER_LOCATOR)
        super_user.click()
        save_button = self.easy_find_element(AdminPageLocators.SAVE_SUPER_LOCATOR)
        save_button.click()

    def log_out(self):
        log_out_button = self.easy_find_element(AdminPageLocators.LOGOUT_LOCATOR)
        log_out_button.click()

    def check_success_login_with_new_user(self):
        assert self.easy_find_element(AdminPageLocators.LOGOUT_LOCATOR).is_displayed()

    def open_posts_list(self):
        open_posts_list = self.easy_find_element(AdminPageLocators.POSTS_LISTS_LOCATOR)
        open_posts_list.click()

    def open_first_post(self):
        list_of_posts = self.browser.find_elements(By.XPATH, "//a[contains(., 'Post object')]")
        list_of_posts[0].click()

    def delete_post(self):
        delete_button = self.easy_find_element(AdminPageLocators.DELETE_BUTTON_LOCATOR)
        delete_button.click()
        confirm_delete = self.easy_find_element(AdminPageLocators.CONFIRM_DELETE_LOCATOR)
        confirm_delete.click()
