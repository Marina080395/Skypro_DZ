from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """Класс для работы со страницей калькулятора."""
    @allure.title("Проверка работы медленного калькулятора")
    @allure.description("Тест проверяет корректность "
                        "вычислений с задержкой")
    def __init__(self, driver):
        """Инициализация страницы калькулятора.

            Args:
                driver: WebDriver экземпляр
        """
        self.driver = driver
        self.url = (
          "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    @allure.step("Открыть страницу калькулятора")
    def open(self):
        """Открывает страницу калькулятора."""
        self.driver.get(self.url)

    @allure.step("Установить задержку вычислений на 45 секунд")
    def setting_the_delay(self):
        """Установить задержку вычислений"""
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

    @allure.step("Выполнить операцию 7 + 8")
    def get_buttons(self):
        """Выполнить вычислительные операции"""
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("Проверить результат вычислений")
    def check_result(self):
        """Проверяет результат вычислений.

                Аргс:
                expected_result: Ожидаемый результат
                время ожидания: Максимальное время ожидания

                Возвращение:
                Фактический результат вычислений

                Повышает:
                AssertionError: Если результат не соответствует ожидаемому
        """
        result = WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"
                 ), "15")
        )
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result == "15", f"Результат не равен 15, а равен {result}"
        return result
