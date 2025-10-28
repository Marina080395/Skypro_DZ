from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.checkout_button = (By.ID, "checkout")

    def checkout(self):
        def checkout(self):
        """Перейти к оформлению заказа."""
        checkout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        )
