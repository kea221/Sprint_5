from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


class Test:
    # Проверяем вход в аккаунт по кнопке "Войти" на главной странице
    def test_login_by_button_login(self, driver):
        driver.find_element(*Locators.LOG_IN_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_FORM))

        driver.find_element(*Locators.EMAIL_FIELD_LOG).send_keys(Constants.EMAIL_USER)
        driver.find_element(*Locators.PASSWORD_FIELD_LOG).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.NAME_IN_ACCOUNT))
        value = driver.find_element(*Locators.NAME_IN_ACCOUNT).get_attribute('value')
        assert Constants.NAME_USER in value

    # Проверяем вход в аккаунт по кнопке "Личный кабинет" на главной странице
    def test_login_by_account(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_FORM))

        driver.find_element(*Locators.EMAIL_FIELD_LOG).send_keys(Constants.EMAIL_USER)
        driver.find_element(*Locators.PASSWORD_FIELD_LOG).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.NAME_IN_ACCOUNT))
        value = driver.find_element(*Locators.NAME_IN_ACCOUNT).get_attribute('value')
        assert Constants.NAME_USER in value

    # Проверяем вход в аккаунт через кнопку в форме регистрации
    def test_login_by_button_in_registration_form(self, driver):
        driver.find_element(*Locators.LOG_IN_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_FORM))

        driver.find_element(*Locators.LINK_TEXT_REGISTRATION).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTER))

        driver.find_element(*Locators.LINK_TEXT_LOGIN_IN_REG).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_FORM))
        driver.find_element(*Locators.EMAIL_FIELD_LOG).send_keys(Constants.EMAIL_USER)
        driver.find_element(*Locators.PASSWORD_FIELD_LOG).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.NAME_IN_ACCOUNT))
        value = driver.find_element(*Locators.NAME_IN_ACCOUNT).get_attribute('value')
        assert Constants.NAME_USER in value

    # Проверяем вход через кнопку в форме восстановления пароля
    def test_login_by_password_recovery(self, driver):
        driver.find_element(*Locators.LOG_IN_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_FORM))

        driver.find_element(*Locators.RECOVER_PASSWORD).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LINK_TEXT_LOGIN_IN_RCVRY))
        driver.find_element(*Locators.LINK_TEXT_LOGIN_IN_RCVRY).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_FORM))

        driver.find_element(*Locators.EMAIL_FIELD_LOG).send_keys(Constants.EMAIL_USER)
        driver.find_element(*Locators.PASSWORD_FIELD_LOG).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.NAME_IN_ACCOUNT))
        value = driver.find_element(*Locators.NAME_IN_ACCOUNT).get_attribute('value')
        assert Constants.NAME_USER in value
