from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


class Test:
    # Проверяем переход к разделу "Булки" в Конструкторе
    def test_to_buns_section(self, login):
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.SAUCES)).click()
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.BUNS)).click()
        assert WebDriverWait(login, 3).until(EC.text_to_be_present_in_element_attribute(Locators.BUNS,
                                                                                         'class',
                                                                                         Constants.VALUE))

    # Проверяем переход к разделу "Соусы" в Конструкторе
    def test_to_sauces_section(self, login):
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.SAUCES)).click()
        assert WebDriverWait(login, 3).until(EC.text_to_be_present_in_element_attribute(Locators.SAUCES,
                                                                                         'class',
                                                                                         Constants.VALUE))

    # Проверяем переход к разделу "Начинки" в Конструкторе
    def test_to_fillings_section(self, login):
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.FILLINGS)).click()
        assert WebDriverWait(login, 3).until(EC.text_to_be_present_in_element_attribute(Locators.FILLINGS,
                                                                                        'class',
                                                                                         Constants.VALUE))
