from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from constants import Constants

faker = Faker()


class Test:
    def test_registration_successful_registration(self, driver):
        email = faker.email()
        driver.find_element(*Locators.LOG_IN_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LINK_TEXT_REGISTRATION)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTER))
        driver.find_element(*Locators.NAME_FIELD_REG).send_keys(Constants.NAME_REG)
        driver.find_element(*Locators.EMAIL_FIELD_REG).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD_REG).send_keys(Constants.CORRECT_PASSWORD)
        driver.find_element(*Locators.REGISTER).click()
        driver.get(Constants.URL)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_FORM))
        driver.find_element(*Locators.EMAIL_FIELD_LOG).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD_LOG).send_keys(Constants.CORRECT_PASSWORD)
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.NAME_IN_ACCOUNT))
        value = driver.find_element(*Locators.NAME_IN_ACCOUNT).get_attribute('value')
        assert Constants.NAME_REG in value

    # Проверяем ошибку для некорректного пароля при регистрации
    def test_invalid_password_error(self, driver):
        driver.find_element(*Locators.LOG_IN_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LINK_TEXT_REGISTRATION))

        driver.find_element(*Locators.LINK_TEXT_REGISTRATION).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTER))

        driver.find_element(*Locators.NAME_FIELD_REG).send_keys(Constants.NAME_REG)
        driver.find_element(*Locators.EMAIL_FIELD_REG).send_keys(Constants.EMAIL_REG)
        driver.find_element(*Locators.PASSWORD_FIELD_REG).send_keys(Constants.INVALID_PASSWORD)
        driver.find_element(*Locators.REGISTER).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ERROR_MESSAGE))
