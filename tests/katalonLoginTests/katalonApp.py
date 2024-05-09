import time

import allure
import pytest
from selenium import webdriver
from tests.pageObjects.katalonPage import katalonPage
from allure_commons.types import AttachmentType



# Assertions


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    # ChromeOptions
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    return driver


@allure.epic("Katalon App Test")
@allure.feature("TC#0 - Katalon App Login Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    driver = setup
    katalon_Page = katalonPage(driver)
    katalon_Page.katalon_login(usr="John Doe", pwd="ThisIsNotAPassword")
    time.sleep(5)
    message = katalon_Page.make_appointment_msg()
    assert message == "Make Appointment"
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    katalon_Page.katalon_logout()
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

