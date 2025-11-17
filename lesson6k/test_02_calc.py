import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def chrome_driver():
    service = Service(executable_path=r"C:\path\to\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_calculate_with_delay(chrome_driver):
    driver = chrome_driver
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Настройка задержки
    delay_field = driver.find_element(By.ID, "delay")
    delay_field.clear()
    delay_field.send_keys("45")

    # Кнопки калькулятора
    driver.find_element(By.XPATH, '//button[@data-value="7"]').click()
    driver.find_element(By.XPATH, '//button[@data-value="+"]').click()
    driver.find_element(By.XPATH, '//button[@data-value="8"]').click()
    driver.find_element(By.XPATH, '//button[@data-value="="]').click()


    # Ожидание вывода результата
    wait = WebDriverWait(driver, 50)
    result_field = wait.until(EC.visibility_of_element_located((By.ID, "result")))

    # Проверка правильного результата
    assert result_field.text.strip() == "15", "Сумма должна быть равной 15."
