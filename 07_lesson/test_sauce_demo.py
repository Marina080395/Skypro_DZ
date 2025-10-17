import unittest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage


class TestSauceDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")

    def tearDown(self):
        self.driver.quit()

    def test_complete_order(self):
        """Полный цикл покупки товаров."""
        # Добавляем товары в корзину
        self.products_page.add_to_cart("backpack", "tshirt", "onesie")
        self.products_page.go_to_cart()

        # Переходим к оформлению заказа
        self.cart_page.checkout()

        # Заполняем данные покупателя
        self.checkout_page.fill_out("Марина", "Нагиева", "12345")

        # Подтверждаем заказ
        self.checkout_page.confirm_order()

        # Проверяем итоговую сумму
        total_price = self.checkout_page.get_total_price()
        self.assertAlmostEqual(total_price, 58.29, places=2)


if __name__ == "__main__":
    unittest.main()
