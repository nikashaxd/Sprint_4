import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators


@pytest.mark.usefixtures("driver")
class TestLogoRedirects:

    @allure.title("Проверка редиректа по клику на логотип Самоката")
    @allure.description("Тест проверяет, что при клике на логотип 'Самоката', происходит редирект на главную страницу")
    def test_scooter_logo_redirects_to_homepage(self, driver):
        url = "https://qa-scooter.praktikum-services.ru/"
        driver.get(url)
        scooter_logo = driver.find_element(*MainPageLocators.SCOOTER_LOGO)
        scooter_logo.click()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", ("Логотип 'Самокат' не "
                                                                                   "перенаправляет на главную страницу")

    @allure.title("Проверка редиректа по клику на логотип Яндекса")
    @allure.description("Тест проверяет, что при клике на логотип 'Яндекса' открывается страница Дзена")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        url = "https://qa-scooter.praktikum-services.ru/"
        driver.get(url)
        yandex_logo = driver.find_element(*MainPageLocators.YANDEX_LOGO)
        yandex_logo.click()
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url, "Логотип 'Яндекс' не перенаправляет на главную страницу Дзена"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
