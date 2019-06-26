from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_cart_to_pocket(self):
        btn_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        btn_add.click()
        self.solve_quiz_and_get_code()

    def should_be_message_about_add(self):
        name = self.browser.find_element(*ProductPageLocators.TEXT_PRODUCT_NAME)  # берем уведомление о добавлении
        real_name = self.browser.find_element(*ProductPageLocators.REAL_NAME_ITEM)  # берем имя товара
        index = name.text.find(real_name.text)  # ищем совпадения
        assert index != -1, "Wrong item"  # проверяем

    def should_be_message_about_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        real_price = self.browser.find_element(*ProductPageLocators.REAL_PRICE)
        assert price.text == real_price.text, "Wrong price"
