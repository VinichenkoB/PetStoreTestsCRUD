import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on. Options: 'chrome' or 'firefox'"
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_choice = request.config.getoption("browser")
    options = None

    if browser_choice.lower() == "chrome":
        options = ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
    elif browser_choice.lower() == "firefox":
        options = FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_choice}")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 10)
