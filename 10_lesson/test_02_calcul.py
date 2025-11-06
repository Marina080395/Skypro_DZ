from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from calculator_page import CalculatorPage
import allure


@allure.feature("Тестирование калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка замедленного тестирование калькулятора")
@allure.description("""
Этот тест проверяет:
1. Открытие и нажатие необходимых клавиш
2. Отправку данных
3. Проверка результатов вычислений
""")
def test_02_calc():
    with allure.step("Инициализация драйвера и открытие страницы"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager(
            ).install()))
    calculator_page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calculator_page.open()

    with allure.step("Установить задержку вычислений на 45 секунд"):
        calculator_page.setting_the_delay()

    with allure.step("Выполнить операцию 7 + 8"):
        calculator_page.get_buttons()

    with allure.step("Проверить результат вычислений"):
        result = calculator_page.check_result()
        assert result == "15", f"Результат не равен 15, а равен {result}"

    with allure.step("Закрытие браузера"):
        driver.quit()
