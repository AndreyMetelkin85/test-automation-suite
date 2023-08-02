from selenium.webdriver.common.by import By
from base_page import BasePage


class Articles(BasePage):
    def articles_heading(self):
        return self.find_element((By.XPATH, '//div[text()="Articles"]'))
