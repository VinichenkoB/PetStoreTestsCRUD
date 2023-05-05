import allure
from pytest import mark
from src.api.petstore import PetStore

pet_store = PetStore()


@allure.feature("Petstore Positive")
@allure.story("Creating tests")
@allure.title("Add new pet")
@mark.petstore_crud
@mark.petstore_positive
@mark.petstore_create_tests
@mark.test_add_new_pet
def test_add_new_pet():
    pet_id = pet_store.generate_nonexistent_pet_id()
    with allure.step("Adding new pet"):
        response = pet_store.add_new_pet(pet_id, pet_store.pet_name, pet_store.pet_status)
    assert response.status_code == 200
    assert response.json()['name'] == pet_store.pet_name
    assert response.json()['status'] == pet_store.pet_status
    with allure.step("Getting pet by id"):
        response = pet_store.get_pet_by_id(pet_id)
    assert response.status_code == 200
    assert response.json()['name'] == pet_store.pet_name
    assert response.json()['status'] == pet_store.pet_status


@allure.feature("Petstore Negative")
@allure.story("Creating tests")
@allure.title("Add new pet with nonexistent long id")
@mark.petstore_crud
@mark.petstore_negative
@mark.petstore_create_tests
@mark.test_add_new_pet_nonexistent_long_id
def test_add_new_pet_with_nonexistent_long_id():
    long_pet_id = pet_store.generate_unsupported_pet_id()
    with allure.step("Adding new pet with unsupported id"):
        response = pet_store.add_new_pet(long_pet_id, pet_store.pet_name, pet_store.pet_status)
    assert response.status_code == 500
