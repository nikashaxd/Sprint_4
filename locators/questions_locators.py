from selenium.webdriver.common.by import By

class QuestionsLocators:
    QUESTION_TITLES = (By.CSS_SELECTOR, 'div[class= "accordion__button"]') # Локатор для всех вопросов
    QUESTION_TEXT = (By.CSS_SELECTOR, 'div[class= "accordion__panel"]')   # Локатор для текста после раскрытия вопроса
    # Локаторы для каждого вопроса
    QUESTION_TITLE_0 = (By.CSS_SELECTOR, 'div[id="accordion__heading-0"]')
    QUESTION_TITLE_1 = (By.CSS_SELECTOR, 'div[id="accordion__heading-1"]')
    QUESTION_TITLE_2 = (By.CSS_SELECTOR, 'div[id="accordion__heading-2"]')
    QUESTION_TITLE_3 = (By.CSS_SELECTOR, 'div[id="accordion__heading-3"]')
    QUESTION_TITLE_4 = (By.CSS_SELECTOR, 'div[id="accordion__heading-4"]')
    QUESTION_TITLE_5 = (By.CSS_SELECTOR, 'div[id="accordion__heading-5"]')
    QUESTION_TITLE_6 = (By.CSS_SELECTOR, 'div[id="accordion__heading-6"]')
    QUESTION_TITLE_7 = (By.CSS_SELECTOR, 'div[id="accordion__heading-7"]')
    # Локаторы для каждого ответа
    QUESTION_TEXT_0 = (By.CSS_SELECTOR, 'div[id="accordion__panel-0"]')
    QUESTION_TEXT_1 = (By.CSS_SELECTOR, 'div[id="accordion__panel-1"]')
    QUESTION_TEXT_2 = (By.CSS_SELECTOR, 'div[id="accordion__panel-2"]')
    QUESTION_TEXT_3 = (By.CSS_SELECTOR, 'div[id="accordion__panel-3"]')
    QUESTION_TEXT_4 = (By.CSS_SELECTOR, 'div[id="accordion__panel-4"]')
    QUESTION_TEXT_5 = (By.CSS_SELECTOR, 'div[id="accordion__panel-5"]')
    QUESTION_TEXT_6 = (By.CSS_SELECTOR, 'div[id="accordion__panel-6"]')
    QUESTION_TEXT_7 = (By.CSS_SELECTOR, 'div[id="accordion__panel-7"]')

