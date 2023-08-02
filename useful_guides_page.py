from selenium.webdriver.common.by import By
from base_page import BasePage


class UsefulGuides(BasePage):
    def useful_guides_heading(self):
        return self.find_element((By.XPATH, '//p[text()="Useful Guides"]'))
   