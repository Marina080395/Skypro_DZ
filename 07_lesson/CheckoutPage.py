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
        first_name_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.first_name_field)
        )
        first_name_input.clear()
        first_name_input.send_keys(first_name)
        
        last_name_input = self.driver.find_element(*self.last_name_field)
        last_name_input.clear()
        last_name_input.send_keys(last_name)
        
        postal_code_input = self.driver.find_element(*self.postal_code_field)
        postal_code_input.clear()
        postal_code_input.send_keys(postal_code)
        
        self.driver.find_element(*self.continue_button).click()

    def confirm_order(self):
        """Подтвердить заказ."""
        finish_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_button)
        )
        finish_btn.click()

    def get_total_price(self):
        """Получить итоговую сумму заказа."""
        price_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.total_amount)
        )
        return float(price_element.text.split("$")[1].strip())