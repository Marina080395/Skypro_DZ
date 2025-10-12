from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Firefox
driver = webdriver.Firefox()

try:
    # Переходим на указанную страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим элемент input и вводим текст 'Sky'
    text_field = driver.find_element(By.TAG_NAME, "input")
    text_field.send_keys('Sky')

    # Очищаем поле
    text_field.clear()

    # Вводим новый текст 'Pro'
    text_field.send_keys('Pro')
finally:
    # Закрываем браузер
    driver.quit()
