from selenium.webdriver.common.by import By
from base_page import BasePage


class Glossary(BasePage):
    def glossary_heading(self):
        return self.find_element((By.XPATH, '//p[text()="Glossary"]'))

    