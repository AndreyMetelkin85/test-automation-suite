from selenium.webdriver.common.by import By
from base_page import BasePage


class FactoringWorks(BasePage):
    def get_heading_label(self):
        return self.find_element((By.XPATH, '//p[contains(., "Everything You Need")]'))
   