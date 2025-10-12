from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Google Chrome
driver = webdriver.Chrome()

try:
    # Переходим на указанную страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Кликаем на синюю кнопку по её классу
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()
finally:
    # Закрываем браузер
    driver.quit()
