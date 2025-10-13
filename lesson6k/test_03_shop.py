import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def firefox_driver():
    service = Service(executable_path=r"C:\path\to\geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()

def test_buy_items(firefox_driver):
    driver = firefox_driver
    driver.get("https://www.saucedemo.com/")

    # Логин
    user_login = driver.find_element(By.ID, "user-name")
    user_password = driver.find_element(By.ID, "password")
    user_login.send_keys("standard_user")
    user_password.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавляем товары в корзину
    items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for item in items:
        add_to_cart_button = driver.find_element(By.XPATH, f"//div[text()='{item}']/parent::*//button")
        add_to_cart_button.click()

    # Перейти в корзину
    shopping_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    shopping_cart.click()

    # Оформляем покупку
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    # Информация покупателя
    first_name = driver.find_element(By.ID, "first-name")
    last_name = driver.find_element(By.ID, "last-name")
    postal_code = driver.find_element(By.ID, "postal-code")
    first_name.send_keys("Марина")
    last_name.send_keys("Нагиева")
    postal_code.send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # Получаем итоговую цену
    final_price = driver.find_element(By.CLASS_NAME, "summary_total_label").text.split()[1]

    # Проверяем итоговую сумму
    assert total_amount == "$58.29", f"Сумма не совпадает: {total_amount}"
