from selenium.webdriver.common.by import By
from base.base_page import BasePage


class Glossary(BasePage):
    def get_heading_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Glossary"]'))

    