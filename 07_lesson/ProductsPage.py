from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt_add_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_add_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, *items):
        """Добавить указанные товары в корзину."""
        elements = {
            "backpack": self.backpack_add_button,
            "tshirt": self.tshirt_add_button,
            "onesie": self.onesie_add_button
        }
        for item in items:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(elements[item])
            )
            element.click()

    def go_to_cart(self):
        """Перейти в корзину."""
        cart = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_link)
        )
        cart.click()
