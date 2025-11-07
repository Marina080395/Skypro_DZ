from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage
import allure


@allure.feature("Тестирование формы заполнения")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка заполнения и валидации формы")
@allure.description("""
Этот тест проверяет:
1. Открытие и заполнение формы
2. Отправку данных
3. Валидацию обязательных полей
4. Проверку подсветки полей
""")
def test_01_form():
    @allure.step("Инициализация драйвера и страницы"):
    driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
    form_page = FormPage(driver)

    @allure.step("Открытие страницы с формой"):
    form_page.open()

    @allure.step("Заполнение формы данными"):
    form_page.fill_form(
        'Марина', 'Нагиева', 'Лермонтова, 55-3',
        'test@skypro.com', '+79100879675',
        'Чёрмоз', 'Россия', 'QA',
        'SkyPro')

    @allure.step("Нажатие кнопки 'Submit'"):
    form_page.submit_form()

    @allure.step("Проверка подсветки обязательных полей"):
    form_page.color_check_red()
    form_page.color_check_green()

    @allure.step("Закрытие браузера"):
    driver.quit()
