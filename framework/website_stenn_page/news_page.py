from selenium.webdriver.common.by import By
from base_page import BasePage


class News(BasePage):

    def get_heading_label(self):
        return self.find_element((By.XPATH, '//div[text()="Articles"]'))

    def accept_all_pop_up_button(self):
        return self.find_element((By.XPATH, '//*[text()="Accept All"]'))
