import unittest
from selenium import webdriver
from pages.SlowCalculatorPage import SlowCalculatorPage


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.calculator = SlowCalculatorPage(self.driver)
        self.calculator.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def tearDown(self):
        self.driver.quit()

    def test_calculation_with_delay(self):
        """Проверить вычисление выражения 7 + 8 с задержкой 45 секунд."""
        self.calculator.set_delay(45)
        self.calculator.press_seven()
        self.calculator.press_plus()
        self.calculator.press_eight()
        self.calculator.press_equal()
        self.calculator.wait_for_result()
        result = self.calculator.get_result()
        self.assertEqual(result, "15")


if __name__ == "__main__":
    unittest.main()
