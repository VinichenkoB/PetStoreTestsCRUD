import json
import random
import requests

base_url = "https://petstore.swagger.io/v2/pet"

headers = {'content-type': 'application/json'}

pet_name = 'Test Pet ' + str(random.randint(1, 1000))
pet_status = random.choice(['available', 'pending', 'sold'])


def get_pet_by_status(status):
    params = {"status": status}
    response = requests.get(base_url + "/findByStatus", params=params)
    return response


def generate_nonexistent_pet_id():

    available_response = get_pet_by_status("available")
    available_pet_data = available_response.json()
    available_pet_ids = [pet['id'] for pet in available_pet_data]

    pending_response = get_pet_by_status("pending")
    pending_pet_data = pending_response.json()
    pending_pet_ids = [pet['id'] for pet in pending_pet_data]

    sold_response = get_pet_by_status("sold")
    sold_pet_data = sold_response.json()
    sold_pet_ids = [pet['id'] for pet in sold_pet_data]

    all_existent_ids = available_pet_ids + pending_pet_ids + sold_pet_ids

    while True:
        nonexistent_id = random.randint(10000, 99999)
        if nonexistent_id not in all_existent_ids:
            print(f"{nonexistent_id} id is unique")
            break
    return nonexistent_id


pet_identifier = generate_nonexistent_pet_id()


def generate_unsupported_pet_id ():
    long_pet_id = random.randint(100000000000000000000, 999999999999999999999)
    print({"nonexistent_long_pet_id": long_pet_id})
    return long_pet_id


def add_new_pet(pet_identifier, pet_name, pet_status):
    data = {
        "id": pet_identifier,
        "name": pet_name,
        "status": pet_status
    }
    response = requests.post(base_url, data=json.dumps(data), headers=headers)
    print({"pet_identifier": pet_identifier})
    print({"pet_name": pet_name})
    print({"pet_status": pet_status})
    return response


def get_pet_by_id(pet_identifier):
    response = requests.get(base_url + "/" + str(pet_identifier))
    return response


def update_pet(pet_identifier, pet_name, status):
    data = {
        "id": pet_identifier,
        "name": pet_name,
        "status": status
    }
    response = requests.put(base_url, data=json.dumps(data), headers=headers)
    return response


def delete_pet(pet_identifier):
    response = requests.delete(base_url + "/" + str(pet_identifier))
    return response
