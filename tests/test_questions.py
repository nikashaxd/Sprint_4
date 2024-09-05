import pytest
import allure
from pages.Questions_page import QuestionsPage
from locators.questions_locators import QuestionsLocators


@pytest.mark.parametrize("question_locator, answer_locator", [
    (QuestionsLocators.QUESTION_TITLE_0, QuestionsLocators.QUESTION_TEXT_0),
    (QuestionsLocators.QUESTION_TITLE_1, QuestionsLocators.QUESTION_TEXT_1),
    (QuestionsLocators.QUESTION_TITLE_2, QuestionsLocators.QUESTION_TEXT_2),
    (QuestionsLocators.QUESTION_TITLE_3, QuestionsLocators.QUESTION_TEXT_3),
    (QuestionsLocators.QUESTION_TITLE_4, QuestionsLocators.QUESTION_TEXT_4),
    (QuestionsLocators.QUESTION_TITLE_5, QuestionsLocators.QUESTION_TEXT_5),
    (QuestionsLocators.QUESTION_TITLE_6, QuestionsLocators.QUESTION_TEXT_6),
    (QuestionsLocators.QUESTION_TITLE_7, QuestionsLocators.QUESTION_TEXT_7)
])
@allure.title("Проверка вопроса и ответа в разделе 'Вопросы о важном'")
@allure.description("Тест проверяет раскрытие ответа на каждый вопрос в разделе 'Вопросы о важном'")
def test_question_answer(driver, question_locator, answer_locator):
    url = "https://qa-scooter.praktikum-services.ru/"
    driver.get(url)

    questions_page = QuestionsPage(driver, url)

    with allure.step(f"Открываем страницу {url} и скроллим до блока с вопросами"):
        questions_page.open()

    with allure.step(f"Кликаем на вопрос {question_locator}"):
        questions_page.click_question(question_locator)

    with allure.step(f"Проверяем, что ответ на вопрос {question_locator} виден"):
        assert questions_page.is_answer_visible(answer_locator), f"Ответ на вопрос {question_locator} не отображается"
