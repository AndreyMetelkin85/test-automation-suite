from selenium.webdriver.common.by import By

from base.base_page import BasePage


class PartnerWithUs(BasePage):

    def get_heading_label(self):
        return self.find_element((By.XPATH, '//h2[contains(. , "Your access to our")]'))
