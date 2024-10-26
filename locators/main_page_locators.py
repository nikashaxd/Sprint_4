from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, '//button[text()="Заказать"][@class="Button_Button__ra12g"]')  # Верхняя кнопка "Заказать"
    ORDER_BUTTON_BOTTOM = (By.XPATH, '//button[contains(@class, "Button_Middle__1CSJM")]')  # Нижняя кнопка "Заказать"
    YANDEX_LOGO = (By.CSS_SELECTOR, 'a[class = "Header_LogoYandex__3TSOI"]')
    SCOOTER_LOGO = (By.CSS_SELECTOR, 'a[class = Header_LogoScooter__3lsAR]')

