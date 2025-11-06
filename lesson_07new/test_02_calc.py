from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from calculator_page import CalculatorPage


def test_02_calc():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().
                              install()))
    calculator_page = CalculatorPage(driver)
    calculator_page.open()
    calculator_page.setting_the_delay()
    calculator_page.get_buttons()
    result = calculator_page.check_result()
    assert result == "15", f"Результат не равен 15, а равен {result}"
    driver.quit()
