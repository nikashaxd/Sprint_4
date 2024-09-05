import pytest
import allure
from pages.Order_page import OrderPageForWho, OrderPageRent
from locators.main_page_locators import MainPageLocators


@pytest.mark.parametrize("name, surname, address, metro_station, phone, rent_date, rent_period, scooter_color, comment",
                         [
                             (
                             "Анна", "Смирнова", "Москва, Тверская, 5", "Арбатская", "+79991112233", "20", "трое суток",
                             "grey", "Позвоните за час")
                         ])
@allure.title("Тест заказа через верхнюю кнопку 'Заказать'")
@allure.description("Тест проверяет заполнение полей и успешное оформление заказа")
def test_order_scooter_top_button(driver, name, surname, address, metro_station, phone, rent_date, rent_period,
                                  scooter_color, comment):
    url = "https://qa-scooter.praktikum-services.ru/"
    driver.get(url)

    order_page_for_who = OrderPageForWho(driver, url)
    order_page_rent = OrderPageRent(driver, url)
    order_page_for_who.element_is_visible(MainPageLocators.ORDER_BUTTON_TOP).click()
    # Заполнение формы "Для кого самокат"
    order_page_for_who.fill_name(name)
    order_page_for_who.fill_surname(surname)
    order_page_for_who.fill_address(address)
    order_page_for_who.select_metro_station(metro_station)
    order_page_for_who.fill_phone(phone)

    order_page_for_who.click_next_button()
    # Заполнение формы "Про Аренду"
    order_page_rent.select_rent_date(rent_date)
    order_page_rent.select_rent_period(rent_period)
    order_page_rent.select_scooter_color(scooter_color)
    order_page_rent.fill_comment(comment)
    order_page_rent.click_order_button()
    order_page_rent.confirm_order()
    assert order_page_rent.check_order_confirmation(), "Заказ не был оформлен"


@pytest.mark.parametrize("name, surname, address, metro_station, phone, rent_date, rent_period, scooter_color, comment",
                         [
                             ("Иван", "Иванов", "Москва, Ленина, 10", "Сокол", "+79991234567", "15", "двое суток",
                              "black", "Оставьте у двери")
                         ])
@allure.title("Тест заказа через нижнюю кнопку 'Заказать'")
@allure.description("Тест проверяет заполнение полей и успешное оформление заказа")
def test_order_scooter_bottom_button(driver, name, surname, address, metro_station, phone, rent_date, rent_period,
                                     scooter_color, comment):
    url = "https://qa-scooter.praktikum-services.ru/"
    driver.get(url)

    order_page_for_who = OrderPageForWho(driver, url)
    order_page_rent = OrderPageRent(driver, url)
    bottom_order_button = order_page_for_who.element_is_visible(MainPageLocators.ORDER_BUTTON_BOTTOM)
    order_page_for_who.go_to_element(bottom_order_button)

    driver.execute_script("arguments[0].click();", bottom_order_button)

    # Заполнение формы "Для кого самокат"
    order_page_for_who.fill_name(name)
    order_page_for_who.fill_surname(surname)
    order_page_for_who.fill_address(address)
    order_page_for_who.select_metro_station(metro_station)
    order_page_for_who.fill_phone(phone)
    order_page_for_who.click_next_button()

    # Заполнение формы "Про Аренду"
    order_page_rent.select_rent_date(rent_date)
    order_page_rent.select_rent_period(rent_period)
    order_page_rent.select_scooter_color(scooter_color)
    order_page_rent.fill_comment(comment)
    order_page_rent.click_order_button()
    order_page_rent.confirm_order()

    assert order_page_rent.check_order_confirmation(), "Заказ не был оформлен"
