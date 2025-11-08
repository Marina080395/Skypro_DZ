from selenium import webdriver
from form_page import FormPage


def test_01_form():
    driver = webdriver.Chrome()
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form(
        'Марина', 'Нагиева', 'Лермонтова, 55-3',
        'test@skypro.com', '+79100879675',
        'Чёрмоз', 'Россия', 'QA',
        'SkyPro')
    form_page.submit_form()
    form_page.color_check_red()
    form_page.color_check_green()
    driver.quit()
