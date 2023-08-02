from selenium.webdriver.common.by import By
from base_page import BasePage


class Careers(BasePage):
    def join_stenn_heading_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Join Stenn"]'))
   