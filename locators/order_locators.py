from selenium.webdriver.common.by import By


class OrderForWhoFieldsLocators:
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_FIELD = (By.XPATH, '//input[@placeholder = "* Станция метро"]')
    METRO_FIELD_SELECTED = (By.CSS_SELECTOR, 'div[class = "select-search__select"')  #Выпадающее поле со станциями метро
    METRO_STATIONS_LIST = (By.CSS_SELECTOR, 'div[class = "Order_Text__2broi"]')  #Лист станций метро
    TELEPHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')


class OrderRentFieldsLocators:
    WHEN_TO_RENT_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    CALENDER_WINDOW = (By.CSS_SELECTOR,
                       'div[class = "react-datepicker__month-container"')  #Окно выпадающего календаря, в котором нужно выбрать дату кликом
    CALENDER_DATE = (By.CSS_SELECTOR, 'div[class = "react-datepicker__week"]')  #Выбор даты в календаре
    RENTAL_PERIOD_INPUT = (By.XPATH, '//div[text()="* Срок аренды"]')
    RENT_OPTION = (By.CSS_SELECTOR, 'div[class = "Dropdown-option"')  #Выпадающее окно с выбором суток
    COLOR_CHECKBOX = (By.CSS_SELECTOR, 'div[class = "Order_Checkboxes__3lWSI"')
    BLACK_CHECKBOX = (By.CSS_SELECTOR, 'input[id = "black"]')
    GREY_CHECKBOX = (By.CSS_SELECTOR, 'input[id = "grey"]')
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')

    ORDER_BUTTON = (
    By.XPATH, '//button[contains(@class, "Button_Button__ra12g Button_Middle__1CSJM") and text()="Заказать"]')

    YES_BUTTON = (By.XPATH, '//button[text()="Да"]')
    ORDER_CONFIRMATION_WINDOW = (By.XPATH, '//div[text()="Хотите оформить заказ?"]')
    ORDER_IS_CREATED_WINDOW = (By.XPATH, '//div[text()="Заказ оформлен"]')
