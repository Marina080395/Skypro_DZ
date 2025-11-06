from selenium.webdriver.common.by import By
import allure


class FormPage:
    def __init__(self, driver):
        """Инициализация страницы формы."""
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    with allure.step("Открыть страницу с формой"):
        def open(self):
            """Открытие браузера."""
            self.driver.get(self.url)

    with allure.step("Заполнение необходимых данных"):
        def fill_form(self, first_name, last_name,
                      address, e_mail, phone,
                      city, country, job_position,
                      company):
            """Заполнение необходимых данных."""
            self.driver.find_element(
                By.CSS_SELECTOR, 'input[name="first-name"]'
            ).send_keys(first_name)
            self.driver.find_element(
                By.CSS_SELECTOR, 'input[name="last-name"]'
            ).send_keys(last_name)
            self.driver.find_element(
                By.CSS_SELECTOR, 'input[name="address"]'
            ).send_keys(address)
            self.driver.find_element(
                By.CSS_SELECTOR, 'input[name="e-mail"]'
            ).send_keys(e_mail)
            self.driver.find_element(
                By.CSS_SELECTOR, 'input[name="phone"]'
            ).send_keys(phone)
            self.driver.find_element(
                By.CSS_SELECTOR, 'input[name="city"]'
            ).send_keys(city)
            self.driver.find_element(
                By.CSS_SELECTOR, 'input[name="country"]'
            ).send_keys(country)
            self.driver.find_element(
                By.CSS_SELECTOR, 'input[name="job-position"]'
            ).send_keys(job_position)
            self.driver.find_element(
                By.CSS_SELECTOR, 'input[name="company"]'
            ).send_keys(company)

    with allure.step("Нажатие кнопки 'Submit'"):
        def submit_form(self):
            self.driver.find_element(
                By.CSS_SELECTOR, "button[type='submit']"
            ).click()

    with allure.step("Функция на поверку, что все поля заполнены"):
        def color_check_red(self):
            assert "alert py-2 alert-danger" in self.driver.find_element(
               By.CSS_SELECTOR, "#zip-code"
            ).get_attribute("class")

        def color_check_green(self):
            assert "alert py-2 alert-success" in self.driver.find_element(
                By.CSS_SELECTOR, "#first-name"
            ).get_attribute("class")
            assert "alert py-2 alert-success" in self.driver.find_element(
                By.CSS_SELECTOR, "#last-name"
            ).get_attribute("class")
            assert "alert py-2 alert-success" in self.driver.find_element(
                By.CSS_SELECTOR, "#address"
            ).get_attribute("class")
            assert "alert py-2 alert-success" in self.driver.find_element(
                By.CSS_SELECTOR, "#city"
            ).get_attribute("class")
            assert "alert py-2 alert-success" in self.driver.find_element(
                By.CSS_SELECTOR, "#country"
            ).get_attribute("class")
            assert "alert py-2 alert-success" in self.driver.find_element(
                By.CSS_SELECTOR, "#e-mail"
            ).get_attribute("class")
            assert "alert py-2 alert-success" in self.driver.find_element(
                By.CSS_SELECTOR, "#phone"
            ).get_attribute("class")
            assert "alert py-2 alert-success" in self.driver.find_element(
                By.CSS_SELECTOR, "#job-position"
            ).get_attribute("class")
            assert "alert py-2 alert-success" in self.driver.find_element(
                By.CSS_SELECTOR, "#company"
            ).get_attribute("class")
