import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def edge_driver():
    service = Service(executable_path=r"C:\path\to\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()

def test_fill_and_submit(edge_driver):
    driver = edge_driver
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение полей
    first_name = driver.find_element(By.NAME, "firstName")
    first_name.send_keys("Иван")
    last_name = driver.find_element(By.NAME, "lastName")
    last_name.send_keys("Петров")
    address = driver.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")
    email = driver.find_element(By.NAME, "email")
    email.send_keys("test@skypro.com")
    phone_number = driver.find_element(By.NAME, "phoneNumber")
    phone_number.send_keys("+7985899998787")
    zip_code = driver.find_element(By.NAME, "zipCode")
    zip_code.clear()  # Оставляем пустым
    city = driver.find_element(By.NAME, "city")
    city.send_keys("Москва")
    country = driver.find_element(By.NAME, "country")
    country.send_keys("Россия")
    job_position = driver.find_element(By.NAME, "jobPosition")
    job_position.send_keys("QA")
    company = driver.find_element(By.NAME, "company")
    company.send_keys("SkyPro")

    # Подтверждение формы
    submit_btn = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit_btn.click()

    # Проверка ошибок и правильных значений полей
    wait = WebDriverWait(driver, 10)
    error_zipcode = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.ng-invalid")))
    valid_inputs = driver.find_elements(By.CSS_SELECTOR, "input.ng-valid")

    # Asserts
    assert len(valid_inputs) >= 8, "Количество валидных полей меньше ожидаемого."
    assert error_zipcode.is_displayed(), "Ошибка в ZIP-коде не отображается."
