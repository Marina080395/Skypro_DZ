from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ShopPage:
    """Класс для работы онлайн корзины."""

    @allure.feature("Тестирование интернет-магазина")
    @allure.title("Полный цикл покупки товара")
    @allure.description("Тест проверяет корректность работы "
                        "и отображения информации в корзине")
    @allure.feature("Result Shop")
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    with allure.step("Открыть страницу с формой"):
        def open(self):
            self.driver.get(self.url)

    with allure.step("Авторизация пользователя"):
        def authorization(self):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR, "#user-name"))
            ).send_keys("standard_user")

            self.driver.find_element(
                By.CSS_SELECTOR, "#password"
            ).send_keys("secret_sauce")
            self.driver.find_element(
                By.CSS_SELECTOR, "#login-button").click()

    with allure.step("Добавить в корзину"):
        def add_to_cart(self):
            items = [
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Onesie",
            ]
            for item in items:
                WebDriverWait(self.driver, 10).until(
                   EC.element_to_be_clickable(
                       (By.XPATH,
                           f"//div[text()='{item}']/ancestor:"
                           f":div[@class='inventory_item']//button",))
                ).click()
    with allure.step("В корзине"):
        def in_cart(self):
            self.driver.find_element(
                By.CSS_SELECTOR, ".shopping_cart_link"
            ).click()

    with allure.step("Начать оформление заказа"):
        def click_checkout(self):
            self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    with allure.step("Заполнение данных для доставки"):
        """Заполнение данных для доставки."""
    def fill_form(self, first_name, last_name, postal_code):
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name"
        ).send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name"
        ).send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code"
        ).send_keys(postal_code)
        self.driver.find_element(
            By.CSS_SELECTOR, "#continue"
        ).click()

    with allure.step("Функция для проверки итоговой суммы "):
        """ Функция для вывода итоговой стоимости покупок """
    def checking_total_amount(self):
        total = (
            WebDriverWait(self.driver, 10)
            .until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".summary_total_label")
                )
            )
            .text
        )
        assert total == "Total: $58.29", (
            f"Итоговая сумма не равна $58.29. " f"Фактическая сумма: {total}"
        )
