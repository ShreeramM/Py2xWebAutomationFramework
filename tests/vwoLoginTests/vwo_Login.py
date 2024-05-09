import time

import allure
import pytest
from selenium import webdriver
from tests.pageObjects.loginPage import LoginPage
from allure_commons.types import AttachmentType



# Assertions


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    # ChromeOptions
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver


@allure.epic("VWO Login Test")
@allure.feature("TC#0 - VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    driver = setup
    loginpage = LoginPage(driver)
    loginpage.vwo_login(usr="admin@admin@gmail.com", pwd="admin")
    time.sleep(5)
    error_message = loginpage.error_message_text()
    assert error_message == "Your email, password, IP address or location did not match"
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


