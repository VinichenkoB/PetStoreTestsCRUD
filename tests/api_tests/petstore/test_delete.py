import allure
from pytest import mark

from src.api.petstore import add_new_pet, delete_pet, get_pet_by_id, generate_nonexistent_pet_id, \
                             pet_identifier, pet_name, pet_status


@allure.feature("Petstore Positive")
@allure.story("Deleting tests")
@allure.title("Delete pet")
@mark.petstore_positive
@mark.petstore_delete_tests
@mark.test_delete_pet
def test_delete_pet():
    with allure.step("Creating new pet"):
        response_after_pet_creation = add_new_pet(pet_identifier, pet_name, pet_status)
    pet_id = response_after_pet_creation.json()['id']
    with allure.step("Deleting created pet"):
        response_after_pet_deleting = delete_pet(pet_id)
    assert response_after_pet_deleting.status_code == 200
    with allure.step("Checking if pet is deleted"):
        response_after_get_order = get_pet_by_id(pet_identifier)
    assert response_after_get_order.status_code == 404


@allure.feature("Petstore Negative")
@allure.story("Deleting tests")
@allure.title("Delete nonexistent pet")
@mark.petstore_negative
@mark.petstore_delete_tests
@mark.test_delete_nonexistent_pet
def test_delete_nonexistent_pet():
    with allure.step("Trying to delete nonexistent pet"):
        nonexistent_pet_identifier = generate_nonexistent_pet_id()
        response = delete_pet(nonexistent_pet_identifier)
    assert response.status_code == 404
