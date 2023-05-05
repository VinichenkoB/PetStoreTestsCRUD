import random
import allure
from pytest import mark

from src.api.petstore import add_new_pet, update_pet, generate_unsupported_pet_id, \
                             pet_identifier, pet_name, pet_status


@allure.feature("Petstore Positive")
@allure.story("Updating tests")
@allure.title("Update pet")
@mark.petstore_positive
@mark.petstore_update_tests
@mark.test_update_pet
def test_update_pet():
    with allure.step("Creating new pet"):
        response = add_new_pet(pet_identifier, pet_name, pet_status)
    pet_id = response.json()['id']
    updated_name = pet_name + " Updated"
    updated_status = random.choice(['available', 'pending', 'sold'])
    with allure.step("Updating pet"):
        response = update_pet(pet_id, updated_name, updated_status)
    assert response.status_code == 200
    assert response.json()['name'] == updated_name
    assert response.json()['status'] == updated_status


@allure.feature("Petstore Negative")
@allure.story("Updating tests")
@allure.title("Update nonexistent pet with long ID")
@mark.petstore_negative
@mark.petstore_update_tests
@mark.test_update_nonexistent_long_pet_id
def test_update_nonexistent_long_pet_id():
    with allure.step("Trying to update nonexistent pet with long ID"):
        nonexistent_long_pet_id = generate_unsupported_pet_id()
        updated_name = pet_name + " Updated"
        updated_status = random.choice(['available', 'pending', 'sold'])
        response = update_pet(nonexistent_long_pet_id, updated_name, updated_status)
    assert response.status_code == 500
