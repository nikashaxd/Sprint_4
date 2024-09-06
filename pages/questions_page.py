from selenium.common import ElementClickInterceptedException
from pages.base_page import BasePage
from locators.questions_locators import QuestionsLocators
import allure


class QuestionsPage(BasePage):
    locators = QuestionsLocators

    @allure.step("Кликаем на вопрос")
    def click_question(self, question_locator):
        question_element = self.element_is_visible(question_locator)
        self.go_to_element(question_element)
        try:
            question_element.click()
        except ElementClickInterceptedException:
            self.execute_script("arguments[0].click();", question_element)

    @allure.step("Проверяем, что текст ответа виден")
    def is_answer_visible(self, answer_locator):
        answer_element = self.element_is_visible(answer_locator)
        return answer_element.is_displayed()

    @allure.step("Получаем текст ответа")
    def get_answer_text(self, answer_locator):
        answer_element = self.element_is_visible(answer_locator)
        return answer_element.text
