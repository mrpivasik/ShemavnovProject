import allure
from faker import Faker
from src.sql_features import check_user_in_db


fake = Faker()


@allure.story("Test for create new user and check in db")
def test_create_user(app, db_connection):
    new_username = fake.simple_profile()['username']
    new_password = "Qwerty1402"
    main_page = app.main_page()
    login_page = app.login_page()
    admin_page = app.admin_page()

    with allure.step('Open login page'):
        main_page.open(main_page.url)
        main_page.open_admin_panel()

    with allure.step('Login like admin and press login button'):
        login_page.fill_login_form_and_login(username="admin",
                                             password="password")

    with allure.step(f'Open User form and add new user. Username {new_username} pass {new_password}'):
        admin_page.open_users_list()
        admin_page.open_new_user_form()
        admin_page.fill_user_form(username=new_username,
                                  password=new_password)
    with allure.step(f'Check new user in db. Username {new_username}'):
        check_user_in_db(db_connection=db_connection, username=new_username)

    with allure.step('Add staff permissions for new user'):
        admin_page.give_staff_permissions()
    with allure.step("Log out"):
        admin_page.log_out()

    with allure.step(f'Login like new user. Username {new_username} pass {new_password}'):
        login_page.login_again()
        login_page.fill_login_form_and_login(username=new_username,
                                             password=new_password)
    admin_page.check_success_login_with_new_user()
