from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ContactUs(BasePage):

    def get_heading_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Contact Us"]'))

    def accept_all_pop_up_button(self):
        return self.find_element((By.XPATH, '//*[text()="Accept all"]'))
