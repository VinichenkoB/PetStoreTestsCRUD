import allure
from pytest import mark

from src.api.petstore import get_pet_by_status, get_pet_by_id, generate_nonexistent_pet_id


@allure.feature("Petstore Positive")
@allure.story("Reading tests")
@allure.title("Get pets by status 'available'")
@mark.petstore_positive
@mark.petstore_read_tests
@mark.test_get_pets_by_status_available
def test_get_pets_by_status_available():
    with allure.step("Getting pets with status 'available'"):
        response = get_pet_by_status("available")
    assert response.status_code == 200
    assert len(response.json()) > 0
    for pet in response.json():
        assert pet['status'] == "available"


@allure.feature("Petstore Positive")
@allure.story("Reading tests")
@allure.title("Get pets by status 'pending'")
@mark.petstore_positive
@mark.petstore_read_tests
@mark.test_get_pets_by_status_pending
def test_get_pets_by_status_pending():
    with allure.step("Getting pets with status 'pending'"):
        response = get_pet_by_status("pending")
    assert response.status_code == 200
    assert len(response.json()) > 0
    for pet in response.json():
        assert pet['status'] == "pending"


@allure.feature("Petstore Positive")
@allure.story("Reading tests")
@allure.title("Get pets by status 'sold'")
@mark.petstore_positive
@mark.petstore_read_tests
@mark.test_get_pets_by_status_sold
def test_get_pets_by_status_sold():
    with allure.step("Getting pets with status 'sold'"):
        response = get_pet_by_status("sold")
    assert response.status_code == 200
    assert len(response.json()) > 0
    for pet in response.json():
        assert pet['status'] == "sold"


@allure.feature("Petstore Negative")
@allure.story("Reading tests")
@allure.title("Find nonexistent pet by id")
@mark.petstore_negative
@mark.petstore_read_tests
@mark.test_get_pets_by_status_sold
def test_find_nonexistent_pet_by_id():
    with allure.step("Finding pet by nonexistent id"):
        nonexistent_id = generate_nonexistent_pet_id()
        response = get_pet_by_id(nonexistent_id)
    assert response.status_code == 404
