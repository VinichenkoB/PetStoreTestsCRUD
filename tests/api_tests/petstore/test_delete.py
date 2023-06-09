import allure
from pytest import mark
from src.api.petstore import PetStore

pet_store = PetStore()


@allure.feature("Petstore Positive")
@allure.story("Deleting tests")
@allure.title("Delete pet")
@mark.petstore_crud
@mark.petstore_positive
@mark.petstore_delete_tests
@mark.test_delete_pet
def test_delete_pet():
    pet_id = pet_store.generate_nonexistent_pet_id()
    with allure.step("Creating new pet"):
        response_after_pet_creation = pet_store.add_new_pet(pet_id, pet_store.pet_name, pet_store.pet_status)
    pet_id = response_after_pet_creation.json()['id']
    with allure.step("Deleting created pet"):
        response_after_pet_deleting = pet_store.delete_pet(pet_id)
    assert response_after_pet_deleting.status_code == 200
    with allure.step("Checking if pet is deleted"):
        response_after_get_order = pet_store.get_pet_by_id(pet_id)
    assert response_after_get_order.status_code == 404


@allure.feature("Petstore Negative")
@allure.story("Deleting tests")
@allure.title("Delete nonexistent pet")
@mark.petstore_crud
@mark.petstore_negative
@mark.petstore_delete_tests
@mark.test_delete_nonexistent_pet
def test_delete_nonexistent_pet():
    with allure.step("Trying to delete nonexistent pet"):
        nonexistent_pet_identifier = pet_store.generate_nonexistent_pet_id()
        response = pet_store.delete_pet(nonexistent_pet_identifier)
    assert response.status_code == 404
