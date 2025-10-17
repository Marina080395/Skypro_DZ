from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.total_amount = (By.CLASS_NAME, "summary_total_label")

    def fill_out(self, first_name, last_name, postal_code):
        """Заполнить форму доставки."""
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.postal_code_field).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def confirm_order(self):
        """Подтвердить заказ."""
        self.driver.find_element(*self.finish_button).click()

    def get_total_price(self):
        """Получить итоговую сумму заказа."""
        price_element = self.driver.find_element(*self.total_amount)
        return float(price_element.text.split("$")[1].strip())
