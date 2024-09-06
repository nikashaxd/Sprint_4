import pytest
import allure
from pages.questions_page import QuestionsPage
from locators.questions_locators import QuestionsLocators


@allure.feature("Тесты вопросов и ответов")
class TestQuestions:
    @pytest.mark.parametrize("question_locator, answer_locator, expected_text", [
        (QuestionsLocators.QUESTION_TITLE_0, QuestionsLocators.QUESTION_TEXT_0, "Сутки — 400 рублей. Оплата курьеру — "
                                                                                "наличными или картой."),
        (QuestionsLocators.QUESTION_TITLE_1, QuestionsLocators.QUESTION_TEXT_1, "Пока что у нас так: один заказ — "
                                                                                "один самокат. Если хотите покататься"
                                                                                " с друзьями, можете просто сделать "
                                                                                "несколько заказов — один за другим."),
        (QuestionsLocators.QUESTION_TITLE_2, QuestionsLocators.QUESTION_TEXT_2, "Допустим, вы оформляете заказ на 8 "
                                                                                "мая. Мы привозим самокат 8 мая в "
                                                                                "течение дня. Отсчёт времени аренды "
                                                                                "начинается с момента, "
                                                                                "когда вы оплатите заказ курьеру. "
                                                                                "Если мы привезли самокат 8 мая в "
                                                                                "20:30, суточная аренда закончится 9 "
                                                                                "мая в 20:30."),
        (QuestionsLocators.QUESTION_TITLE_3, QuestionsLocators.QUESTION_TEXT_3, "Только начиная с завтрашнего дня. Но "
                                                                                "скоро станем расторопнее."),
        (QuestionsLocators.QUESTION_TITLE_4, QuestionsLocators.QUESTION_TEXT_4, "Пока что нет! Но если что-то срочное "
                                                                                "— всегда можно позвонить в поддержку"
                                                                                " по красивому номеру 1010."),
        (QuestionsLocators.QUESTION_TITLE_5, QuestionsLocators.QUESTION_TEXT_5, "Самокат приезжает к вам с полной "
                                                                                "зарядкой. Этого хватает на восемь "
                                                                                "суток — даже если будете кататься "
                                                                                "без передышек и во сне. Зарядка не "
                                                                                "понадобится."),
        (QuestionsLocators.QUESTION_TITLE_6, QuestionsLocators.QUESTION_TEXT_6, "Да, пока самокат не привезли. Штрафа "
                                                                                "не будет, объяснительной записки "
                                                                                "тоже не попросим. Все же свои."),
        (QuestionsLocators.QUESTION_TITLE_7, QuestionsLocators.QUESTION_TEXT_7, "Да, обязательно. Всем самокатов! И "
                                                                                "Москве, и Московской области."),

    ])
    @allure.title("Проверка текста ответа на вопросы")
    @allure.description("Тест проверяет текст ответа на каждый вопрос в разделе 'Вопросы о важном'")
    def test_question_answer(self, driver, question_locator, answer_locator, expected_text):
        url = "https://qa-scooter.praktikum-services.ru/"
        driver.get(url)

        questions_page = QuestionsPage(driver, url)

        questions_page.click_question(question_locator)

        assert questions_page.is_answer_visible(
            answer_locator), f"Ответ на вопрос {question_locator} не отображается"

        actual_text = questions_page.get_answer_text(answer_locator)
        assert actual_text == expected_text, (f"Текст ответа не соответствует. Ожидалось: '{expected_text}', а "
                                              f"получено: '{actual_text}'")
