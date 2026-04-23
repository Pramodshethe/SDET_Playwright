import time

from playwright.sync_api import expect


class LoginPage:
    def __init__(self, browser_instance):
        self.browser_instance = browser_instance

    def navigate(self):
        self.browser_instance.goto('https://automationexercise.com/')

    def login(self, username, Password, **kwargs):
        self.browser_instance.get_by_role('link', name=' Signup / Login').click()
        self.browser_instance.locator("//input[@data-qa='login-email']").fill(username)
        self.browser_instance.get_by_role('textbox', name='password').fill(Password)
        self.browser_instance.get_by_role('button', name='Login').click()
        time.sleep(5)

    def incorrect_login(self, username, Password, **kwargs):
        self.browser_instance.goto('https://automationexercise.com/login')
        self.browser_instance.locator("//input[@data-qa='login-email']").fill(username)
        self.browser_instance.get_by_role('textbox', name='password').fill(Password)
        self.browser_instance.get_by_role('button', name='Login').click()
        expect(self.browser_instance.get_by_text("Your email or password is incorrect!")).to_be_visible()
        time.sleep(5)
