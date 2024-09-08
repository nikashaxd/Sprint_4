from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step("Проверяем, что текущий URL совпадает с ожидаемым")
    def is_current_url_correct(self, expected_url):
        return self.driver.current_url == expected_url

    @allure.step("Кликаем по логотипу 'Самокат'")
    def click_scooter_logo(self):
        scooter_logo = self.element_is_visible(MainPageLocators.SCOOTER_LOGO)
        scooter_logo.click()

    @allure.step("Кликаем по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        yandex_logo = self.element_is_visible(MainPageLocators.YANDEX_LOGO)
        yandex_logo.click()
        self.switch_to_new_window()
        self.wait_for_url_contains("dzen.ru")
