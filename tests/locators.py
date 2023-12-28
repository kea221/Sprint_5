from selenium.webdriver.common.by import By


class Locators:
    # LOG_IN_TO_ACCOUNT - кнопка "Войти в аккаунт" на главной странице
    LOG_IN_TO_ACCOUNT = (By.CSS_SELECTOR, ".button_button_size_large__G21Vg")
    # LINK_TEXT_REGISTRATION - текстовая ссылка "Зарегистрироваться" на странице входа
    LINK_TEXT_REGISTRATION = (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/register']")
    # REGISTER - кнопка "Зарегистрироваться" на экране регистрации
    REGISTER = (By.CSS_SELECTOR, "button.button_button__33qZ0")
    # NAME_FIELD_REG - поле ввода Имени в форме регистрации
    NAME_FIELD_REG = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # EMAIL_FIELD_REG - поле ввода Email в форме регистрации
    EMAIL_FIELD_REG = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # PASSWORD_FIELD_REG - поле ввода пароля в форме регистрации
    PASSWORD_FIELD_REG = (By.XPATH, "//input[@type='password']")
    # ERROR_MESSAGE - текст ошибки при вводе некорректного пароля при регистрации
    ERROR_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default']")

    # LOGIN_FORM - форма для входа с полями Email и Пароль
    # LOGIN_FORM = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']")
    LOGIN_FORM = (By.CSS_SELECTOR, ".App_App__aOmNj")
    # EMAIL_FIELD_LOG - поле ввода Email в форме для входа
    EMAIL_FIELD_LOG = (By.XPATH, "//input[@name='name']")
    # PASSWORD_FIELD_LOG - поле ввода Пароля в форме для входа
    PASSWORD_FIELD_LOG = (By.XPATH, "//input[@type='password']")
    # LOG_IN_BUTTON - кнопка "Войти" в форме входа
    LOG_IN_BUTTON = (By.XPATH, "//form[@class]/button")
    # ORDER_BUTTON -кнопка "Оформить заказ"
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.button_button_size_large__G21Vg")

    # ACCOUNT_BUTTON - кнопка "Личный Кабинет"
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    # NAME_IN_ACCOUNT - поле Имя в Личном Кабинете
    NAME_IN_ACCOUNT = (By.XPATH, "//input[@name='Name']")
    # EMAIL_IN_ACCOUNT - поле Email в Личном Кабинете
    EMAIL_IN_ACCOUNT = (By.XPATH, "//input[@name='name']")

    # LINK_TEXT_LOGIN_IN_REG - текстовая ссылка "Войти" на странице регистрации
    LINK_TEXT_LOGIN_IN_REG = (By.XPATH, "//a[@class='Auth_link__1fOlj']")

    # RECOVER_PASSWORD - текстовая ссылка "Восстановить пароль"
    RECOVER_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']")

    # LINK_TEXT_LOGIN_IN_RCVRY - текстовая ссылка "Войти" на странице восстановления пароля
    LINK_TEXT_LOGIN_IN_RCVRY = (By.XPATH, "//p/a[@class='Auth_link__1fOlj']")

    # SAVE_BUTTON - кнопка "Сохранить" в Личном Кабинете
    SAVE_BUTTON = (By.XPATH, "//div[@class='Profile_buttonBox__1JlBI']/button[last()]")

    # CONSTRUCTOR - кнопка "Конструктор"
    CONSTRUCTOR = (By.XPATH, "//nav//li/a[@href='/']")

    # SECTION_OF_BURGERS - секция "Соберите бургер"
    SECTION_OF_BURGERS = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']")

    # LOGO svg[fill='none']
    LOGO = (By.CSS_SELECTOR, "svg[fill='none']")

    # LOG_OUT - кнопка выхода из ЛК
    LOG_OUT = (By.CSS_SELECTOR, "button.text_color_inactive")

    # BUNS - раздел Булки
    BUNS = (By.XPATH, "//div[@style]/div[@class][1]")
    # BUNS_HEADER - заголовок "Булки" в разделе "Булки"
    BUNS_HEADER = (By.XPATH, "//h2[contains(text(),'Булки')]")
    # SAUCES - раздел Соусы "//div[@style]/div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'][1]"
    SAUCES = (By.XPATH, "//div[@style]/div[@class][2]")
    # SAUCES_HEADER - заголовок "Соусы" в разделе "Соусы"
    SAUCES_HEADER = (By.XPATH, "//h2[contains(text(),'Соусы')]")
    # FILLINGS - раздел Начинки
    FILLINGS = (By.XPATH, "//div[@style]/div[@class][3]")
    # FILLINGS_HEADER - заголовок "Начинки" в разделе "Начинки"
    FILLINGS_HEADER = (By.XPATH, "//h2[contains(text(),'Начинки')]")
