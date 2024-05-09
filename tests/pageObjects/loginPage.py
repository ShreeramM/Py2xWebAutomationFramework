# Page Class
# Page Locators
# Page Actions
# Webdriver intialization
# Custom functions(no asserts in Page object class)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    submitbtn = (By.XPATH, "//button[@id='js-login-btn']")
    error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def submit(self):
        return self.driver.find_element(*LoginPage.submitbtn)

    def error_msg(self):
        return self.driver.find_element(*LoginPage.error_message)

    def vwo_login(self, usr, pwd):
        self.get_username().send_keys(usr)
        self.get_password().send_keys(pwd)
        self.submit().click()

    def error_message_text(self):
        return self.error_msg().text
