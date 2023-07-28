import click
from selenium.webdriver.common.by import By
from BaseApp import BasePage


class HeaderButtons(BasePage):

    def products_button(self):
        return self.find_element((By.XPATH, '//a[contains(text(), "Products")]'))

    def solutions_button(self):
        return self.find_element((By.XPATH, '//a[contains(text(),"Solutions")]'))

    def resources_button(self):
        return self.find_element((By.XPATH, '//a[contains(text(),"Resources")]'))

    def contact_us_button(self):
        return self.find_element((By.XPATH, '//a[contains(text(),"Contact Us")]'))

    def accept_all_pop_up_button(self):
        return self.find_element((By.XPATH, '//*[text()="Accept All"]'))

    def click(self):
        pass
