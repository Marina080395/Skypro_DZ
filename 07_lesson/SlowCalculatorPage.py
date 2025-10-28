from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.seven_button = (By.XPATH, "//span[text()='7']")
        self.plus_button = (By.XPATH, "//span[text()='+']")
        self.eight_button = (By.XPATH, "//span[text()='8']")
        self.equal_button = (By.XPATH, "//span[text()='=']")
        self.result_field = (By.CSS_SELECTOR, "div.screen")

    def set_delay(self, seconds):
        """Установка значения задержки."""
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def press_seven(self):
        """Нажать цифру 7."""
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.seven_button)
        )
        button.click()

    def press_plus(self):
        """Нажать знак '+'."""
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.plus_button)
        )
        button.click()

    def press_eight(self):
        """Нажать цифру 8."""
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.eight_button)
        )
        button.click()

    def press_equal(self):
        """Нажать '='."""
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.equal_button)
        )
        button.click()

    def get_result(self):
        """Получить результат вычисления."""
        return self.driver.find_element(*self.result_field).text.strip()

    def wait_for_result(self):
        """Подождать появление результата."""
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(self.result_field, "15"))
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.seven_button = (By.XPATH, "//button[contains(@onclick,'display(\\"7\\")')]")
        self.plus_button = (By.XPATH, "//button[contains(@onclick,'display(\\"+\\")')]")
        self.eight_button = (By.XPATH, "//button[contains(@onclick,'display(\\"8\\")')]")
        self.equal_button = (By.XPATH, "//button[contains(@onclick,'calculate()')]")
        self.result_field = (By.ID, "result")

    def set_delay(self, seconds):
        """Установка значения задержки."""
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def press_seven(self):
        """Нажать цифру 7."""
        self.driver.find_element(*self.seven_button).click()

    def press_plus(self):
        """Нажать знак '+'."""
        self.driver.find_element(*self.plus_button).click()

    def press_eight(self):
        """Нажать цифру 8."""
        self.driver.find_element(*self.eight_button).click()

    def press_equal(self):
        """Нажать '='."""
        self.driver.find_element(*self.equal_button).click()

    def get_result(self):
        """Получить результат вычисления."""
        return self.driver.find_element(*self.result_field).text.strip()

    def wait_for_result(self):
        """Подождать появление результата."""
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element(self.result_field, "15"))
