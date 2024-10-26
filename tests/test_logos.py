import allure
from pages.main_page import MainPage
from urls import Urls


class TestLogoRedirects:

    @allure.title("Проверка редиректа по клику на логотип 'Самокат'")
    @allure.description("Тест проверяет, что при клике на логотип 'Самоката' происходит редирект на главную страницу")
    def test_scooter_logo_redirects_to_homepage(self, driver):
        main_page = MainPage(driver, Urls.HOME_PAGE)
        main_page.open_homepage(Urls.HOME_PAGE)
        main_page.click_scooter_logo()
        assert main_page.is_current_url_correct(Urls.HOME_PAGE), ("Логотип 'Самокат' не перенаправляет на главную "
                                                                  "страницу")

    @allure.title("Проверка редиректа по клику на логотип 'Яндекс'")
    @allure.description("Тест проверяет, что при клике на логотип 'Яндекса' открывается страница Дзена")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver, Urls.HOME_PAGE)
        main_page.open_homepage(Urls.HOME_PAGE)
        main_page.click_yandex_logo()
        main_page.wait_for_url_contains("dzen.ru")
        assert "dzen.ru" in driver.current_url, "Логотип 'Яндекс' не перенаправляет на страницу Дзена"
