from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step("Кликаем по логотипу 'Самокат'")
    def click_scooter_logo(self):
        scooter_logo = self.element_is_visible(MainPageLocators.SCOOTER_LOGO)
        scooter_logo.click()

    @allure.step("Кликаем по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        yandex_logo = self.element_is_visible(MainPageLocators.YANDEX_LOGO)
        yandex_logo.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains("dzen.ru"))
