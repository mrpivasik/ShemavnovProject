from selenium.webdriver.common.by import By


class MainPageLocators:
    ADMIN_LOGIN_BUTTON = (By.XPATH, "//a[contains(., 'Go to Admin')]")
    FIRST_IMAGE_LOCATOR = (By.CLASS_NAME, "card-img-top")


class LoginAdminPageLocators:
    USERNAME_LOCATOR = (By.ID, "id_username")
    PASSWORD_LOCATOR = (By.ID, "id_password")
    BUTTON_LOCATOR = (By.XPATH, "//input[@value='Log in']")
    LOGIN_AGAIN_LOCATOR = (By.XPATH, "//a[contains(., 'Log in again')]")


class AdminPageLocators:
    USERS_LIST_LOCATOR = (By.XPATH, "//a[contains(., 'Users')]")
    NEW_USER_FORM_LOCATOR = (By.XPATH, "//a[contains(., 'Add user')]")
    NEW_USERNAME_LOCATOR = (By.ID, "id_username")
    NEW_PASSWORD_LOCATOR = (By.ID, "id_password1")
    CONFIRM_PASSWORD_LOCATOR = (By.ID, "id_password2")
    SAVE_LOCATOR = (By.CLASS_NAME, "default")
    STAFF_LOCATOR = (By.ID, "id_is_staff")
    SUPERUSER_LOCATOR = (By.ID, "id_is_superuser")
    SAVE_SUPER_LOCATOR = (By.CLASS_NAME, "default")
    LOGOUT_LOCATOR = (By.XPATH, "//a[contains(., 'Log out')]")
    POSTS_LISTS_LOCATOR = (By.XPATH, "//a[contains(., 'Posts')]")
    FIRST_POST_LOCATOR = (By.XPATH, "//a[contains(., 'Post object')]")
    DELETE_BUTTON_LOCATOR = (By.XPATH, "//a[contains(., 'Delete')]")
    CONFIRM_DELETE_LOCATOR = (By.XPATH, "//input[@type='submit']")
