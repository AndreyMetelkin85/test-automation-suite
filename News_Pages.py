from selenium.webdriver.common.by import By
from BaseApp import Button, Text, Label, BasePage


class News(BasePage):

    def heading_articles_label(self) -> Text:
        return self.find_element((By.XPATH, '//div[text()="Articles"]'))

    def accept_all_pop_up_button(self) -> Button:
        return self.find_element((By.XPATH, '//*[text()="Accept All"]'))
