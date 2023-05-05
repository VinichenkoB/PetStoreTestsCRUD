import allure
from pytest import mark

from src.api.petstore import add_new_pet, get_pet_by_id, generate_unsupported_pet_id, \
                             pet_identifier, pet_name, pet_status


@allure.feature("Petstore Positive")
@allure.story("Creating tests")
@allure.title("Add new pet")
@mark.petstore_positive
@mark.petstore_create_tests
@mark.test_add_new_pet
def test_add_new_pet():
    with allure.step("Adding new pet"):
        response = add_new_pet(pet_identifier, pet_name, pet_status)
    assert response.status_code == 200
    assert response.json()['name'] == pet_name
    assert response.json()['status'] == pet_status
    with allure.step("Getting pet by id"):
        response = get_pet_by_id(pet_identifier)
    assert response.status_code == 200
    assert response.json()['name'] == pet_name
    assert response.json()['status'] == pet_status


@allure.feature("Petstore Negative")
@allure.story("Creating tests")
@allure.title("Add new pet with nonexistent long id")
@mark.petstore_negative
@mark.petstore_create_tests
@mark.test_add_new_pet_nonexistent_long_id
def test_add_new_pet_with_nonexistent_long_id():
    with allure.step("Adding new pet with unsupported id"):
        response = add_new_pet(generate_unsupported_pet_id(), pet_name, pet_status)
    assert response.status_code == 500
