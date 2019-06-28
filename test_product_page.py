import pytest
import time

from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.login
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse="True")
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + "@gmo.com"
        password = "par1234ol"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()  # открыли страницу
        page.add_cart_to_pocket()  # добавили товар в корзину и решили уравнение
        page.should_be_message_about_add()  # проверили наименование товара
        page.should_be_message_about_price()  # проверели цену товара

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.parametrize('links', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_cart(browser, links):
    link = "{}".format(links)
    page = ProductPage(browser, link)
    page.open()  # открыли страницу
    page.add_cart_to_pocket()  # добавили товар в корзину и решили уравнение
    page.should_be_message_about_add()  # проверили наименование товара
    page.should_be_message_about_price()  # проверели цену товара


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = CartPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_text_about_empty()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
