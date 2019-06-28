from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def login_user(self, email, password):
        em = self.browser.find_element(*LoginPageLocators.LOGIN_USERNAME)
        psw = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        btn = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        em.send_keys(email)
        psw.send_keys(password)
        btn.click()

    def register_new_user(self, email, password):
        em = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        psw = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        repeat_pws = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        btn_reg = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        em.send_keys(email)
        psw.send_keys(password)
        repeat_pws.send_keys(password)
        btn_reg.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        index = self.url.find("login")
        assert index != -1, "Url don't have login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Don't have form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.FROM_REGISTRATION), "Don't have form"
