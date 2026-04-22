import time


class LoginPage:
    def __init__(self, browser_instance):
        self.browser_instance = browser_instance

    def navigate(self):
        self.browser_instance.goto('https://automationexercise.com/')

    def login(self, username, Password):
        self.browser_instance.get_by_role('link', name=' Signup / Login').click()
        self.browser_instance.locator("//input[@data-qa='login-email']").fill(username)
        self.browser_instance.get_by_role('textbox', name='password').fill(Password)
        self.browser_instance.get_by_role('button', name='Login').click()
        time.sleep(5)


