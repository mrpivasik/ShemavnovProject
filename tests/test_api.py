import allure
from src.pages.ApiPage import ApiPage
from faker import Faker


fake = Faker()
pet_id = int(f"901{fake.random_number(digits=7)}")
name = fake.simple_profile()['username']
new_name = f"New_{fake.simple_profile()['username']}"


@allure.story("Test for create and check new pet")
def test_create_new_pet():
    pet_api = ApiPage()
    with allure.step('Create new pet'):
        pet_api.add_new_pet_with_api(pet_id=pet_id, name=name)
    with allure.step('Check new pet'):
        pet_check = pet_api.check_new_pet_with_api(pet_id=pet_id)
    assert pet_check.get("id") == pet_id and pet_check.get("name") == name


@allure.story("Test for update pet")
def test_update_pet():
    pet_api = ApiPage()
    with allure.step('Update name of pet'):
        pet_api.update_pet_with_api(pet_id=pet_id, new_name=new_name)
    with allure.step('Check update'):
        pet_check = pet_api.check_new_pet_after_update(pet_id=pet_id, new_name=new_name)
    assert pet_check.get("name") == new_name
