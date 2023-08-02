from selenium.webdriver.common.by import By
from base_page import BasePage


class QuestionsAnswers(BasePage):
    def questions_answers_heading_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Questions & Answers"]'))
   