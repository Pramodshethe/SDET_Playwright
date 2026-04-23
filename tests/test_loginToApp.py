
from pages.login_page import LoginPage
from conftest import creds_data


def test_login_to_application(browser_instance, valid_user):

    login_page = LoginPage(browser_instance)
    login_page.navigate()
    login_page.login(**valid_user)


def test_invalid_login(browser_instance, invalid_user):

    login_page = LoginPage(browser_instance)
    login_page.incorrect_login(**invalid_user)