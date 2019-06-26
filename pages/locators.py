from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators(object):
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FROM_REGISTRATION = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    BUTTON_ADD = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    TEXT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")
    PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")
    REAL_NAME_ITEM = (By.CSS_SELECTOR, ".product_main h1")
    REAL_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
