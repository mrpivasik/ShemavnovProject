import allure


@allure.story("Test for delete first image")
def test_delete_first_image(app):
    main_page = app.main_page()
    admin_page = app.admin_page()

    with allure.step('Open main page and save first image'):

        main_page.open(main_page.url)
        first_img = main_page.get_first_image()

    with allure.step('Open admin panel'):
        main_page.open_admin_panel()

    with allure.step('Open list of post and open first post'):
        admin_page.open_posts_list()
        admin_page.open_first_post()

    with allure.step('Delete post'):
        admin_page.delete_post()

    with allure.step('Back on main page and check missing image'):
        main_page.open(main_page.url)
        main_page.check_missing_image(img=first_img)
