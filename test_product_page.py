from .pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()  # открыли страницу
    page.add_cart_to_pocket()  # добавили товар в корзину и решили уравнение
    page.should_be_message_about_add()  # проверили наименование товара
    page.should_be_message_about_price()  # проверели цену товара
