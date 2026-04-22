import json
from pathlib import Path
import pytest
from playwright.sync_api import Playwright

current_directory = Path(__file__).parent
file_path = current_directory / "data" / "creds.json"

with open(file_path) as f:
    creds_data = json.load(f)["user_creds"]

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
    parser.addoption(
        "--url_link", action="store", default="url", help="server selection"
    )

@pytest.fixture(scope="session", params=creds_data)
def user_credentials(request):
    return request.param

@pytest.fixture(scope="session")
def browser_type(playwright: Playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == 'firefox':
        browser = playwright.firefox.launch(headless=False)

    yield browser
    browser.close()

@pytest.fixture
def browser_instance(browser_type):
    context = browser_type.new_context()
    page = context.new_page()
    yield page
    context.close()