from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_locators import OrderForWhoFieldsLocators, OrderRentFieldsLocators
import allure


class OrderPageForWho(BasePage):
    locators = OrderForWhoFieldsLocators()

    @allure.step("Заполняем поле Имя: {name}")
    def fill_name(self, name):
        self.element_is_visible(self.locators.NAME_INPUT).send_keys(name)

    @allure.step("Заполняем поле Фамилия: {surname}")
    def fill_surname(self, surname):
        self.element_is_visible(self.locators.SURNAME_INPUT).send_keys(surname)

    @allure.step("Заполняем поле Адрес: {address}")
    def fill_address(self, address):
        self.element_is_visible(self.locators.ADDRESS_INPUT).send_keys(address)

    @allure.step("Выбираем станцию метро: {station_name}")
    def select_metro_station(self, station_name):
        metro_input = self.element_is_visible(self.locators.METRO_FIELD)
        metro_input.click()
        self.element_is_visible(self.locators.METRO_FIELD_SELECTED)
        stations = self.elements_are_visible(self.locators.METRO_STATIONS_LIST)
        for station in stations:
            self.go_to_element(station)
            if station.text == station_name:
                station.click()
                break

    @allure.step("Заполняем телефон: {phone_number}")
    def fill_phone(self, phone_number):
        self.element_is_visible(self.locators.TELEPHONE_INPUT).send_keys(phone_number)

    @allure.step("Нажимаем кнопку Далее")
    def click_next_button(self):
        self.element_is_visible(self.locators.NEXT_BUTTON).click()


class OrderPageRent(BasePage):
    locators = OrderRentFieldsLocators()

    @allure.step("Выбираем дату аренды: {date}")
    def select_rent_date(self, date):
        date_input = self.element_is_visible(self.locators.WHEN_TO_RENT_INPUT)
        date_input.click()
        self.element_is_visible(
            (By.XPATH, self.locators.SPECIFIC_DATE_TEMPLATE.format(date=date))
        ).click()

    @allure.step("Выбираем срок аренды: {period}")
    def select_rent_period(self, period):
        period_input = self.element_is_visible(self.locators.RENTAL_PERIOD_INPUT)
        period_input.click()
        rent_periods = self.elements_are_visible(self.locators.RENT_OPTION)
        for rent_period in rent_periods:
            if rent_period.text == period:
                rent_period.click()
                break

    @allure.step("Выбираем цвет самоката: {color}")
    def select_scooter_color(self, color):
        if color.lower() == 'black':
            self.element_is_visible(self.locators.BLACK_CHECKBOX).click()
        elif color.lower() == 'grey':
            self.element_is_visible(self.locators.GREY_CHECKBOX).click()

    @allure.step("Заполняем комментарий: {comment}")
    def fill_comment(self, comment):
        self.element_is_visible(self.locators.COMMENT_INPUT).send_keys(comment)

    @allure.step("Нажимаем кнопку Оформить заказ")
    def click_order_button(self):
        self.element_is_visible(self.locators.ORDER_BUTTON).click()

    @allure.step("Подтверждаем заказ")
    def confirm_order(self):
        self.element_is_visible(self.locators.YES_BUTTON).click()

    @allure.step("Проверяем, что заказ оформлен")
    def check_order_confirmation(self):
        return self.element_is_visible(self.locators.ORDER_IS_CREATED_WINDOW).is_displayed()
