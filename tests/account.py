from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


class Test:
    # Проверяем переход по клику на «Личный кабинет»
    def test_click_account(self, login):
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.ACCOUNT_BUTTON)).click()
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.SAVE_BUTTON))
        assert login.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    # Проверяем переход из личного кабинета в конструктор
    def test_click_constructor(self, login):
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.ACCOUNT_BUTTON)).click()
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.SAVE_BUTTON))
        login.find_element(*Locators.CONSTRUCTOR).click()
        assert WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.SECTION_OF_BURGERS))

    # Проверяем переход из личного кабинета на логотип Stellar Burgers
    def test_click_logo(self, login):
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.ACCOUNT_BUTTON)).click()
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.SAVE_BUTTON))
        login.find_element(*Locators.LOGO).click()
        assert login.current_url == Constants.URL

    # Проверяем выход из личного кабинета
    def test_log_out(self, login):
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.ACCOUNT_BUTTON)).click()
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.LOG_OUT)).click()
        assert WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.LOGIN_FORM))
