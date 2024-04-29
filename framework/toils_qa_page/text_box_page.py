from selenium.webdriver.common.by import By

from base_page import BasePage


class TextBox(BasePage):

    def text_box_label(self):
        return self.find_element((By.XPATH, '//h1[@class="text-center" and text()="Text Box"]'))

    def user_name_input(self):
        return self.find_element((By.XPATH, '//input[@id="userName"]'))

    def user_email_input(self):
        return self.find_element((By.XPATH, '//input[@id="userEmail"]'))

    def current_address_input(self):
        return self.find_element((By.XPATH, '//textarea[@id="currentAddress"]'))

    def permanent_address_input(self):
        return self.find_element((By.XPATH, '//textarea[@id="permanentAddress"]'))

    def submit_button(self):
        return self.find_element((By.XPATH, '//button[@id="submit"]'))

    def output_field(self):
        return self.find_elements((By.XPATH, '//div[@id="output"]//descendant::p'))
