from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Firefox
driver = webdriver.Firefox()

try:
    # Переходим на указанную страницу
    driver.get("http://the-internet.herokuapp.com/login")

    # Заполняем форму авторизации
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")

    # Нажимаем кнопку Login
    login_button = driver.find_element(By.CLASS_NAME, "radius")
    login_button.click()

    # Получаем сообщение с зелёной плашки и выводим его в консоль
    success_message = driver.find_element(By.CLASS_NAME, "flash.success").text
    print(success_message)
finally:
    # Закрываем браузер
    driver.quit()
