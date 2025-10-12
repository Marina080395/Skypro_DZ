from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Google Chrome
driver = webdriver.Chrome()

try:
    # Переходим на указанную страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Кликаем на синюю кнопку по её цвету и типу кнопки
    button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    button.click()
finally:
    # Закрываем браузер
    driver.quit()
