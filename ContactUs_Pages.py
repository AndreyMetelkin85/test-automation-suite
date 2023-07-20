from selenium.webdriver.common.by import By
from BaseApp import BasePage, Button, Text


class ContactUs(BasePage):

    def heading_contact_us_label(self) -> Text:
        return self.find_element((By.XPATH, '//div[text()="Contact Us"]'))

    def accept_all_pop_up_button(self) -> Button:
        return self.find_element((By.XPATH, '//*[text()="Accept All"]'))
