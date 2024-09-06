import allure
from pages.main_page import MainPage


class TestLogoRedirects:

    @allure.title("Проверка редиректа по клику на логотип Самоката")
    @allure.description("Тест проверяет, что при клике на логотип 'Самоката', происходит редирект на главную страницу")
    def test_scooter_logo_redirects_to_homepage(self, driver):
        url = "https://qa-scooter.praktikum-services.ru/"
        driver.get(url)
        main_page = MainPage(driver, url)
        main_page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", ("Логотип 'Самокат' не "
                                                                                   "перенаправляет на главную страницу")

    @allure.title("Проверка редиректа по клику на логотип Яндекса")
    @allure.description("Тест проверяет, что при клике на логотип 'Яндекса' открывается страница Дзена")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        url = "https://qa-scooter.praktikum-services.ru/"
        driver.get(url)
        main_page = MainPage(driver, url)
        main_page.click_yandex_logo()
        assert "dzen.ru" in driver.current_url, "Логотип 'Яндекс' не перенаправляет на главную страницу Дзена"
