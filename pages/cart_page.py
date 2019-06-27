from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_ITEMS_BLOCK), "Корзина не пустая"

    def should_be_text_about_empty(self):
        text_empty = self.browser.find_element(*CartPageLocators.BASKET_EMPTY_TEXT)
        assert text_empty.text == "Your basket is empty. Continue shopping", "Your basket is not empty."
