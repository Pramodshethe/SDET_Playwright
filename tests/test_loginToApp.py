from playwright.sync_api import Page, Playwright
from pages.login_page import LoginPage

def test_logintoapplication(browser_instance, user_credentials):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    login_page.login(**user_credentials)