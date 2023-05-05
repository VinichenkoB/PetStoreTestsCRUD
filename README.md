# PetStoreTestsCRUD
This repository contains CRUD (Create, Read, Update, Delete) tests for the PetStore API using Python, PyTest, and Poetry. The PetStore API is a sample RESTful API that allows you to manage the resources of a pet store application, such as pets, orders, and users.

## Getting Started
These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites
To run the tests, make sure you have the following software installed on your system:
- Python 3.7 or higher
- Poetry (Python dependency management tool)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/VinichenkoB/PetStoreTestsCRUD.git

```
2. Navigate to the project directory:
```bash
cd PetStoreTestsCRUD
```

3. Install the required packages using Poetry:
```bash
poetry install
```

## Running the Tests
To run the tests, execute the following command in the project directory:

Run all tests:
```bash
poetry run pytest
```

Run specific tests by decorator name:
```bash
python -m pytest -m {decorator name}
```
Example:
```bash
pytest -m petstore_create_tests
```

Run tests with allure reports:
```bash
poetry run pytest --alluredir=allure-results
allure serve allure-results
```