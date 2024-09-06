from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step("Открываем страницу")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Элемент {locator} становится видимым")
    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Все элементы {locator} становятся видимыми")
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Элемент {locator} присутствует на странице")
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Элемент {locator} становится кликабельным")
    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Скроллим к элементу {element}")
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Используем JavaScript для принудительного клика {element}")
    def execute_script(self, script, element=None):
        self.driver.execute_script(script, element)
