import pytest
from selenium import webdriver

from constants import Constants
from locators import Locators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Constants.URL)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.LOG_IN_TO_ACCOUNT).click()
    driver.find_element(*Locators.EMAIL_FIELD_LOG).send_keys(Constants.EMAIL_USER)
    driver.find_element(*Locators.PASSWORD_FIELD_LOG).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOG_IN_BUTTON).click()
    return driver
