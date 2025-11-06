from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
          "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def open(self):
        self.driver.get(self.url)

    def setting_the_delay(self):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

    def get_buttons(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def check_result(self):
        result = WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"
                 ), "15")
        )
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result == "15", f"Результат не равен 15, а равен {result}"
        return result
